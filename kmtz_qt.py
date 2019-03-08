# -*- coding: utf-8 -*-

import sys
from gui.mainwindow  import MainWindow
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt


if __name__ == '__main__':

    app = QApplication(sys.argv)

    #app.setAttribute(Qt.AA_DontShowIconsInMenus, True)

    w = MainWindow()

    sys.exit(app.exec_())
