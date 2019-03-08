# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QDialog, QPushButton, QLayout
from PyQt5.QtCore import Qt

class SettingsDialog(QDialog):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        gridLayout = 
        
        self.resize(400, 400)
        self.setWindowTitle("Dialog")
        self.setWindowModality(Qt.ApplicationModal)
