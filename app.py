import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from camera import OlympusCamera
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.ip = ""
        self.connected = False
        self.actionConnect_camera.triggered.connect(self.file_open_camera)
        self.actionConnect_MockService.triggered.connect(self.file_open_mockservice)
        self.actionE_xit.triggered.connect(self.file_exit)

    def file_open_camera(self)->None:
        self.connect_camera()

    def file_open_mockservice(self)->None:
        self.connect_camera("http://127.0.0.1:8080/")

    def file_exit(self)->None:
        self.close()

    def refresh(self)->None:
        pass

    def connect_camera(self, prefix: str = "") -> None:
        try:
            self.camera = OlympusCamera(prefix)
            self.connected = True
            self.refresh()
            self.statusbar.showMessage(f"Connected: {self.camera.camera_info['model']}",20000)
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
