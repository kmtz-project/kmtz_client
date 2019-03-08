# -*- coding: utf-8 -*-

import sys, os
from PyQt5.QtWidgets import QDialog, QGridLayout, QSizePolicy, QFileDialog
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class SettingsDialog(QDialog):

    imgFolderEdit   = None
    lidarFolderEdit = None
    ipEdit          = None
    portEdit        = None

    imgFolderDialog   = None
    lidarFolderDialog = None
    
    def __init__(self):
        super().__init__()

        self.imgFolderDialog   = QFileDialog(self, "Select IMG directory")
        self.imgFolderDialog.setFileMode(QFileDialog.Directory)
        self.lidarFolderDialog = QFileDialog(self, "Select LIDAR directory")
        self.lidarFolderDialog.setFileMode(QFileDialog.Directory)

        self.initUI()

    def initUI(self):

        # Create Widgets
        self.imgFolderEdit   = QLineEdit(os.getcwd() + "\\IMG")
        self.lidarFolderEdit = QLineEdit(os.getcwd() + "\\LIDAR")
        
        self.ipEdit   = QLineEdit("192.168.1.2")
        self.portEdit = QLineEdit("22")
        self.portEdit.setFixedSize(70, 25)
        
        openImgFolderBtn   = QPushButton("Open")
        openImgFolderBtn.setFixedSize(70, 25)
        openImgFolderBtn.clicked.connect(self.imgFolderDialog.exec)

        openLidarFolderBtn = QPushButton("Open")
        openLidarFolderBtn.setFixedSize(70, 25)
        openLidarFolderBtn.clicked.connect(self.lidarFolderDialog.exec)

        saveBtn = QPushButton("Save")
        saveBtn.setFixedSize(70, 25)

        # Create Layout
        gridLayout = QGridLayout()

        gridLayout.setColumnMinimumWidth(1, 200)
        gridLayout.setColumnMinimumWidth(2, 10)

        gridLayout.addWidget(QLabel("Image folder:"), 0, 0)
        gridLayout.addWidget(self.imgFolderEdit, 0, 1)
        gridLayout.addWidget(openImgFolderBtn, 0, 2)

        gridLayout.addWidget(QLabel("LIDAR data folder:"), 1, 0)
        gridLayout.addWidget(self.lidarFolderEdit, 1, 1)
        gridLayout.addWidget(openLidarFolderBtn, 1, 2)

        gridLayout.addWidget(QLabel("KMTZ IP and port:"), 2, 0)
        gridLayout.addWidget(self.ipEdit, 2, 1)
        gridLayout.addWidget(self.portEdit, 2, 2)

        gridLayout.addWidget(saveBtn, 3, 2)

        self.setLayout(gridLayout)
        
        # Set Window Settings        
        #self.resize(400, 400)
        self.setWindowTitle("Settings")
        self.setWindowModality(Qt.ApplicationModal)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setWindowFlags (self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
