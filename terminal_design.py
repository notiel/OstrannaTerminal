# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Terminal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1207, 1217)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico_curved/Q_curved_white_background.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.GBMacros = QtWidgets.QGroupBox(self.centralwidget)
        self.GBMacros.setObjectName("GBMacros")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.GBMacros)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.BtnMacros11 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros11.setEnabled(False)
        self.BtnMacros11.setObjectName("BtnMacros11")
        self.gridLayout_6.addWidget(self.BtnMacros11, 12, 0, 1, 1)
        self.BtnMacros1 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros1.setEnabled(False)
        self.BtnMacros1.setObjectName("BtnMacros1")
        self.gridLayout_6.addWidget(self.BtnMacros1, 2, 0, 1, 1)
        self.BtnMacros8 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros8.setEnabled(False)
        self.BtnMacros8.setObjectName("BtnMacros8")
        self.gridLayout_6.addWidget(self.BtnMacros8, 9, 0, 1, 1)
        self.BtnMacros16 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros16.setEnabled(False)
        self.BtnMacros16.setObjectName("BtnMacros16")
        self.gridLayout_6.addWidget(self.BtnMacros16, 2, 1, 1, 1)
        self.BtnMacros29 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros29.setEnabled(False)
        self.BtnMacros29.setObjectName("BtnMacros29")
        self.gridLayout_6.addWidget(self.BtnMacros29, 15, 1, 1, 1)
        self.BtnMacros22 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros22.setEnabled(False)
        self.BtnMacros22.setObjectName("BtnMacros22")
        self.gridLayout_6.addWidget(self.BtnMacros22, 8, 1, 1, 1)
        self.BtnMacros7 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros7.setEnabled(False)
        self.BtnMacros7.setObjectName("BtnMacros7")
        self.gridLayout_6.addWidget(self.BtnMacros7, 8, 0, 1, 1)
        self.BtnMacros21 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros21.setEnabled(False)
        self.BtnMacros21.setObjectName("BtnMacros21")
        self.gridLayout_6.addWidget(self.BtnMacros21, 7, 1, 1, 1)
        self.BtnMacros30 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros30.setEnabled(False)
        self.BtnMacros30.setObjectName("BtnMacros30")
        self.gridLayout_6.addWidget(self.BtnMacros30, 16, 1, 1, 1)
        self.BtnMacros6 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros6.setEnabled(False)
        self.BtnMacros6.setObjectName("BtnMacros6")
        self.gridLayout_6.addWidget(self.BtnMacros6, 7, 0, 1, 1)
        self.BtnCreateMacros = QtWidgets.QPushButton(self.GBMacros)
        self.BtnCreateMacros.setObjectName("BtnCreateMacros")
        self.gridLayout_6.addWidget(self.BtnCreateMacros, 20, 0, 1, 2)
        self.BtnMacros2 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros2.setEnabled(False)
        self.BtnMacros2.setObjectName("BtnMacros2")
        self.gridLayout_6.addWidget(self.BtnMacros2, 3, 0, 1, 1)
        self.LblEmpty2 = QtWidgets.QLabel(self.GBMacros)
        self.LblEmpty2.setText("")
        self.LblEmpty2.setObjectName("LblEmpty2")
        self.gridLayout_6.addWidget(self.LblEmpty2, 17, 0, 1, 1)
        self.BtnMacros26 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros26.setEnabled(False)
        self.BtnMacros26.setObjectName("BtnMacros26")
        self.gridLayout_6.addWidget(self.BtnMacros26, 12, 1, 1, 1)
        self.BtnMacros17 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros17.setEnabled(False)
        self.BtnMacros17.setObjectName("BtnMacros17")
        self.gridLayout_6.addWidget(self.BtnMacros17, 3, 1, 1, 1)
        self.BtnMacros12 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros12.setEnabled(False)
        self.BtnMacros12.setObjectName("BtnMacros12")
        self.gridLayout_6.addWidget(self.BtnMacros12, 13, 0, 1, 1)
        self.BtnMacros10 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros10.setEnabled(False)
        self.BtnMacros10.setObjectName("BtnMacros10")
        self.gridLayout_6.addWidget(self.BtnMacros10, 11, 0, 1, 1)
        self.BtnMacros20 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros20.setEnabled(False)
        self.BtnMacros20.setObjectName("BtnMacros20")
        self.gridLayout_6.addWidget(self.BtnMacros20, 6, 1, 1, 1)
        self.BtnMacros24 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros24.setEnabled(False)
        self.BtnMacros24.setObjectName("BtnMacros24")
        self.gridLayout_6.addWidget(self.BtnMacros24, 10, 1, 1, 1)
        self.BtnMacros25 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros25.setEnabled(False)
        self.BtnMacros25.setObjectName("BtnMacros25")
        self.gridLayout_6.addWidget(self.BtnMacros25, 11, 1, 1, 1)
        self.LblMacrosAvailable = QtWidgets.QLabel(self.GBMacros)
        self.LblMacrosAvailable.setObjectName("LblMacrosAvailable")
        self.gridLayout_6.addWidget(self.LblMacrosAvailable, 0, 0, 1, 2)
        self.BtnMacros15 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros15.setEnabled(False)
        self.BtnMacros15.setObjectName("BtnMacros15")
        self.gridLayout_6.addWidget(self.BtnMacros15, 16, 0, 1, 1)
        self.BtnMacros3 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros3.setEnabled(False)
        self.BtnMacros3.setObjectName("BtnMacros3")
        self.gridLayout_6.addWidget(self.BtnMacros3, 4, 0, 1, 1)
        self.BtnMacros9 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros9.setEnabled(False)
        self.BtnMacros9.setObjectName("BtnMacros9")
        self.gridLayout_6.addWidget(self.BtnMacros9, 10, 0, 1, 1)
        self.BtnMacros19 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros19.setEnabled(False)
        self.BtnMacros19.setObjectName("BtnMacros19")
        self.gridLayout_6.addWidget(self.BtnMacros19, 5, 1, 1, 1)
        self.CBMacros = QtWidgets.QComboBox(self.GBMacros)
        self.CBMacros.setObjectName("CBMacros")
        self.gridLayout_6.addWidget(self.CBMacros, 1, 0, 1, 2)
        self.BtnMacros23 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros23.setEnabled(False)
        self.BtnMacros23.setObjectName("BtnMacros23")
        self.gridLayout_6.addWidget(self.BtnMacros23, 9, 1, 1, 1)
        self.BtnMacros18 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros18.setEnabled(False)
        self.BtnMacros18.setObjectName("BtnMacros18")
        self.gridLayout_6.addWidget(self.BtnMacros18, 4, 1, 1, 1)
        self.BtnMacros28 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros28.setEnabled(False)
        self.BtnMacros28.setObjectName("BtnMacros28")
        self.gridLayout_6.addWidget(self.BtnMacros28, 14, 1, 1, 1)
        self.BtnMacros5 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros5.setEnabled(False)
        self.BtnMacros5.setObjectName("BtnMacros5")
        self.gridLayout_6.addWidget(self.BtnMacros5, 6, 0, 1, 1)
        self.BtnMacros14 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros14.setEnabled(False)
        self.BtnMacros14.setObjectName("BtnMacros14")
        self.gridLayout_6.addWidget(self.BtnMacros14, 15, 0, 1, 1)
        self.BtnMacros27 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros27.setEnabled(False)
        self.BtnMacros27.setObjectName("BtnMacros27")
        self.gridLayout_6.addWidget(self.BtnMacros27, 13, 1, 1, 1)
        self.BtnMacros13 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros13.setEnabled(False)
        self.BtnMacros13.setObjectName("BtnMacros13")
        self.gridLayout_6.addWidget(self.BtnMacros13, 14, 0, 1, 1)
        self.BtnMacros4 = QtWidgets.QPushButton(self.GBMacros)
        self.BtnMacros4.setEnabled(False)
        self.BtnMacros4.setObjectName("BtnMacros4")
        self.gridLayout_6.addWidget(self.BtnMacros4, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.GBMacros, 9, 14, 3, 2)
        self.LblAvailable = QtWidgets.QLabel(self.centralwidget)
        self.LblAvailable.setObjectName("LblAvailable")
        self.gridLayout.addWidget(self.LblAvailable, 4, 2, 1, 1, QtCore.Qt.AlignRight)
        self.LblStatus = QtWidgets.QLabel(self.centralwidget)
        self.LblStatus.setText("")
        self.LblStatus.setPixmap(QtGui.QPixmap(":/status-disconn/icon/status discon2.gif"))
        self.LblStatus.setObjectName("LblStatus")
        self.gridLayout.addWidget(self.LblStatus, 4, 11, 1, 1)
        self.CBPorts = QtWidgets.QComboBox(self.centralwidget)
        self.CBPorts.setMinimumSize(QtCore.QSize(200, 0))
        self.CBPorts.setObjectName("CBPorts")
        self.gridLayout.addWidget(self.CBPorts, 4, 3, 1, 8)
        self.BtnConnect = QtWidgets.QPushButton(self.centralwidget)
        self.BtnConnect.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Connect/icon/conn.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnConnect.setIcon(icon1)
        self.BtnConnect.setObjectName("BtnConnect")
        self.gridLayout.addWidget(self.BtnConnect, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.BtnClear = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/clear/icon/clear.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnClear.setIcon(icon2)
        self.BtnClear.setObjectName("BtnClear")
        self.gridLayout.addWidget(self.BtnClear, 6, 0, 1, 1)
        self.BtnReScan = QtWidgets.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/rescan/icon/rescan.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnReScan.setIcon(icon3)
        self.BtnReScan.setObjectName("BtnReScan")
        self.gridLayout.addWidget(self.BtnReScan, 4, 1, 1, 1)
        self.BtnDisconnect = QtWidgets.QPushButton(self.centralwidget)
        self.BtnDisconnect.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Disconnect/icon/discon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnDisconnect.setIcon(icon4)
        self.BtnDisconnect.setObjectName("BtnDisconnect")
        self.gridLayout.addWidget(self.BtnDisconnect, 5, 0, 1, 1)
        self.GBSettings = QtWidgets.QGroupBox(self.centralwidget)
        self.GBSettings.setObjectName("GBSettings")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.GBSettings)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.BtnSettings = QtWidgets.QPushButton(self.GBSettings)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Settings/icon/customize.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnSettings.setIcon(icon5)
        self.BtnSettings.setObjectName("BtnSettings")
        self.gridLayout_3.addWidget(self.BtnSettings, 0, 0, 1, 3)
        self.BtnHelp = QtWidgets.QPushButton(self.GBSettings)
        self.BtnHelp.setEnabled(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Help/icon/info.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnHelp.setIcon(icon6)
        self.BtnHelp.setObjectName("BtnHelp")
        self.gridLayout_3.addWidget(self.BtnHelp, 1, 0, 1, 3)
        self.BtnAscii = QtWidgets.QPushButton(self.GBSettings)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/ascii/icon/i16x16.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnAscii.setIcon(icon7)
        self.BtnAscii.setObjectName("BtnAscii")
        self.gridLayout_3.addWidget(self.BtnAscii, 1, 3, 1, 1)
        self.BtnVar = QtWidgets.QPushButton(self.GBSettings)
        self.BtnVar.setEnabled(True)
        self.BtnVar.setObjectName("BtnVar")
        self.gridLayout_3.addWidget(self.BtnVar, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.GBSettings, 3, 14, 4, 2)
        self.LblName = QtWidgets.QLabel(self.centralwidget)
        self.LblName.setObjectName("LblName")
        self.gridLayout.addWidget(self.LblName, 5, 12, 1, 1)
        self.LineName = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineName.sizePolicy().hasHeightForWidth())
        self.LineName.setSizePolicy(sizePolicy)
        self.LineName.setMaximumSize(QtCore.QSize(100, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LineName.setFont(font)
        self.LineName.setObjectName("LineName")
        self.gridLayout.addWidget(self.LineName, 5, 13, 1, 1)
        self.BtnSave = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSave.setMaximumSize(QtCore.QSize(100, 16777215))
        self.BtnSave.setObjectName("BtnSave")
        self.gridLayout.addWidget(self.BtnSave, 6, 13, 1, 1)
        self.TxtBuffer = QtWidgets.QTextBrowser(self.centralwidget)
        self.TxtBuffer.setEnabled(True)
        self.TxtBuffer.setObjectName("TxtBuffer")
        self.gridLayout.addWidget(self.TxtBuffer, 9, 0, 1, 14)
        self.LblBaudrate = QtWidgets.QLabel(self.centralwidget)
        self.LblBaudrate.setObjectName("LblBaudrate")
        self.gridLayout.addWidget(self.LblBaudrate, 4, 12, 1, 1, QtCore.Qt.AlignRight)
        self.CBBaudrate = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CBBaudrate.sizePolicy().hasHeightForWidth())
        self.CBBaudrate.setSizePolicy(sizePolicy)
        self.CBBaudrate.setMaximumSize(QtCore.QSize(200, 16777215))
        self.CBBaudrate.setObjectName("CBBaudrate")
        self.CBBaudrate.addItem("")
        self.CBBaudrate.addItem("")
        self.CBBaudrate.addItem("")
        self.CBBaudrate.addItem("")
        self.gridLayout.addWidget(self.CBBaudrate, 4, 13, 1, 1)
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
        self.CBSTM = QtWidgets.QCheckBox(self.centralwidget)
        self.CBSTM.setChecked(True)
        self.CBSTM.setObjectName("CBSTM")
        self.gridLayout.addWidget(self.CBSTM, 5, 8, 1, 3, QtCore.Qt.AlignRight)
        self.CBNRF = QtWidgets.QCheckBox(self.centralwidget)
        self.CBNRF.setObjectName("CBNRF")
        self.gridLayout.addWidget(self.CBNRF, 6, 8, 1, 3, QtCore.Qt.AlignRight)
        self.GBTransmit = QtWidgets.QGroupBox(self.centralwidget)
        self.GBTransmit.setObjectName("GBTransmit")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.GBTransmit)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.LblLength = QtWidgets.QLabel(self.GBTransmit)
        self.LblLength.setObjectName("LblLength")
        self.gridLayout_7.addWidget(self.LblLength, 2, 0, 1, 1)
        self.LblCrc = QtWidgets.QLabel(self.GBTransmit)
        self.LblCrc.setObjectName("LblCrc")
        self.gridLayout_7.addWidget(self.LblCrc, 2, 1, 1, 1)
        self.BtnRefresh = QtWidgets.QPushButton(self.GBTransmit)
        self.BtnRefresh.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Refresh/icon/kisspng_computer_icons_icon_design_clip_art_database_icon_5ab2e5fb7763e8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnRefresh.setIcon(icon8)
        self.BtnRefresh.setObjectName("BtnRefresh")
        self.gridLayout_7.addWidget(self.BtnRefresh, 2, 2, 1, 1)
        self.BtnSendFile = QtWidgets.QPushButton(self.GBTransmit)
        self.BtnSendFile.setEnabled(False)
        self.BtnSendFile.setObjectName("BtnSendFile")
        self.gridLayout_7.addWidget(self.BtnSendFile, 0, 2, 1, 1)
        self.BtnFile = QtWidgets.QPushButton(self.GBTransmit)
        self.BtnFile.setObjectName("BtnFile")
        self.gridLayout_7.addWidget(self.BtnFile, 0, 1, 1, 1)
        self.LblFile = QtWidgets.QLabel(self.GBTransmit)
        self.LblFile.setObjectName("LblFile")
        self.gridLayout_7.addWidget(self.LblFile, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.GBTransmit, 27, 13, 2, 3)
        self.GBTansmit = QtWidgets.QGroupBox(self.centralwidget)
        self.GBTansmit.setObjectName("GBTansmit")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.GBTansmit)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.CBClear = QtWidgets.QCheckBox(self.GBTansmit)
        self.CBClear.setChecked(False)
        self.CBClear.setObjectName("CBClear")
        self.gridLayout_8.addWidget(self.CBClear, 0, 0, 1, 1)
        self.BtnSend = QtWidgets.QPushButton(self.GBTansmit)
        self.BtnSend.setEnabled(False)
        self.BtnSend.setMaximumSize(QtCore.QSize(50, 16777215))
        self.BtnSend.setObjectName("BtnSend")
        self.gridLayout_8.addWidget(self.BtnSend, 1, 7, 1, 1)
        self.BtnSend2 = QtWidgets.QPushButton(self.GBTansmit)
        self.BtnSend2.setEnabled(False)
        self.BtnSend2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.BtnSend2.setObjectName("BtnSend2")
        self.gridLayout_8.addWidget(self.BtnSend2, 2, 7, 1, 1)
        self.CBRepeat = QtWidgets.QCheckBox(self.GBTansmit)
        self.CBRepeat.setMaximumSize(QtCore.QSize(80, 16777215))
        self.CBRepeat.setObjectName("CBRepeat")
        self.gridLayout_8.addWidget(self.CBRepeat, 1, 4, 1, 1)
        self.SpinRepeat2 = QtWidgets.QSpinBox(self.GBTansmit)
        self.SpinRepeat2.setMaximumSize(QtCore.QSize(65, 16777215))
        self.SpinRepeat2.setMinimum(10)
        self.SpinRepeat2.setMaximum(10000)
        self.SpinRepeat2.setProperty("value", 1000)
        self.SpinRepeat2.setObjectName("SpinRepeat2")
        self.gridLayout_8.addWidget(self.SpinRepeat2, 2, 5, 1, 1)
        self.TxtTransmit = QtWidgets.QLineEdit(self.GBTansmit)
        self.TxtTransmit.setObjectName("TxtTransmit")
        self.gridLayout_8.addWidget(self.TxtTransmit, 1, 0, 1, 4)
        self.SpinRepeat = QtWidgets.QSpinBox(self.GBTansmit)
        self.SpinRepeat.setMaximumSize(QtCore.QSize(65, 16777215))
        self.SpinRepeat.setMinimum(10)
        self.SpinRepeat.setMaximum(10000)
        self.SpinRepeat.setProperty("value", 1000)
        self.SpinRepeat.setObjectName("SpinRepeat")
        self.gridLayout_8.addWidget(self.SpinRepeat, 1, 5, 1, 1)
        self.CBRepeat2 = QtWidgets.QCheckBox(self.GBTansmit)
        self.CBRepeat2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.CBRepeat2.setObjectName("CBRepeat2")
        self.gridLayout_8.addWidget(self.CBRepeat2, 2, 4, 1, 1)
        self.LblMs2 = QtWidgets.QLabel(self.GBTansmit)
        self.LblMs2.setMaximumSize(QtCore.QSize(25, 16777215))
        self.LblMs2.setObjectName("LblMs2")
        self.gridLayout_8.addWidget(self.LblMs2, 2, 6, 1, 1)
        self.LblMs1 = QtWidgets.QLabel(self.GBTansmit)
        self.LblMs1.setMaximumSize(QtCore.QSize(25, 16777215))
        self.LblMs1.setObjectName("LblMs1")
        self.gridLayout_8.addWidget(self.LblMs1, 1, 6, 1, 1)
        self.TxtTransmit2 = QtWidgets.QLineEdit(self.GBTansmit)
        self.TxtTransmit2.setObjectName("TxtTransmit2")
        self.gridLayout_8.addWidget(self.TxtTransmit2, 2, 0, 1, 4)
        self.gridLayout.addWidget(self.GBTansmit, 27, 0, 2, 13)
        self.CBHex = QtWidgets.QCheckBox(self.centralwidget)
        self.CBHex.setObjectName("CBHex")
        self.gridLayout.addWidget(self.CBHex, 6, 3, 1, 5)
        self.BtnGraph = QtWidgets.QPushButton(self.centralwidget)
        self.BtnGraph.setObjectName("BtnGraph")
        self.gridLayout.addWidget(self.BtnGraph, 6, 12, 1, 1)
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
        MainWindow.setTabOrder(self.BtnCounter, self.TxtTransmit)
        MainWindow.setTabOrder(self.TxtTransmit, self.BtnSend)
        MainWindow.setTabOrder(self.BtnSend, self.TxtTransmit2)
        MainWindow.setTabOrder(self.TxtTransmit2, self.BtnSend2)
        MainWindow.setTabOrder(self.BtnSend2, self.BtnMacros1)
        MainWindow.setTabOrder(self.BtnMacros1, self.BtnMacros2)
        MainWindow.setTabOrder(self.BtnMacros2, self.BtnMacros3)
        MainWindow.setTabOrder(self.BtnMacros3, self.BtnMacros4)
        MainWindow.setTabOrder(self.BtnMacros4, self.BtnMacros5)
        MainWindow.setTabOrder(self.BtnMacros5, self.BtnMacros6)
        MainWindow.setTabOrder(self.BtnMacros6, self.BtnMacros7)
        MainWindow.setTabOrder(self.BtnMacros7, self.BtnMacros8)
        MainWindow.setTabOrder(self.BtnMacros8, self.BtnMacros9)
        MainWindow.setTabOrder(self.BtnMacros9, self.BtnMacros10)
        MainWindow.setTabOrder(self.BtnMacros10, self.BtnCreateMacros)
        MainWindow.setTabOrder(self.BtnCreateMacros, self.BtnSettings)
        MainWindow.setTabOrder(self.BtnSettings, self.TxtBuffer)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quetima"))
        self.GBMacros.setTitle(_translate("MainWindow", "Macros "))
        self.BtnMacros11.setText(_translate("MainWindow", "M11"))
        self.BtnMacros1.setText(_translate("MainWindow", "M1"))
        self.BtnMacros8.setText(_translate("MainWindow", "M8"))
        self.BtnMacros16.setText(_translate("MainWindow", "M16"))
        self.BtnMacros29.setText(_translate("MainWindow", "M29"))
        self.BtnMacros22.setText(_translate("MainWindow", "M22"))
        self.BtnMacros7.setText(_translate("MainWindow", "M7"))
        self.BtnMacros21.setText(_translate("MainWindow", "M21"))
        self.BtnMacros30.setText(_translate("MainWindow", "M30"))
        self.BtnMacros6.setText(_translate("MainWindow", "M6"))
        self.BtnCreateMacros.setText(_translate("MainWindow", "Cre&ate/Edit Macros Set"))
        self.BtnMacros2.setText(_translate("MainWindow", "M2"))
        self.BtnMacros26.setText(_translate("MainWindow", "M26"))
        self.BtnMacros17.setText(_translate("MainWindow", "M17"))
        self.BtnMacros12.setText(_translate("MainWindow", "M12"))
        self.BtnMacros10.setText(_translate("MainWindow", "M10"))
        self.BtnMacros20.setText(_translate("MainWindow", "M20"))
        self.BtnMacros24.setText(_translate("MainWindow", "M24"))
        self.BtnMacros25.setText(_translate("MainWindow", "M25"))
        self.LblMacrosAvailable.setText(_translate("MainWindow", "Macros sets available"))
        self.BtnMacros15.setText(_translate("MainWindow", "M15"))
        self.BtnMacros3.setText(_translate("MainWindow", "M3"))
        self.BtnMacros9.setText(_translate("MainWindow", "M9"))
        self.BtnMacros19.setText(_translate("MainWindow", "M19"))
        self.BtnMacros23.setText(_translate("MainWindow", "M23"))
        self.BtnMacros18.setText(_translate("MainWindow", "M18"))
        self.BtnMacros28.setText(_translate("MainWindow", "M28"))
        self.BtnMacros5.setText(_translate("MainWindow", "M5"))
        self.BtnMacros14.setText(_translate("MainWindow", "M14"))
        self.BtnMacros27.setText(_translate("MainWindow", "M27"))
        self.BtnMacros13.setText(_translate("MainWindow", "M13"))
        self.BtnMacros4.setText(_translate("MainWindow", "M4"))
        self.LblAvailable.setText(_translate("MainWindow", "COMs:"))
        self.BtnConnect.setText(_translate("MainWindow", "&Connect"))
        self.BtnClear.setText(_translate("MainWindow", "Clear"))
        self.BtnReScan.setText(_translate("MainWindow", "&ReScan"))
        self.BtnDisconnect.setText(_translate("MainWindow", "&Disconnect"))
        self.GBSettings.setTitle(_translate("MainWindow", "Settings "))
        self.BtnSettings.setText(_translate("MainWindow", "&Settings"))
        self.BtnHelp.setText(_translate("MainWindow", "Help"))
        self.BtnAscii.setText(_translate("MainWindow", "ASCII"))
        self.BtnVar.setText(_translate("MainWindow", "&Variables"))
        self.LblName.setText(_translate("MainWindow", "Session Name:"))
        self.BtnSave.setText(_translate("MainWindow", "Save to &log"))
        self.TxtBuffer.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.LblBaudrate.setText(_translate("MainWindow", "Baudrate:"))
        self.CBBaudrate.setItemText(0, _translate("MainWindow", "9600"))
        self.CBBaudrate.setItemText(1, _translate("MainWindow", "115200"))
        self.CBBaudrate.setItemText(2, _translate("MainWindow", "256000"))
        self.CBBaudrate.setItemText(3, _translate("MainWindow", "Custom"))
        self.GBCounter.setTitle(_translate("MainWindow", "Counter"))
        self.LblCounter.setText(_translate("MainWindow", "Counter:"))
        self.BtnCounter.setText(_translate("MainWindow", "Clear Counter"))
        self.LblCounterData.setText(_translate("MainWindow", "0"))
        self.CBSTM.setText(_translate("MainWindow", "Filter ST&M devices"))
        self.CBNRF.setText(_translate("MainWindow", "Filter &NRF devices"))
        self.GBTransmit.setTitle(_translate("MainWindow", "Transmit File"))
        self.LblLength.setText(_translate("MainWindow", "Length: None"))
        self.LblCrc.setText(_translate("MainWindow", "CRC: None"))
        self.BtnRefresh.setText(_translate("MainWindow", "Refres&h"))
        self.BtnSendFile.setText(_translate("MainWindow", "Send F&ile"))
        self.BtnFile.setText(_translate("MainWindow", "Select &File"))
        self.LblFile.setText(_translate("MainWindow", "File: None"))
        self.GBTansmit.setTitle(_translate("MainWindow", "Transmit Command"))
        self.CBClear.setText(_translate("MainWindow", "Clear aft&er sending"))
        self.BtnSend.setText(_translate("MainWindow", "Send&1"))
        self.BtnSend2.setText(_translate("MainWindow", "Send&2"))
        self.CBRepeat.setText(_translate("MainWindow", "Repeat "))
        self.CBRepeat2.setText(_translate("MainWindow", "Repeat"))
        self.LblMs2.setText(_translate("MainWindow", "ms"))
        self.LblMs1.setText(_translate("MainWindow", "ms"))
        self.CBHex.setText(_translate("MainWindow", "Hex Mode"))
        self.BtnGraph.setText(_translate("MainWindow", "Show &Graph"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
import logo_rc
