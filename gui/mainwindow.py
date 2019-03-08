# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from gui.settingsDialog import SettingsDialog

class MainWindow(QMainWindow):

    settingsDialog = None

    def __init__(self):
        super().__init__()

        self.settingsDialog = SettingsDialog()

        self.initMenu()
        self.initWindow()

    def initMenu(self):

        menubar = self.menuBar()

        #connectAction = QAction('&Connect', self)
        #connectAction.setStatusTip('Connect to KMTZ')
        #menubar.addAction(connectAction);

        # File menu items
        exitAction = QAction('&Exit', self)
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
 
        settingsAction = QAction('&Settings', self)
        settingsAction.setStatusTip('Open settings dialog')
        settingsAction.triggered.connect(self.settingsDialog.exec)

        appMenu = menubar.addMenu('&Application')
        appMenu.addAction(settingsAction)
        appMenu.addAction(exitAction)

        # Tools menu items
        calibAction = QAction('&Calibration', self)
        calibAction.setStatusTip('Do calibration task')

        toolsMenu = menubar.addMenu('&Tools')
        toolsMenu.addAction(calibAction)

    def initWindow(self):

        self.setStyleSheet(open("qss/mainwindow.css", "r").read())

        self.resize(800, 600)
        self.setWindowTitle('KMTZ GUI')
        self.statusBar().showMessage('Ready')

        self.show()
