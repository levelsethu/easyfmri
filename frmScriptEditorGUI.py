# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmScriptEditorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmScriptEditor(object):
    def setupUi(self, frmScriptEditor):
        frmScriptEditor.setObjectName("frmScriptEditor")
        frmScriptEditor.resize(663, 657)
        self.groupBox_3 = QtWidgets.QGroupBox(frmScriptEditor)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 98, 621, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 35, 60, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(300, 35, 60, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(480, 35, 60, 16))
        self.label_10.setObjectName("label_10")
        self.txtRunPer = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtRunPer.setGeometry(QtCore.QRect(530, 35, 80, 21))
        self.txtRunPer.setObjectName("txtRunPer")
        self.txtRunLen = QtWidgets.QSpinBox(self.groupBox_3)
        self.txtRunLen.setGeometry(QtCore.QRect(370, 35, 80, 24))
        self.txtRunLen.setMaximum(100000)
        self.txtRunLen.setProperty("value", 2)
        self.txtRunLen.setObjectName("txtRunLen")
        self.txtRunNum = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtRunNum.setGeometry(QtCore.QRect(75, 35, 211, 21))
        self.txtRunNum.setObjectName("txtRunNum")
        self.groupBox = QtWidgets.QGroupBox(frmScriptEditor)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 621, 80))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 35, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(300, 35, 60, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(480, 35, 60, 16))
        self.label_4.setObjectName("label_4")
        self.txtSubPer = QtWidgets.QLineEdit(self.groupBox)
        self.txtSubPer.setGeometry(QtCore.QRect(530, 35, 80, 21))
        self.txtSubPer.setObjectName("txtSubPer")
        self.txtSubLen = QtWidgets.QSpinBox(self.groupBox)
        self.txtSubLen.setGeometry(QtCore.QRect(370, 35, 80, 24))
        self.txtSubLen.setMaximum(100000)
        self.txtSubLen.setSingleStep(1)
        self.txtSubLen.setProperty("value", 2)
        self.txtSubLen.setObjectName("txtSubLen")
        self.txtSubFrom = QtWidgets.QSpinBox(self.groupBox)
        self.txtSubFrom.setGeometry(QtCore.QRect(60, 35, 80, 24))
        self.txtSubFrom.setMaximum(100000)
        self.txtSubFrom.setProperty("value", 1)
        self.txtSubFrom.setObjectName("txtSubFrom")
        self.txtSubTo = QtWidgets.QSpinBox(self.groupBox)
        self.txtSubTo.setGeometry(QtCore.QRect(200, 35, 80, 24))
        self.txtSubTo.setMaximum(100000)
        self.txtSubTo.setProperty("value", 1)
        self.txtSubTo.setObjectName("txtSubTo")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(160, 35, 60, 16))
        self.label_7.setObjectName("label_7")
        self.groupBox_4 = QtWidgets.QGroupBox(frmScriptEditor)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 273, 621, 151))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(11, 69, 81, 16))
        self.label_5.setObjectName("label_5")
        self.txtTask = QtWidgets.QLineEdit(self.groupBox_4)
        self.txtTask.setGeometry(QtCore.QRect(100, 70, 501, 21))
        self.txtTask.setText("")
        self.txtTask.setObjectName("txtTask")
        self.btnDIR = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDIR.setGeometry(QtCore.QRect(559, 26, 51, 32))
        self.btnDIR.setObjectName("btnDIR")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(10, 31, 111, 16))
        self.label.setToolTip("")
        self.label.setStatusTip("")
        self.label.setProperty("toolTipDuration", -1)
        self.label.setObjectName("label")
        self.txtDIR = QtWidgets.QLineEdit(self.groupBox_4)
        self.txtDIR.setGeometry(QtCore.QRect(118, 31, 431, 21))
        self.txtDIR.setToolTip("")
        self.txtDIR.setStatusTip("")
        self.txtDIR.setText("")
        self.txtDIR.setProperty("toolTipDuration", -1)
        self.txtDIR.setObjectName("txtDIR")
        self.txtScript = QtWidgets.QLineEdit(self.groupBox_4)
        self.txtScript.setGeometry(QtCore.QRect(120, 108, 481, 21))
        self.txtScript.setObjectName("txtScript")
        self.label_34 = QtWidgets.QLabel(self.groupBox_4)
        self.label_34.setGeometry(QtCore.QRect(11, 108, 201, 16))
        self.label_34.setObjectName("label_34")
        self.groupBox_2 = QtWidgets.QGroupBox(frmScriptEditor)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 185, 621, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 35, 60, 16))
        self.label_6.setObjectName("label_6")
        self.txtConFrom = QtWidgets.QSpinBox(self.groupBox_2)
        self.txtConFrom.setGeometry(QtCore.QRect(60, 35, 80, 24))
        self.txtConFrom.setMaximum(100000)
        self.txtConFrom.setProperty("value", 1)
        self.txtConFrom.setObjectName("txtConFrom")
        self.txtConTo = QtWidgets.QSpinBox(self.groupBox_2)
        self.txtConTo.setGeometry(QtCore.QRect(200, 35, 80, 24))
        self.txtConTo.setMaximum(100000)
        self.txtConTo.setProperty("value", 1)
        self.txtConTo.setObjectName("txtConTo")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(160, 35, 60, 16))
        self.label_15.setObjectName("label_15")
        self.txtConPer = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtConPer.setGeometry(QtCore.QRect(530, 35, 80, 21))
        self.txtConPer.setObjectName("txtConPer")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(480, 35, 60, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(300, 35, 60, 21))
        self.label_12.setObjectName("label_12")
        self.txtConLen = QtWidgets.QSpinBox(self.groupBox_2)
        self.txtConLen.setGeometry(QtCore.QRect(370, 35, 80, 24))
        self.txtConLen.setMaximum(100000)
        self.txtConLen.setSingleStep(1)
        self.txtConLen.setProperty("value", 2)
        self.txtConLen.setObjectName("txtConLen")
        self.groupBox_5 = QtWidgets.QGroupBox(frmScriptEditor)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 435, 621, 111))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(11, 69, 101, 16))
        self.label_16.setObjectName("label_16")
        self.txtOutput = QtWidgets.QLineEdit(self.groupBox_5)
        self.txtOutput.setGeometry(QtCore.QRect(120, 70, 401, 21))
        self.txtOutput.setText("")
        self.txtOutput.setObjectName("txtOutput")
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(10, 31, 111, 16))
        self.label_17.setToolTip("")
        self.label_17.setStatusTip("")
        self.label_17.setProperty("toolTipDuration", -1)
        self.label_17.setObjectName("label_17")
        self.txtInput = QtWidgets.QLineEdit(self.groupBox_5)
        self.txtInput.setGeometry(QtCore.QRect(100, 31, 421, 21))
        self.txtInput.setToolTip("")
        self.txtInput.setStatusTip("")
        self.txtInput.setText("")
        self.txtInput.setProperty("toolTipDuration", -1)
        self.txtInput.setObjectName("txtInput")
        self.cbInDynamic = QtWidgets.QCheckBox(self.groupBox_5)
        self.cbInDynamic.setGeometry(QtCore.QRect(530, 31, 87, 20))
        self.cbInDynamic.setChecked(True)
        self.cbInDynamic.setObjectName("cbInDynamic")
        self.cbOutDynamic = QtWidgets.QCheckBox(self.groupBox_5)
        self.cbOutDynamic.setGeometry(QtCore.QRect(530, 70, 87, 20))
        self.cbOutDynamic.setChecked(True)
        self.cbOutDynamic.setObjectName("cbOutDynamic")
        self.label_23 = QtWidgets.QLabel(frmScriptEditor)
        self.label_23.setGeometry(QtCore.QRect(20, 610, 621, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_23.setObjectName("label_23")
        self.btnExit = QtWidgets.QPushButton(frmScriptEditor)
        self.btnExit.setGeometry(QtCore.QRect(530, 560, 113, 32))
        self.btnExit.setObjectName("btnExit")
        self.btnRun = QtWidgets.QPushButton(frmScriptEditor)
        self.btnRun.setGeometry(QtCore.QRect(20, 560, 113, 32))
        self.btnRun.setObjectName("btnRun")
        self.cbDEMO = QtWidgets.QCheckBox(frmScriptEditor)
        self.cbDEMO.setGeometry(QtCore.QRect(150, 563, 87, 20))
        self.cbDEMO.setObjectName("cbDEMO")

        self.retranslateUi(frmScriptEditor)
        QtCore.QMetaObject.connectSlotsByName(frmScriptEditor)
        frmScriptEditor.setTabOrder(self.txtSubFrom, self.txtSubTo)
        frmScriptEditor.setTabOrder(self.txtSubTo, self.txtSubLen)
        frmScriptEditor.setTabOrder(self.txtSubLen, self.txtSubPer)
        frmScriptEditor.setTabOrder(self.txtSubPer, self.txtRunNum)
        frmScriptEditor.setTabOrder(self.txtRunNum, self.txtRunLen)
        frmScriptEditor.setTabOrder(self.txtRunLen, self.txtRunPer)
        frmScriptEditor.setTabOrder(self.txtRunPer, self.txtConFrom)
        frmScriptEditor.setTabOrder(self.txtConFrom, self.txtConTo)
        frmScriptEditor.setTabOrder(self.txtConTo, self.txtConLen)
        frmScriptEditor.setTabOrder(self.txtConLen, self.txtConPer)
        frmScriptEditor.setTabOrder(self.txtConPer, self.txtDIR)
        frmScriptEditor.setTabOrder(self.txtDIR, self.btnDIR)
        frmScriptEditor.setTabOrder(self.btnDIR, self.txtTask)
        frmScriptEditor.setTabOrder(self.txtTask, self.txtInput)
        frmScriptEditor.setTabOrder(self.txtInput, self.txtOutput)
        frmScriptEditor.setTabOrder(self.txtOutput, self.btnExit)
        frmScriptEditor.setTabOrder(self.btnExit, self.btnRun)

    def retranslateUi(self, frmScriptEditor):
        _translate = QtCore.QCoreApplication.translate
        frmScriptEditor.setWindowTitle(_translate("frmScriptEditor", "Group Script Editor"))
        self.groupBox_3.setTitle(_translate("frmScriptEditor", "<Runs>"))
        self.label_8.setText(_translate("frmScriptEditor", "Number:"))
        self.label_9.setText(_translate("frmScriptEditor", "Length:"))
        self.label_10.setText(_translate("frmScriptEditor", "Perfix:"))
        self.txtRunPer.setText(_translate("frmScriptEditor", "0"))
        self.txtRunNum.setText(_translate("frmScriptEditor", "1"))
        self.groupBox.setTitle(_translate("frmScriptEditor", "<Subjects>"))
        self.label_2.setText(_translate("frmScriptEditor", "From:"))
        self.label_3.setText(_translate("frmScriptEditor", "Length:"))
        self.label_4.setText(_translate("frmScriptEditor", "Perfix:"))
        self.txtSubPer.setText(_translate("frmScriptEditor", "0"))
        self.label_7.setText(_translate("frmScriptEditor", "To:"))
        self.groupBox_4.setTitle(_translate("frmScriptEditor", "<General>"))
        self.label_5.setText(_translate("frmScriptEditor", "Task Name:"))
        self.btnDIR.setText(_translate("frmScriptEditor", "..."))
        self.label.setText(_translate("frmScriptEditor", "Main Directory:"))
        self.label.setProperty("setToolTip", _translate("frmScriptEditor", "Please enter the main directory of the fMRI dataset. Format of directory must be based on BIDS structure."))
        self.txtScript.setText(_translate("frmScriptEditor", "/sub-$SUB$/func/sub-$SUB$_task-$TASK$_run-$RUN$_script.fsf"))
        self.label_34.setText(_translate("frmScriptEditor", "Analysis Script:"))
        self.groupBox_2.setTitle(_translate("frmScriptEditor", "<Counter>"))
        self.label_6.setText(_translate("frmScriptEditor", "From:"))
        self.label_15.setText(_translate("frmScriptEditor", "To:"))
        self.txtConPer.setText(_translate("frmScriptEditor", "0"))
        self.label_11.setText(_translate("frmScriptEditor", "Perfix:"))
        self.label_12.setText(_translate("frmScriptEditor", "Length:"))
        self.groupBox_5.setTitle(_translate("frmScriptEditor", "<Value Structures>"))
        self.label_16.setText(_translate("frmScriptEditor", "Output Value:"))
        self.label_17.setText(_translate("frmScriptEditor", "Input Value:"))
        self.label_17.setProperty("setToolTip", _translate("frmScriptEditor", "Please enter the main directory of the fMRI dataset. Format of directory must be based on BIDS structure."))
        self.cbInDynamic.setText(_translate("frmScriptEditor", "Dynamic"))
        self.cbOutDynamic.setText(_translate("frmScriptEditor", "Dynamic"))
        self.label_23.setText(_translate("frmScriptEditor", "$SUB$, $TASK$, $RUN$, $COUNT$ will be replaced by the preprocessing parameters.\n"
"It\'s case sensitive."))
        self.btnExit.setText(_translate("frmScriptEditor", "Exit"))
        self.btnRun.setText(_translate("frmScriptEditor", "Run"))
        self.cbDEMO.setText(_translate("frmScriptEditor", "DEMO"))

