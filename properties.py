# Form implementation generated from reading ui file 'C:\Users\oraveczl\PycharmProjects\OlympusGUI\ui\properties.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PropertiesDialog(object):
    def setupUi(self, PropertiesDialog):
        PropertiesDialog.setObjectName("PropertiesDialog")
        PropertiesDialog.resize(427, 311)
        self.verticalLayout = QtWidgets.QVBoxLayout(PropertiesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.properties = QtWidgets.QTableWidget(parent=PropertiesDialog)
        self.properties.setObjectName("properties")
        self.properties.setColumnCount(4)
        self.properties.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.properties.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.properties.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.properties.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.properties.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.properties)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=PropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PropertiesDialog)
        self.buttonBox.accepted.connect(PropertiesDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(PropertiesDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PropertiesDialog)

    def retranslateUi(self, PropertiesDialog):
        _translate = QtCore.QCoreApplication.translate
        PropertiesDialog.setWindowTitle(_translate("PropertiesDialog", "Camera properies"))
        item = self.properties.horizontalHeaderItem(0)
        item.setText(_translate("PropertiesDialog", "Name"))
        item = self.properties.horizontalHeaderItem(1)
        item.setText(_translate("PropertiesDialog", "Value"))
        item = self.properties.horizontalHeaderItem(2)
        item.setText(_translate("PropertiesDialog", "Attribute"))
        item = self.properties.horizontalHeaderItem(3)
        item.setText(_translate("PropertiesDialog", "Enum"))
