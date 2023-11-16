import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QTableWidgetItem

from camera import OlympusCamera
from mainwindow import Ui_MainWindow
from properties import Ui_PropertiesDialog
from settings import Ui_SettingsDialog


class PropertiesDialog(QDialog, Ui_PropertiesDialog):
    def __init__(self, camera: OlympusCamera, *args, obj=None, **kwargs):
        super(PropertiesDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle(f"{camera.camera_info['model']} camera properties")
        camera.send_command('switch_cammode', mode='rec')
        xml = camera.xml_query('get_camprop', com='desc', propname='desclist')
        camera.send_command('switch_cammode', mode='play')
        self.properties.setRowCount(5 + len(xml))

        self.properties.setItem(0, 0, QTableWidgetItem("Camera"))
        self.properties.setItem(0, 1, QTableWidgetItem(camera.camera_info["model"]))
        self.properties.setItem(1, 0, QTableWidgetItem("Version"))
        self.properties.setItem(1, 1, QTableWidgetItem(camera.versions["version"]))
        self.properties.setItem(2, 0, QTableWidgetItem("Supported"))
        self.properties.setItem(2, 1, QTableWidgetItem('.'.join(camera.supported)))
        self.properties.setItem(3, 0, QTableWidgetItem("Freespace"))
        self.properties.setItem(3, 1, QTableWidgetItem(camera.get_unusedcapacity()))
        self.properties.setItem(4, 0, QTableWidgetItem("Dcf file"))
        self.properties.setItem(4, 1, QTableWidgetItem(camera.xml_query('get_dcffilenum')['dcffile']))
        i = 5
        for row in xml:
            self.properties.setItem(i, 0, QTableWidgetItem(row["propname"]))
            self.properties.setItem(i, 1, QTableWidgetItem(row["value"]))
            self.properties.setItem(i, 2, QTableWidgetItem(row["attribute"]))
            if "enum" in row:
                self.properties.setItem(i, 3, QTableWidgetItem(row["enum"]))
            i += 1


class SettingsDialog(QDialog,Ui_SettingsDialog):
    def __init__(self,*args, obj=None,**kwargs):
        super(SettingsDialog,self).__init__(*args,**kwargs)
        self.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.camera = None
        self.setupUi(self)
        self.ip = ""
        self.connected = False
        self.actionConnect_camera.triggered.connect(self.file_open_camera)
        self.actionConnect_MockService.triggered.connect(self.file_open_mockservice)
        self.actionE_xit.triggered.connect(self.file_exit)
        self.actionCamera_properties.triggered.connect(self.file_camera_properties)
        self.action_About.triggered.connect(self.help_about)
        self.action_Settings.triggered.connect(self.file_settings)

    def file_open_camera(self) -> None:
        self.connect_camera()

    def file_open_mockservice(self) -> None:
        self.connect_camera("http://127.0.0.1:8080/")

    def file_camera_properties(self) -> None:
        if self.connected:
            dlg = PropertiesDialog(self.camera)
            dlg.exec()

    def help_about(self) -> None:
        QMessageBox.about(self, "Olympus GUI", "Image downloader for Olympus cameras")

    def file_exit(self) -> None:
        self.close()

    def file_settings(self) -> None:
        dlg=SettingsDialog()
        if dlg.exec():
            pass

    def refresh(self) -> None:
        pass

    def connect_camera(self, prefix: str = "") -> None:
        try:
            self.camera = OlympusCamera(prefix)
            self.connected = True
            self.refresh()
            self.statusbar.showMessage(f"Connected: {self.camera.camera_info['model']}", 20000)
        except ConnectionError as ex:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error!")
            dlg.setText(str(ex))
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
