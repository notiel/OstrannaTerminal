# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Terminal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1055, 798)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Logo_new.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.LblAvailable = QtWidgets.QLabel(self.centralwidget)
        self.LblAvailable.setObjectName("LblAvailable")
        self.gridLayout.addWidget(self.LblAvailable, 4, 2, 1, 1, QtCore.Qt.AlignRight)
        self.TxtBuffer = QtWidgets.QTextBrowser(self.centralwidget)
        self.TxtBuffer.setObjectName("TxtBuffer")
        self.gridLayout.addWidget(self.TxtBuffer, 9, 0, 1, 12)
        self.GBTansmit = QtWidgets.QGroupBox(self.centralwidget)
        self.GBTansmit.setObjectName("GBTansmit")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.GBTansmit)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.TxtTransmit2 = QtWidgets.QLineEdit(self.GBTansmit)
        self.TxtTransmit2.setObjectName("TxtTransmit2")
        self.gridLayout_8.addWidget(self.TxtTransmit2, 0, 0, 1, 1)
        self.BtnSend2 = QtWidgets.QPushButton(self.GBTansmit)
        self.BtnSend2.setEnabled(False)
        self.BtnSend2.setObjectName("BtnSend2")
        self.gridLayout_8.addWidget(self.BtnSend2, 0, 1, 1, 1)
        self.TxtTransmit = QtWidgets.QLineEdit(self.GBTansmit)
        self.TxtTransmit.setObjectName("TxtTransmit")
        self.gridLayout_8.addWidget(self.TxtTransmit, 1, 0, 1, 1)
        self.BtnSend = QtWidgets.QPushButton(self.GBTansmit)
        self.BtnSend.setEnabled(False)
        self.BtnSend.setObjectName("BtnSend")
        self.gridLayout_8.addWidget(self.BtnSend, 1, 1, 1, 1)
        self.CBClear2 = QtWidgets.QCheckBox(self.GBTansmit)
        self.CBClear2.setObjectName("CBClear2")
        self.gridLayout_8.addWidget(self.CBClear2, 0, 2, 1, 1)
        self.CBClear = QtWidgets.QCheckBox(self.GBTansmit)
        self.CBClear.setChecked(False)
        self.CBClear.setObjectName("CBClear")
        self.gridLayout_8.addWidget(self.CBClear, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.GBTansmit, 27, 0, 2, 10)
        self.GBTransmit = QtWidgets.QGroupBox(self.centralwidget)
        self.GBTransmit.setObjectName("GBTransmit")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.GBTransmit)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.BtnSendFile = QtWidgets.QPushButton(self.GBTransmit)
        self.BtnSendFile.setEnabled(False)
        self.BtnSendFile.setObjectName("BtnSendFile")
        self.gridLayout_7.addWidget(self.BtnSendFile, 0, 1, 1, 1)
        self.BtnFile = QtWidgets.QPushButton(self.GBTransmit)
        self.BtnFile.setObjectName("BtnFile")
        self.gridLayout_7.addWidget(self.BtnFile, 0, 0, 1, 1)
        self.LblFile = QtWidgets.QLabel(self.GBTransmit)
        self.LblFile.setObjectName("LblFile")
        self.gridLayout_7.addWidget(self.LblFile, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.GBTransmit, 27, 10, 2, 4)
        self.GBMacros = QtWidgets.QGroupBox(self.centralwidget)
        self.GBMacros.setObjectName("GBMacros")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.GBMacros)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.LblMacrosSelected = QtWidgets.QLabel(self.GBMacros)
        self.LblMacrosSelected.setObjectName("LblMacrosSelected")
        self.gridLayout_6.addWidget(self.LblMacrosSelected, 12, 0, 1, 2)
        self.BtnMacros11 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros11.setEnabled(False)
        self.BtnMacros11.setObjectName("BtnMacros11")
        self.gridLayout_6.addWidget(self.BtnMacros11, 0, 1, 1, 1)
        self.BtnMacros12 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros12.setEnabled(False)
        self.BtnMacros12.setObjectName("BtnMacros12")
        self.gridLayout_6.addWidget(self.BtnMacros12, 1, 1, 1, 1)
        self.BtnMacros14 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros14.setEnabled(False)
        self.BtnMacros14.setObjectName("BtnMacros14")
        self.gridLayout_6.addWidget(self.BtnMacros14, 3, 1, 1, 1)
        self.BtnMacros2 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros2.setEnabled(False)
        self.BtnMacros2.setObjectName("BtnMacros2")
        self.gridLayout_6.addWidget(self.BtnMacros2, 1, 0, 1, 1)
        self.BtnMacros5 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros5.setEnabled(False)
        self.BtnMacros5.setObjectName("BtnMacros5")
        self.gridLayout_6.addWidget(self.BtnMacros5, 4, 0, 1, 1)
        self.BtnMacros15 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros15.setEnabled(False)
        self.BtnMacros15.setObjectName("BtnMacros15")
        self.gridLayout_6.addWidget(self.BtnMacros15, 4, 1, 1, 1)
        self.BtnMacros17 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros17.setEnabled(False)
        self.BtnMacros17.setObjectName("BtnMacros17")
        self.gridLayout_6.addWidget(self.BtnMacros17, 6, 1, 1, 1)
        self.BtnMacros16 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros16.setEnabled(False)
        self.BtnMacros16.setObjectName("BtnMacros16")
        self.gridLayout_6.addWidget(self.BtnMacros16, 5, 1, 1, 1)
        self.BtnMacros8 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros8.setEnabled(False)
        self.BtnMacros8.setObjectName("BtnMacros8")
        self.gridLayout_6.addWidget(self.BtnMacros8, 7, 0, 1, 1)
        self.BtnMacros9 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros9.setEnabled(False)
        self.BtnMacros9.setObjectName("BtnMacros9")
        self.gridLayout_6.addWidget(self.BtnMacros9, 8, 0, 1, 1)
        self.BtnMacros6 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros6.setEnabled(False)
        self.BtnMacros6.setObjectName("BtnMacros6")
        self.gridLayout_6.addWidget(self.BtnMacros6, 5, 0, 1, 1)
        self.BtnMacros7 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros7.setEnabled(False)
        self.BtnMacros7.setObjectName("BtnMacros7")
        self.gridLayout_6.addWidget(self.BtnMacros7, 6, 0, 1, 1)
        self.BtnMacros20 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros20.setEnabled(False)
        self.BtnMacros20.setObjectName("BtnMacros20")
        self.gridLayout_6.addWidget(self.BtnMacros20, 9, 1, 1, 1)
        self.CBMacros = QtWidgets.QComboBox(self.GBMacros)
        self.CBMacros.setObjectName("CBMacros")
        self.gridLayout_6.addWidget(self.CBMacros, 11, 0, 1, 2)
        self.BtnMacros18 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros18.setEnabled(False)
        self.BtnMacros18.setObjectName("BtnMacros18")
        self.gridLayout_6.addWidget(self.BtnMacros18, 7, 1, 1, 1)
        self.BtnMacros19 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros19.setEnabled(False)
        self.BtnMacros19.setObjectName("BtnMacros19")
        self.gridLayout_6.addWidget(self.BtnMacros19, 8, 1, 1, 1)
        self.BtnMacros10 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros10.setEnabled(False)
        self.BtnMacros10.setObjectName("BtnMacros10")
        self.gridLayout_6.addWidget(self.BtnMacros10, 9, 0, 1, 1)
        self.LblMacrosAvailable = QtWidgets.QLabel(self.GBMacros)
        self.LblMacrosAvailable.setObjectName("LblMacrosAvailable")
        self.gridLayout_6.addWidget(self.LblMacrosAvailable, 10, 0, 1, 2)
        self.BtnMacros1 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros1.setEnabled(False)
        self.BtnMacros1.setObjectName("BtnMacros1")
        self.gridLayout_6.addWidget(self.BtnMacros1, 0, 0, 1, 1)
        self.BtnMacros4 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros4.setEnabled(False)
        self.BtnMacros4.setObjectName("BtnMacros4")
        self.gridLayout_6.addWidget(self.BtnMacros4, 3, 0, 1, 1)
        self.BtnMacros3 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros3.setEnabled(False)
        self.BtnMacros3.setObjectName("BtnMacros3")
        self.gridLayout_6.addWidget(self.BtnMacros3, 2, 0, 1, 1)
        self.BtnMacros13 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros13.setEnabled(False)
        self.BtnMacros13.setObjectName("BtnMacros13")
        self.gridLayout_6.addWidget(self.BtnMacros13, 2, 1, 1, 1)
        self.BtnCreateMacros = QtWidgets.QPushButton(self.GBMacros)
        self.BtnCreateMacros.setObjectName("BtnCreateMacros")
        self.gridLayout_6.addWidget(self.BtnCreateMacros, 13, 0, 1, 2)
        self.gridLayout.addWidget(self.GBMacros, 9, 12, 3, 2)
        self.GBSettings = QtWidgets.QGroupBox(self.centralwidget)
        self.GBSettings.setObjectName("GBSettings")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.GBSettings)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.BtnSettings = QtWidgets.QPushButton(self.GBSettings)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Settings/icon/customize.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnSettings.setIcon(icon1)
        self.BtnSettings.setObjectName("BtnSettings")
        self.gridLayout_3.addWidget(self.BtnSettings, 0, 0, 1, 3)
        self.BtnAscii = QtWidgets.QPushButton(self.GBSettings)
        self.BtnAscii.setObjectName("BtnAscii")
        self.gridLayout_3.addWidget(self.BtnAscii, 0, 3, 1, 1)
        self.CBBaudrate = QtWidgets.QComboBox(self.GBSettings)
        self.CBBaudrate.setObjectName("CBBaudrate")
        self.CBBaudrate.addItem("")
        self.CBBaudrate.addItem("")
        self.CBBaudrate.addItem("")
        self.CBBaudrate.addItem("")
        self.gridLayout_3.addWidget(self.CBBaudrate, 2, 3, 1, 1)
        self.LblBaudrate = QtWidgets.QLabel(self.GBSettings)
        self.LblBaudrate.setObjectName("LblBaudrate")
        self.gridLayout_3.addWidget(self.LblBaudrate, 2, 0, 1, 3, QtCore.Qt.AlignRight)
        self.gridLayout.addWidget(self.GBSettings, 3, 12, 4, 2)
        self.BtnReScan = QtWidgets.QPushButton(self.centralwidget)
        self.BtnReScan.setObjectName("BtnReScan")
        self.gridLayout.addWidget(self.BtnReScan, 4, 1, 1, 1)
        self.BtnConnect = QtWidgets.QPushButton(self.centralwidget)
        self.BtnConnect.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Connect/icon/connect.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnConnect.setIcon(icon2)
        self.BtnConnect.setObjectName("BtnConnect")
        self.gridLayout.addWidget(self.BtnConnect, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.BtnDisconnect = QtWidgets.QPushButton(self.centralwidget)
        self.BtnDisconnect.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Disconnect/icon/discon.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnDisconnect.setIcon(icon3)
        self.BtnDisconnect.setObjectName("BtnDisconnect")
        self.gridLayout.addWidget(self.BtnDisconnect, 5, 0, 1, 1)
        self.BtnClear = QtWidgets.QPushButton(self.centralwidget)
        self.BtnClear.setObjectName("BtnClear")
        self.gridLayout.addWidget(self.BtnClear, 6, 0, 1, 1)
        self.CBSTM = QtWidgets.QCheckBox(self.centralwidget)
        self.CBSTM.setChecked(True)
        self.CBSTM.setObjectName("CBSTM")
        self.gridLayout.addWidget(self.CBSTM, 5, 3, 1, 1)
        self.BtnSave = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSave.setObjectName("BtnSave")
        self.gridLayout.addWidget(self.BtnSave, 6, 11, 1, 1)
        self.CBPorts = QtWidgets.QComboBox(self.centralwidget)
        self.CBPorts.setMinimumSize(QtCore.QSize(300, 0))
        self.CBPorts.setObjectName("CBPorts")
        self.gridLayout.addWidget(self.CBPorts, 4, 3, 1, 9)
        self.GBCounter = QtWidgets.QGroupBox(self.centralwidget)
        self.GBCounter.setObjectName("GBCounter")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.GBCounter)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.LblCounter = QtWidgets.QLabel(self.GBCounter)
        self.LblCounter.setMaximumSize(QtCore.QSize(55, 16777215))
        self.LblCounter.setObjectName("LblCounter")
        self.gridLayout_4.addWidget(self.LblCounter, 0, 0, 1, 1)
        self.BtnCounter = QtWidgets.QPushButton(self.GBCounter)
        self.BtnCounter.setObjectName("BtnCounter")
        self.gridLayout_4.addWidget(self.BtnCounter, 0, 2, 1, 1)
        self.LblCounterData = QtWidgets.QLabel(self.GBCounter)
        self.LblCounterData.setObjectName("LblCounterData")
        self.gridLayout_4.addWidget(self.LblCounterData, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.GBCounter, 5, 1, 2, 2)
        self.CBHex = QtWidgets.QCheckBox(self.centralwidget)
        self.CBHex.setObjectName("CBHex")
        self.gridLayout.addWidget(self.CBHex, 6, 9, 1, 2)
        self.CBNRF = QtWidgets.QCheckBox(self.centralwidget)
        self.CBNRF.setObjectName("CBNRF")
        self.gridLayout.addWidget(self.CBNRF, 5, 4, 1, 3)
        self.LblStatusInfo = QtWidgets.QLabel(self.centralwidget)
        self.LblStatusInfo.setObjectName("LblStatusInfo")
        self.gridLayout.addWidget(self.LblStatusInfo, 5, 11, 1, 1)
        self.LblStatus = QtWidgets.QLabel(self.centralwidget)
        self.LblStatus.setObjectName("LblStatus")
        self.gridLayout.addWidget(self.LblStatus, 5, 10, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.CBPorts, self.BtnReScan)
        MainWindow.setTabOrder(self.BtnReScan, self.BtnConnect)
        MainWindow.setTabOrder(self.BtnConnect, self.BtnDisconnect)
        MainWindow.setTabOrder(self.BtnDisconnect, self.BtnClear)
        MainWindow.setTabOrder(self.BtnClear, self.BtnCounter)
        MainWindow.setTabOrder(self.BtnCounter, self.CBSTM)
        MainWindow.setTabOrder(self.CBSTM, self.CBHex)
        MainWindow.setTabOrder(self.CBHex, self.BtnSave)
        MainWindow.setTabOrder(self.BtnSave, self.TxtTransmit2)
        MainWindow.setTabOrder(self.TxtTransmit2, self.BtnSend2)
        MainWindow.setTabOrder(self.BtnSend2, self.CBClear2)
        MainWindow.setTabOrder(self.CBClear2, self.TxtTransmit)
        MainWindow.setTabOrder(self.TxtTransmit, self.BtnSend)
        MainWindow.setTabOrder(self.BtnSend, self.CBClear)
        MainWindow.setTabOrder(self.CBClear, self.BtnFile)
        MainWindow.setTabOrder(self.BtnFile, self.BtnSendFile)
        MainWindow.setTabOrder(self.BtnSendFile, self.BtnMacros1)
        MainWindow.setTabOrder(self.BtnMacros1, self.BtnMacros11)
        MainWindow.setTabOrder(self.BtnMacros11, self.BtnMacros2)
        MainWindow.setTabOrder(self.BtnMacros2, self.BtnMacros12)
        MainWindow.setTabOrder(self.BtnMacros12, self.BtnMacros3)
        MainWindow.setTabOrder(self.BtnMacros3, self.BtnMacros13)
        MainWindow.setTabOrder(self.BtnMacros13, self.BtnMacros4)
        MainWindow.setTabOrder(self.BtnMacros4, self.BtnMacros14)
        MainWindow.setTabOrder(self.BtnMacros14, self.BtnMacros5)
        MainWindow.setTabOrder(self.BtnMacros5, self.BtnMacros15)
        MainWindow.setTabOrder(self.BtnMacros15, self.BtnMacros6)
        MainWindow.setTabOrder(self.BtnMacros6, self.BtnMacros16)
        MainWindow.setTabOrder(self.BtnMacros16, self.BtnMacros7)
        MainWindow.setTabOrder(self.BtnMacros7, self.BtnMacros17)
        MainWindow.setTabOrder(self.BtnMacros17, self.BtnMacros8)
        MainWindow.setTabOrder(self.BtnMacros8, self.BtnMacros18)
        MainWindow.setTabOrder(self.BtnMacros18, self.BtnMacros9)
        MainWindow.setTabOrder(self.BtnMacros9, self.BtnMacros19)
        MainWindow.setTabOrder(self.BtnMacros19, self.BtnMacros10)
        MainWindow.setTabOrder(self.BtnMacros10, self.BtnMacros20)
        MainWindow.setTabOrder(self.BtnMacros20, self.CBMacros)
        MainWindow.setTabOrder(self.CBMacros, self.BtnCreateMacros)
        MainWindow.setTabOrder(self.BtnCreateMacros, self.BtnSettings)
        MainWindow.setTabOrder(self.BtnSettings, self.BtnAscii)
        MainWindow.setTabOrder(self.BtnAscii, self.CBBaudrate)
        MainWindow.setTabOrder(self.CBBaudrate, self.TxtBuffer)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OstrannaTerminal"))
        self.LblAvailable.setText(_translate("MainWindow", "COMs:"))
        self.TxtBuffer.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.GBTansmit.setTitle(_translate("MainWindow", "Transmit Command"))
        self.BtnSend2.setText(_translate("MainWindow", "Send Input&1"))
        self.BtnSend.setText(_translate("MainWindow", "Send Input&2"))
        self.CBClear2.setText(_translate("MainWindow", "Clear &after sending"))
        self.CBClear.setText(_translate("MainWindow", "Clear aft&er sending"))
        self.GBTransmit.setTitle(_translate("MainWindow", "Transmit File"))
        self.BtnSendFile.setText(_translate("MainWindow", "Send F&ile"))
        self.BtnFile.setText(_translate("MainWindow", "Select &File"))
        self.LblFile.setText(_translate("MainWindow", "File Selected: None"))
        self.GBMacros.setTitle(_translate("MainWindow", "Macros "))
        self.LblMacrosSelected.setText(_translate("MainWindow", "Macros set selected: None"))
        self.BtnMacros11.setText(_translate("MainWindow", "M11"))
        self.BtnMacros12.setText(_translate("MainWindow", "M12"))
        self.BtnMacros14.setText(_translate("MainWindow", "M14"))
        self.BtnMacros2.setText(_translate("MainWindow", "M2"))
        self.BtnMacros5.setText(_translate("MainWindow", "M5"))
        self.BtnMacros15.setText(_translate("MainWindow", "M15"))
        self.BtnMacros17.setText(_translate("MainWindow", "M17"))
        self.BtnMacros16.setText(_translate("MainWindow", "M16"))
        self.BtnMacros8.setText(_translate("MainWindow", "M8"))
        self.BtnMacros9.setText(_translate("MainWindow", "M9"))
        self.BtnMacros6.setText(_translate("MainWindow", "M6"))
        self.BtnMacros7.setText(_translate("MainWindow", "M7"))
        self.BtnMacros20.setText(_translate("MainWindow", "M20"))
        self.BtnMacros18.setText(_translate("MainWindow", "M18"))
        self.BtnMacros19.setText(_translate("MainWindow", "M19"))
        self.BtnMacros10.setText(_translate("MainWindow", "M10"))
        self.LblMacrosAvailable.setText(_translate("MainWindow", "Macros sets available"))
        self.BtnMacros1.setText(_translate("MainWindow", "M1"))
        self.BtnMacros4.setText(_translate("MainWindow", "M4"))
        self.BtnMacros3.setText(_translate("MainWindow", "M3"))
        self.BtnMacros13.setText(_translate("MainWindow", "M13"))
        self.BtnCreateMacros.setText(_translate("MainWindow", "C&reate/Edit Macros Set"))
        self.GBSettings.setTitle(_translate("MainWindow", "Settings "))
        self.BtnSettings.setText(_translate("MainWindow", "&Settings"))
        self.BtnAscii.setText(_translate("MainWindow", "ASCII"))
        self.CBBaudrate.setItemText(0, _translate("MainWindow", "9600"))
        self.CBBaudrate.setItemText(1, _translate("MainWindow", "115200"))
        self.CBBaudrate.setItemText(2, _translate("MainWindow", "256000"))
        self.CBBaudrate.setItemText(3, _translate("MainWindow", "Custom"))
        self.LblBaudrate.setText(_translate("MainWindow", "Baudrate:"))
        self.BtnReScan.setText(_translate("MainWindow", "&ReScan"))
        self.BtnConnect.setText(_translate("MainWindow", "&Connect"))
        self.BtnDisconnect.setText(_translate("MainWindow", "&Disconnect"))
        self.BtnClear.setText(_translate("MainWindow", "Clear"))
        self.CBSTM.setText(_translate("MainWindow", "Filter ST&M devices"))
        self.BtnSave.setText(_translate("MainWindow", "Save to &log"))
        self.GBCounter.setTitle(_translate("MainWindow", "Counter"))
        self.LblCounter.setText(_translate("MainWindow", "Counter:"))
        self.BtnCounter.setText(_translate("MainWindow", "Clear Counter"))
        self.LblCounterData.setText(_translate("MainWindow", "0"))
        self.CBHex.setText(_translate("MainWindow", "Hex Mode"))
        self.CBNRF.setText(_translate("MainWindow", "Filter &NRF devices"))
        self.LblStatusInfo.setText(_translate("MainWindow", "Not Connected"))
        self.LblStatus.setText(_translate("MainWindow", "Status:"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))

import logo_rc
