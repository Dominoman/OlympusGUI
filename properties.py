# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'properties.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHeaderView, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_PropertiesDialog(object):
    def setupUi(self, PropertiesDialog):
        if not PropertiesDialog.objectName():
            PropertiesDialog.setObjectName(u"PropertiesDialog")
        PropertiesDialog.resize(427, 311)
        self.verticalLayout = QVBoxLayout(PropertiesDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.properties = QTableWidget(PropertiesDialog)
        if (self.properties.columnCount() < 4):
            self.properties.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.properties.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.properties.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.properties.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.properties.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.properties.setObjectName(u"properties")

        self.verticalLayout.addWidget(self.properties)

        self.buttonBox = QDialogButtonBox(PropertiesDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(PropertiesDialog)
        self.buttonBox.accepted.connect(PropertiesDialog.accept)
        self.buttonBox.rejected.connect(PropertiesDialog.reject)

        QMetaObject.connectSlotsByName(PropertiesDialog)
    # setupUi

    def retranslateUi(self, PropertiesDialog):
        PropertiesDialog.setWindowTitle(QCoreApplication.translate("PropertiesDialog", u"Camera properies", None))
        ___qtablewidgetitem = self.properties.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PropertiesDialog", u"Name", None));
        ___qtablewidgetitem1 = self.properties.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PropertiesDialog", u"Value", None));
        ___qtablewidgetitem2 = self.properties.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PropertiesDialog", u"Attribute", None));
        ___qtablewidgetitem3 = self.properties.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PropertiesDialog", u"Enum", None));
    # retranslateUi

