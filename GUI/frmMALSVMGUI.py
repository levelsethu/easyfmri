# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMALSVMGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMALSVM(object):
    def setupUi(self, frmMALSVM):
        frmMALSVM.setObjectName("frmMALSVM")
        frmMALSVM.resize(782, 764)
        self.btnInFile = QtWidgets.QPushButton(frmMALSVM)
        self.btnInFile.setGeometry(QtCore.QRect(710, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmMALSVM)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 211, 16))
        self.label_33.setObjectName("label_33")
        self.btnOutFile = QtWidgets.QPushButton(frmMALSVM)
        self.btnOutFile.setGeometry(QtCore.QRect(710, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtInFile = QtWidgets.QLineEdit(frmMALSVM)
        self.txtInFile.setGeometry(QtCore.QRect(210, 20, 491, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmMALSVM)
        self.btnConvert.setGeometry(QtCore.QRect(620, 715, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmMALSVM)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 181, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmMALSVM)
        self.txtOutFile.setGeometry(QtCore.QRect(210, 60, 491, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnClose = QtWidgets.QPushButton(frmMALSVM)
        self.btnClose.setGeometry(QtCore.QRect(30, 715, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmMALSVM)
        self.tabWidget.setGeometry(QtCore.QRect(30, 150, 731, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(360, 10, 61, 16))
        self.label.setObjectName("label")
        self.txtITrLabel = QtWidgets.QComboBox(self.tab)
        self.txtITrLabel.setGeometry(QtCore.QRect(240, 110, 121, 26))
        self.txtITrLabel.setEditable(True)
        self.txtITrLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITrLabel.setObjectName("txtITrLabel")
        self.txtITrData = QtWidgets.QComboBox(self.tab)
        self.txtITrData.setGeometry(QtCore.QRect(240, 70, 121, 26))
        self.txtITrData.setEditable(True)
        self.txtITrData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITrData.setObjectName("txtITrData")
        self.txtITeLabel = QtWidgets.QComboBox(self.tab)
        self.txtITeLabel.setGeometry(QtCore.QRect(390, 110, 121, 26))
        self.txtITeLabel.setEditable(True)
        self.txtITeLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITeLabel.setObjectName("txtITeLabel")
        self.txtITeData = QtWidgets.QComboBox(self.tab)
        self.txtITeData.setGeometry(QtCore.QRect(390, 70, 121, 26))
        self.txtITeData.setEditable(True)
        self.txtITeData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITeData.setObjectName("txtITeData")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(285, 40, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(430, 40, 81, 16))
        self.label_8.setObjectName("label_8")
        self.txtFoldID = QtWidgets.QComboBox(self.tab)
        self.txtFoldID.setGeometry(QtCore.QRect(240, 150, 121, 26))
        self.txtFoldID.setEditable(True)
        self.txtFoldID.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtFoldID.setObjectName("txtFoldID")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 150, 121, 16))
        self.label_9.setObjectName("label_9")
        self.lbFoldID = QtWidgets.QLabel(self.tab)
        self.lbFoldID.setGeometry(QtCore.QRect(390, 150, 251, 16))
        self.lbFoldID.setObjectName("lbFoldID")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 671, 80))
        self.groupBox.setObjectName("groupBox")
        self.cbScale = QtWidgets.QCheckBox(self.groupBox)
        self.cbScale.setGeometry(QtCore.QRect(20, 40, 641, 21))
        self.cbScale.setChecked(True)
        self.cbScale.setObjectName("cbScale")
        self.txtMaxIter = QtWidgets.QLineEdit(self.tab_2)
        self.txtMaxIter.setGeometry(QtCore.QRect(260, 320, 160, 21))
        self.txtMaxIter.setObjectName("txtMaxIter")
        self.txtTole = QtWidgets.QLineEdit(self.tab_2)
        self.txtTole.setGeometry(QtCore.QRect(260, 280, 160, 21))
        self.txtTole.setObjectName("txtTole")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(30, 280, 221, 16))
        self.label_14.setObjectName("label_14")
        self.cbPenalty = QtWidgets.QComboBox(self.tab_2)
        self.cbPenalty.setGeometry(QtCore.QRect(260, 160, 161, 26))
        self.cbPenalty.setObjectName("cbPenalty")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(30, 160, 231, 16))
        self.label_13.setObjectName("label_13")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(30, 320, 251, 16))
        self.label_16.setObjectName("label_16")
        self.lblFeaNum_5 = QtWidgets.QLabel(self.tab_2)
        self.lblFeaNum_5.setGeometry(QtCore.QRect(440, 280, 281, 16))
        self.lblFeaNum_5.setObjectName("lblFeaNum_5")
        self.cbMode = QtWidgets.QComboBox(self.tab_2)
        self.cbMode.setGeometry(QtCore.QRect(260, 120, 161, 26))
        self.cbMode.setObjectName("cbMode")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(30, 120, 231, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(30, 240, 221, 16))
        self.label_20.setObjectName("label_20")
        self.txtC = QtWidgets.QLineEdit(self.tab_2)
        self.txtC.setGeometry(QtCore.QRect(260, 240, 160, 21))
        self.txtC.setObjectName("txtC")
        self.cbDual = QtWidgets.QCheckBox(self.tab_2)
        self.cbDual.setGeometry(QtCore.QRect(30, 360, 641, 20))
        self.cbDual.setChecked(True)
        self.cbDual.setObjectName("cbDual")
        self.cbIntercept = QtWidgets.QCheckBox(self.tab_2)
        self.cbIntercept.setGeometry(QtCore.QRect(30, 400, 661, 20))
        self.cbIntercept.setChecked(True)
        self.cbIntercept.setObjectName("cbIntercept")
        self.lblFeaNum_6 = QtWidgets.QLabel(self.tab_2)
        self.lblFeaNum_6.setGeometry(QtCore.QRect(440, 240, 281, 16))
        self.lblFeaNum_6.setObjectName("lblFeaNum_6")
        self.cbLoss = QtWidgets.QComboBox(self.tab_2)
        self.cbLoss.setGeometry(QtCore.QRect(260, 200, 161, 26))
        self.cbLoss.setObjectName("cbLoss")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(30, 200, 231, 16))
        self.label_21.setObjectName("label_21")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.txtFoldFrom = QtWidgets.QSpinBox(self.tab_3)
        self.txtFoldFrom.setGeometry(QtCore.QRect(100, 30, 80, 24))
        self.txtFoldFrom.setMaximum(100000)
        self.txtFoldFrom.setProperty("value", 1)
        self.txtFoldFrom.setObjectName("txtFoldFrom")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(40, 30, 60, 16))
        self.label_17.setObjectName("label_17")
        self.txtFoldTo = QtWidgets.QSpinBox(self.tab_3)
        self.txtFoldTo.setGeometry(QtCore.QRect(270, 30, 80, 24))
        self.txtFoldTo.setMaximum(100000)
        self.txtFoldTo.setProperty("value", 1)
        self.txtFoldTo.setObjectName("txtFoldTo")
        self.label_44 = QtWidgets.QLabel(self.tab_3)
        self.label_44.setGeometry(QtCore.QRect(210, 30, 60, 16))
        self.label_44.setObjectName("label_44")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 201, 16))
        self.label_4.setObjectName("label_4")
        self.txtFilter = QtWidgets.QLineEdit(self.tab_4)
        self.txtFilter.setGeometry(QtCore.QRect(190, 30, 291, 21))
        self.txtFilter.setObjectName("txtFilter")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(490, 30, 211, 16))
        self.label_5.setObjectName("label_5")
        self.txtClass = QtWidgets.QTextEdit(self.tab_4)
        self.txtClass.setGeometry(QtCore.QRect(190, 70, 91, 431))
        self.txtClass.setReadOnly(True)
        self.txtClass.setObjectName("txtClass")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 201, 16))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.cbAverage = QtWidgets.QCheckBox(self.tab_5)
        self.cbAverage.setGeometry(QtCore.QRect(20, 30, 181, 20))
        self.cbAverage.setChecked(True)
        self.cbAverage.setObjectName("cbAverage")
        self.cbPrecision = QtWidgets.QCheckBox(self.tab_5)
        self.cbPrecision.setGeometry(QtCore.QRect(20, 70, 181, 20))
        self.cbPrecision.setChecked(True)
        self.cbPrecision.setObjectName("cbPrecision")
        self.cbPrecisionAvg = QtWidgets.QComboBox(self.tab_5)
        self.cbPrecisionAvg.setGeometry(QtCore.QRect(240, 70, 321, 26))
        self.cbPrecisionAvg.setObjectName("cbPrecisionAvg")
        self.cbAPrecisionAvg = QtWidgets.QComboBox(self.tab_5)
        self.cbAPrecisionAvg.setGeometry(QtCore.QRect(240, 110, 321, 26))
        self.cbAPrecisionAvg.setObjectName("cbAPrecisionAvg")
        self.cbAPrecision = QtWidgets.QCheckBox(self.tab_5)
        self.cbAPrecision.setGeometry(QtCore.QRect(20, 110, 231, 20))
        self.cbAPrecision.setChecked(False)
        self.cbAPrecision.setObjectName("cbAPrecision")
        self.cbRecallAvg = QtWidgets.QComboBox(self.tab_5)
        self.cbRecallAvg.setGeometry(QtCore.QRect(240, 150, 321, 26))
        self.cbRecallAvg.setObjectName("cbRecallAvg")
        self.cbRecall = QtWidgets.QCheckBox(self.tab_5)
        self.cbRecall.setGeometry(QtCore.QRect(20, 150, 181, 20))
        self.cbRecall.setChecked(True)
        self.cbRecall.setObjectName("cbRecall")
        self.cbF1 = QtWidgets.QCheckBox(self.tab_5)
        self.cbF1.setGeometry(QtCore.QRect(20, 190, 181, 20))
        self.cbF1.setChecked(True)
        self.cbF1.setObjectName("cbF1")
        self.cbF1Avg = QtWidgets.QComboBox(self.tab_5)
        self.cbF1Avg.setGeometry(QtCore.QRect(240, 190, 321, 26))
        self.cbF1Avg.setObjectName("cbF1Avg")
        self.tabWidget.addTab(self.tab_5, "")
        self.label_12 = QtWidgets.QLabel(frmMALSVM)
        self.label_12.setGeometry(QtCore.QRect(185, 720, 421, 20))
        self.label_12.setObjectName("label_12")
        self.btnOutModel = QtWidgets.QPushButton(frmMALSVM)
        self.btnOutModel.setGeometry(QtCore.QRect(710, 100, 51, 32))
        self.btnOutModel.setObjectName("btnOutModel")
        self.label_36 = QtWidgets.QLabel(frmMALSVM)
        self.label_36.setGeometry(QtCore.QRect(30, 100, 231, 16))
        self.label_36.setObjectName("label_36")
        self.txtOutModel = QtWidgets.QLineEdit(frmMALSVM)
        self.txtOutModel.setGeometry(QtCore.QRect(210, 100, 491, 21))
        self.txtOutModel.setText("")
        self.txtOutModel.setObjectName("txtOutModel")

        self.retranslateUi(frmMALSVM)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmMALSVM)
        frmMALSVM.setTabOrder(self.txtInFile, self.btnInFile)
        frmMALSVM.setTabOrder(self.btnInFile, self.txtOutFile)
        frmMALSVM.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmMALSVM.setTabOrder(self.btnOutFile, self.tabWidget)
        frmMALSVM.setTabOrder(self.tabWidget, self.txtITrData)
        frmMALSVM.setTabOrder(self.txtITrData, self.txtITrLabel)
        frmMALSVM.setTabOrder(self.txtITrLabel, self.btnConvert)
        frmMALSVM.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmMALSVM):
        _translate = QtCore.QCoreApplication.translate
        frmMALSVM.setWindowTitle(_translate("frmMALSVM", "Linear Support Vector Classification"))
        self.btnInFile.setText(_translate("frmMALSVM", "..."))
        self.label_33.setText(_translate("frmMALSVM", "Input Data (per fold)"))
        self.btnOutFile.setText(_translate("frmMALSVM", "..."))
        self.btnConvert.setText(_translate("frmMALSVM", "Analyze"))
        self.label_35.setText(_translate("frmMALSVM", "Analysis Results"))
        self.btnClose.setText(_translate("frmMALSVM", "Close"))
        self.label_2.setText(_translate("frmMALSVM", "Data"))
        self.label_3.setText(_translate("frmMALSVM", "Label"))
        self.label.setText(_translate("frmMALSVM", "Input"))
        self.label_7.setText(_translate("frmMALSVM", "Train"))
        self.label_8.setText(_translate("frmMALSVM", "Test"))
        self.label_9.setText(_translate("frmMALSVM", "FoldID"))
        self.lbFoldID.setText(_translate("frmMALSVM", "ID=None"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmMALSVM", "Data"))
        self.groupBox.setTitle(_translate("frmMALSVM", "<Input Data Normalization>"))
        self.cbScale.setText(_translate("frmMALSVM", "Scale Data Train~N(0,1) and Test~N(0,1)"))
        self.txtMaxIter.setText(_translate("frmMALSVM", "1000"))
        self.txtTole.setText(_translate("frmMALSVM", "0.0001"))
        self.label_14.setText(_translate("frmMALSVM", "Tolerance"))
        self.label_13.setText(_translate("frmMALSVM", "Penalty"))
        self.label_16.setText(_translate("frmMALSVM", "Maximum Iterations"))
        self.lblFeaNum_5.setText(_translate("frmMALSVM", "Tolerance for stopping criterion"))
        self.label_19.setText(_translate("frmMALSVM", "Mode"))
        self.label_20.setText(_translate("frmMALSVM", "C"))
        self.txtC.setText(_translate("frmMALSVM", "1"))
        self.cbDual.setText(_translate("frmMALSVM", "Dual optimization problem"))
        self.cbIntercept.setText(_translate("frmMALSVM", " Intercept for this model"))
        self.lblFeaNum_6.setText(_translate("frmMALSVM", "Penalty parameter "))
        self.label_21.setText(_translate("frmMALSVM", "Loss"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmMALSVM", "Parameters"))
        self.label_17.setText(_translate("frmMALSVM", "From:"))
        self.label_44.setText(_translate("frmMALSVM", "To:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmMALSVM", "Fold"))
        self.label_4.setText(_translate("frmMALSVM", "Remove Class IDs"))
        self.txtFilter.setText(_translate("frmMALSVM", "0"))
        self.label_5.setText(_translate("frmMALSVM", "e.g. 0 or [1,2]"))
        self.label_10.setText(_translate("frmMALSVM", "Existed Classes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmMALSVM", "Filter Class ID"))
        self.cbAverage.setText(_translate("frmMALSVM", "Average"))
        self.cbPrecision.setText(_translate("frmMALSVM", "Precision"))
        self.cbAPrecision.setText(_translate("frmMALSVM", "Average of Precision"))
        self.cbRecall.setText(_translate("frmMALSVM", "Recall"))
        self.cbF1.setText(_translate("frmMALSVM", "f1 score"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("frmMALSVM", "Metrics"))
        self.label_12.setText(_translate("frmMALSVM", "$FOLD$ will be replaced by fold number."))
        self.btnOutModel.setText(_translate("frmMALSVM", "..."))
        self.label_36.setText(_translate("frmMALSVM", "Models (per fold/opt)"))
