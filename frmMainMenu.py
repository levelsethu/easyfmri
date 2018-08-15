#!/usr/bin/env python3
from frmMainMenuGUI import *
from frmPreprocess import *
import PyQt5.QtWidgets as QtWidgets
#import PyQt5.QtCore as QtCore
from pyqode.core import api
from pyqode.core import modes
from pyqode.core import panels
from pyqode.qt import QtWidgets as pyWidgets
import numpy, scipy, sklearn
import os, platform
import nibabel, nipype

import sys
import subprocess
import configparser as cp
import glob

from frmSelectSession   import frmSelectSession
from frmEventViewer     import frmEventViewer
from frmRenameFile      import frmRenameFile
from frmScriptEditor    import frmScriptEditor

from utility            import getTimeSliceText,fixstr,setParameters
from Setting            import Setting
from SettingHistory     import History
from BrainExtractor     import BrainExtractor
from EventGenerator     import EventGenerator
from ScriptGenerator    import ScriptGenerator
from RunPreprocess      import RunPreprocess


def About():
    return """<h1>easy fMRI project</h1>
<h3>A toolbox for Human Brain Mapping and Decoding</h3>
<h4>Website: <a href=\"https://easyfmri.github.io\">https://easyfmri.github.io</a></h4>
<p>Created by:</p>
<p><a href=\"https://myousefnezhad.github.io\">Muhammad Yousefnezhad</a>, <a href=\"http://ibrain.nuaa.edu.cn\">iBRAIN Group</a>,</p>
<p><a href=\"http://iao.nuaa.edu.cn\">Nanjing University of Aeronautics and Astronautics</a>, China.<p></h6>
"""


class frmMainMenuGUI(QtWidgets.QMainWindow):
    dialog = None
    ui = Ui_frmMainMenuGUI()


    def show(self):
        from utility import getVersion
        global dialog, ui
        ui = Ui_frmMainMenuGUI()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)


        dialog.setWindowTitle("easy fMRI - " + getVersion())

        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())


        ui.btnFeatureAnalysis.setEnabled(False)
        ui.btnModelAnalysis.setEnabled(False)
        ui.btnVisualization.setEnabled(False)


        dialog.show()


    def set_events(self):
        global ui
        ui.btnExit.clicked.connect(self.btnExit_click)
        ui.btnPreprocess.clicked.connect(self.btnPreprocess_click)
        ui.btnAbout.clicked.connect(self.btnAbout_click)


    def btnExit_click(self):
         import sys
         sys.exit()

    def btnAbout_click(self):
        from utility import MyMessageBox

        msgBox = MyMessageBox()
        msgBox.setMinimumWidth(800)
        msgBox.setText(About())
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
        pass

    def btnPreprocess_click(self):
        global dialog
        dialog.hide()
        frmPreprocess.show(frmPreprocess,dialog)
        #dialog.show()

# Auto Run
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmMainMenuGUI.show(frmMainMenuGUI)
    sys.exit(app.exec_())