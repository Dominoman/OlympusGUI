from dataclasses import dataclass
from datetime import datetime, time
from typing import Dict, Set, Optional, Union, List
import xml.etree.ElementTree as ElementTree

import requests


class RequestError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class ResultError(Exception):
    def __init__(self, msg: str, response: requests.Response) -> None:
        super().__init__(msg)
        self.response = response


class OlympusCamera:
    @dataclass
    class CmdDescr:
        method: str
        args: Optional[Dict[str, Optional[dict]]]

    URL_PREFIX = "http:/192.168.0.10/"
    HEADERS = {'Host': '192.168.0.10',
               'User-Agent': 'OI.Share v2'}
    ANY_PARAMETER = '*'
    EMPTY_PARAMETERS: Dict[str, Optional[dict]] = {ANY_PARAMETER: None}

    def __init__(self, prefix: str = "") -> None:
        if prefix != "":
            self.URL_PREFIX = prefix
        self.versions: Dict[str, str] = {}
        self.supported: Set[str] = set()
        self.camera_info = None
        self.commands: Dict[str, CmdDescr] = {
            'get_commandlist': self.CmdDescr('get', None)
        }

        response = self.send_command('get_commandlist')
        if response is None:
            return

        for elem in ElementTree.fromstring(response.text):
            if elem.tag == 'cgi':
                for http_method in elem:
                    if http_method.tag == 'http_method':
                        self.commands[elem.attrib['name']] = self.CmdDescr(http_method.attrib['type'],
                                                                           self.commandlist_cmds(http_method))
            elif elem.tag == 'support':
                self.supported.add(elem.attrib['func'])
            elif elem.tag == 'version':
                self.versions[elem.tag] = elem.text.strip()

        self.camera_info = self.xml_query('get_caminfo')
        self.send_command('switch_cammode', mode='rec')
        self.camprop_name2values = {
            prop['propname']: prop['enum'].split() for prop in
            self.xml_query('get_camprop', com='desc', propname='desclist') if
            prop['attribute'] == 'getset' and 'enum' in prop
        }
        self.send_command('switch_cammode', mode='play')

    def commandlist_params(self, parent: ElementTree.Element) -> Dict[str, Optional[dict]]:
        """Parse parameters in the XML output of command get_commandlist."""
        params = {}
        for param in parent:
            if param.tag.startswith('cmd'):
                return {self.ANY_PARAMETER: {param.attrib['name'].strip(): self.commandlist_params(param)}}
            name = param.attrib['name'].strip() if 'name' in param.attrib else self.ANY_PARAMETER
            params[name] = self.commandlist_cmds(param)
        return params if len(params) else self.EMPTY_PARAMETERS

    def commandlist_cmds(self, parent: ElementTree.Element) -> Optional[Dict[str, Optional[dict]]]:
        """Parse commands in the XML output of command get_commandlist."""
        cmds: Dict[str, Optional[dict]] = {}
        for cmd in parent:
            assert cmd.tag.startswith('cmd')
            cmds[cmd.attrib['name'].strip()] = self.commandlist_params(cmd)
        return cmds if cmds else None

    def send_command(self, command: str, **args) -> requests.Response:
        self.check_valid_command(command, args)
        url = f'{self.URL_PREFIX}{command}.cgi'
        if self.commands[command].method == 'get':
            response = requests.get(url, headers=self.HEADERS, params=args)
        else:
            assert self.commands[command].method == 'post'
            if 'post_data' not in args:
                raise RequestError(
                    f"Error in '{command}' with args '{', '.join([f'{k}={v}' for k, v in args.items()])}': missing entry 'post_data' for method 'post'."
                )
            post_data = args['post_data']
            del args['post_data']
            headers = self.HEADERS.copy()
            if len(post_data) > 6 and post_data[:6] == "<?xml ".encode('utf-8'):
                headers['Content-type'] = 'text/plain;charset=utf-8'
            response = requests.post(url, headers=headers, params=args, data=post_data)

        if response.status_code in [requests.codes.ok, requests.codes.accepted]:
            return response
        err_xml = self.xml_response(response)
        if isinstance(err_xml, dict):
            msg = ', '.join([f'{key}={value}' for key, value in err_xml.items()])
        else:
            msg = response.text.replace('\r\n', '')
        raise ResultError(f"Error #{response.status_code} "
                          f"for url {response.url.replace('%2F', '/')}: "
                          f"{msg}.", response)

    def check_valid_command(self, command: str, args: Dict[str, CmdDescr]) -> None:
        if command not in self.commands:
            raise RequestError(f"Error: command {command} not supported; "
                               "valid commands: "
                               f"{','.join(list(self.commands))}")
        valid_command_arguments = self.commands[command].args
        wildcard = self.ANY_PARAMETER
        for key, value in args.items():
            if key == 'post_date' and self.commands[command].method == 'post':
                if not isinstance(value, bytes):
                    raise RequestError(f"Error in {command}: data for method "
                                       f"'post' is of type '{type(value)}'; "
                                       "type 'bytes' expected.")
                continue
            if valid_command_arguments is None:
                raise RequestError(f"Error in {command}: '{key}' in "
                                   f"{key}={value} not supported.")

            if key in valid_command_arguments:
                valid_command_arguments = valid_command_arguments[key]
            elif wildcard in valid_command_arguments:
                valid_command_arguments = valid_command_arguments[wildcard]
            else:
                raise RequestError(f"Error in {command}: '{key}' in "
                                   f"{key}={value} not supported; supported: "
                                   f"{', '.join(list(valid_command_arguments))}.")

            if value in valid_command_arguments:
                valid_command_arguments = valid_command_arguments[value]
            elif wildcard in valid_command_arguments:
                valid_command_arguments = valid_command_arguments[wildcard]
            else:
                raise RequestError(
                    f"Error in {command}: '{value}' in {key}={value} not supported; supported:{', '.join([f'{key}={v}' for v in valid_command_arguments])}."
                )

    def xml_response(self, response: requests.Response) -> Optional[Union[Dict[str, str], List[Dict[str, str]]]]:
        if 'Content-Type' in response.headers and response.headers['Content-Type'] == 'text/xml':
            xml = ElementTree.fromstring(response.text)
            my_dict: Dict[str, str] = {}
            if my_list := self.xml2dict(xml, my_dict):
                return my_list[0] if len(my_list) == 1 else my_list
            else:
                return my_dict
        return None

    def xml2dict(self, xml: ElementTree.Element, parent: Dict[str, str]) -> List[Dict[str, str]]:
        if xml.text and xml.text.strip():
            parent[xml.tag] = xml.text.strip()
            return []
        results = []
        params: Dict[str, str] = {}
        for elem in xml:
            results += self.xml2dict(elem, params)
        if params:
            results.append(params)
        return results

    def xml_query(self, command: str, **args) -> Optional[Union[Dict[str, str], List[Dict[str, str]]]]:
        return self.xml_response(self.send_command(command, **args))

    def set_clock(self) -> None:
        self.send_command('switch_cammode', mode='play')
        self.send_command('set_utctimediff', utctime=datetime.utcnow().strftime("%Y%m%dT%H%M%S"),
                          diff=time.strftime("%z"))

    def get_unusedcapacity(self)->str:
        result=self.xml_query('get_unusedcapacity')
        return result['unused']
