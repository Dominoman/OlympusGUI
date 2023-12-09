# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionE_xit = QAction(MainWindow)
        self.actionE_xit.setObjectName(u"actionE_xit")
        self.actionConnect_camera = QAction(MainWindow)
        self.actionConnect_camera.setObjectName(u"actionConnect_camera")
        self.actionConnect_MockService = QAction(MainWindow)
        self.actionConnect_MockService.setObjectName(u"actionConnect_MockService")
        self.actionCamera_properties = QAction(MainWindow)
        self.actionCamera_properties.setObjectName(u"actionCamera_properties")
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        self.action_Settings = QAction(MainWindow)
        self.action_Settings.setObjectName(u"action_Settings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.log = QTextEdit(self.centralwidget)
        self.log.setObjectName(u"log")
        self.log.setReadOnly(True)

        self.horizontalLayout.addWidget(self.log)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_File.addAction(self.actionConnect_camera)
        self.menu_File.addAction(self.actionConnect_MockService)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionCamera_properties)
        self.menu_File.addAction(self.action_Settings)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionE_xit)
        self.menu_Help.addAction(self.action_About)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionE_xit.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
        self.actionConnect_camera.setText(QCoreApplication.translate("MainWindow", u"Connect camera", None))
        self.actionConnect_MockService.setText(QCoreApplication.translate("MainWindow", u"Connect MockService", None))
        self.actionCamera_properties.setText(QCoreApplication.translate("MainWindow", u"Camera properties...", None))
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"&About", None))
        self.action_Settings.setText(QCoreApplication.translate("MainWindow", u"&Settings...", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi

