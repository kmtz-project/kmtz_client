# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QListWidget, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QComboBox, QPushButton, QSizePolicy, QSpacerItem
from gui.settingsDialog import SettingsDialog

class MainWindow(QMainWindow):

    settingsDialog   = None
    imgLeftLabel     = None
    imgRightlabel    = None
    folderListWidget = None

    depthMethodCBox  = None
    procMethodCBox   = None

    def __init__(self):
        super().__init__()

        self.settingsDialog = SettingsDialog()

        self.initMenu()
        self.initBody()
        self.initWindow()

    def initBody(self):

        self.imgLeftLabel  = QLabel("Image left")
        self.imgLeftLabel.setAlignment(Qt.AlignCenter)
        self.imgLeftLabel.setMinimumSize(400, 200)
        self.imgRightLabel = QLabel("Image right")
        self.imgRightLabel.setAlignment(Qt.AlignCenter)
        self.imgRightLabel.setMinimumSize(400, 200)

        self.folderListWidget = QListWidget()
        self.folderListWidget.setMinimumSize(200, 200)

        depthMethodLabel = QLabel("Depth calc method")
        procMethodLabel  = QLabel("Processing method")

        showDepthBtn    = QPushButton("Show depth")
        showDepthBtn.setFixedSize(100, 24)
        doProcBtn       = QPushButton("Do processing")
        doProcBtn.setFixedSize(100, 24)
        saveImgBtn      = QPushButton("Save images")
        deleteFolderBtn = QPushButton("Delete folder")

        depthMethodCBox = QComboBox()
        procMethodCBox  = QComboBox()

        # Column 1
        col1Layout = QVBoxLayout()
        col1Widget = QWidget()
        col1Widget.setLayout(col1Layout)
        col1SizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        col1SizePolicy.setHorizontalStretch(2)
        col1Widget.setSizePolicy(col1SizePolicy)
        col1Spacer = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        depthMethodWidget = QWidget()
        depthMethodWLayout = QGridLayout()
        depthMethodWidget.setLayout(depthMethodWLayout)
        depthMethodWLayout.addWidget(depthMethodLabel, 0, 0)
        depthMethodWLayout.addWidget(depthMethodCBox, 1, 0)
        depthMethodWLayout.addWidget(showDepthBtn, 1, 1)

        col1Layout.addWidget(self.imgLeftLabel)
        col1Layout.addItem(col1Spacer)
        col1Layout.addWidget(depthMethodWidget)

        # Column 2
        col2Layout = QVBoxLayout()
        col2Widget = QWidget()
        col2Widget.setLayout(col2Layout)
        col2SizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        col2SizePolicy.setHorizontalStretch(2)
        col2Widget.setSizePolicy(col2SizePolicy)
        col2Spacer = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        procMethodWidget = QWidget()
        procMethodWLayout = QGridLayout()
        procMethodWidget.setLayout(procMethodWLayout)
        procMethodWLayout.addWidget(procMethodLabel, 0, 0)
        procMethodWLayout.addWidget(procMethodCBox, 1, 0)
        procMethodWLayout.addWidget(doProcBtn, 1, 1)

        col2Layout.addWidget(self.imgRightLabel)
        col2Layout.addItem(col2Spacer)
        col2Layout.addWidget(procMethodWidget)

        # Column 3
        col3Layout = QVBoxLayout()
        col3Widget = QWidget()
        col3Widget.setLayout(col3Layout)
        col3SizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        col3SizePolicy.setHorizontalStretch(1)
        col3Widget.setSizePolicy(col3SizePolicy)

        col3Layout.addWidget(self.folderListWidget)
        col3Layout.addWidget(saveImgBtn)
        col3Layout.addWidget(deleteFolderBtn)

        # Main Layout
        hBoxLayout = QHBoxLayout()
        hBoxLayout.addWidget(col1Widget)
        hBoxLayout.addWidget(col2Widget)
        hBoxLayout.addWidget(col3Widget)

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(hBoxLayout)



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
        #self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.show()
