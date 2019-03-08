# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initMenu()
        self.initWindow()

    def initMenu(self):

        menubar = self.menuBar()
        #menubar.setStyleSheet("")

        # File menu items
        exitAction = QAction('&Exit', self)
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        exitAction.setIconVisibleInMenu(False)

        settingsAction = QAction('&Settings', self)
        settingsAction.setStatusTip('Open Settings Dialog')

        appMenu = menubar.addMenu('&Application')
        appMenu.addAction(settingsAction)
        appMenu.addAction(exitAction)

        #appMenu.setStyleSheet("QMenu::item::selected { background-color: rgb(30,30,30) } QMenu { background-color: rgb(0,0,0) }")

        # Tools menu items
        toolsMenu = menubar.addMenu('&Tools')

    def initWindow(self):

        self.setStyleSheet(open("qss/mainwindow.css", "r").read())

        self.setFixedSize(800, 600)
        self.setWindowTitle('KMTZ GUI')
        self.statusBar().showMessage('Ready')

        self.show()
