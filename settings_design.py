# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1202, 467)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Settings/icon/customize.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.GBDatabits = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GBDatabits.setFont(font)
        self.GBDatabits.setCheckable(False)
        self.GBDatabits.setObjectName("GBDatabits")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.GBDatabits)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.RBDatabits6 = QtWidgets.QRadioButton(self.GBDatabits)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RBDatabits6.setFont(font)
        self.RBDatabits6.setObjectName("RBDatabits6")
        self.gridLayout_2.addWidget(self.RBDatabits6, 2, 0, 1, 1)
        self.RBDatabits5 = QtWidgets.QRadioButton(self.GBDatabits)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RBDatabits5.setFont(font)
        self.RBDatabits5.setObjectName("RBDatabits5")
        self.gridLayout_2.addWidget(self.RBDatabits5, 1, 0, 1, 1)
        self.RBDatabits7 = QtWidgets.QRadioButton(self.GBDatabits)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RBDatabits7.setFont(font)
        self.RBDatabits7.setObjectName("RBDatabits7")
        self.gridLayout_2.addWidget(self.RBDatabits7, 3, 0, 1, 1)
        self.RBDatabits8 = QtWidgets.QRadioButton(self.GBDatabits)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RBDatabits8.setFont(font)
        self.RBDatabits8.setChecked(True)
        self.RBDatabits8.setObjectName("RBDatabits8")
        self.gridLayout_2.addWidget(self.RBDatabits8, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.GBDatabits, 0, 0, 2, 1)
        self.GBParity = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GBParity.setFont(font)
        self.GBParity.setObjectName("GBParity")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.GBParity)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.RBParityMark = QtWidgets.QRadioButton(self.GBParity)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RBParityMark.setFont(font)
        self.RBParityMark.setObjectName("RBParityMark")
        self.gridLayout_3.addWidget(self.RBParityMark, 3, 0, 1, 1)
        self.RBParityNone = QtWidgets.QRadioButton(self.GBParity)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RBParityNone.setFont(font)
        self.RBParityNone.setChecked(True)
        self.RBParityNone.setObjectName("RBParityNone")
        self.gridLayout_3.addWidget(self.RBParityNone, 0, 0, 1, 1)
        self.RBParityOdd = QtWidgets.QRadioButton(self.GBParity)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RBParityOdd.setFont(font)
        self.RBParityOdd.setObjectName("RBParityOdd")
        self.gridLayout_3.addWidget(self.RBParityOdd, 1, 0, 1, 1)
        self.RBParityEven = QtWidgets.QRadioButton(self.GBParity)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RBParityEven.setFont(font)
        self.RBParityEven.setObjectName("RBParityEven")
        self.gridLayout_3.addWidget(self.RBParityEven, 2, 0, 1, 1)
        self.RBParitySpace = QtWidgets.QRadioButton(self.GBParity)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RBParitySpace.setFont(font)
        self.RBParitySpace.setObjectName("RBParitySpace")
        self.gridLayout_3.addWidget(self.RBParitySpace, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.GBParity, 0, 1, 2, 1)
        self.GBStopBits = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GBStopBits.setFont(font)
        self.GBStopBits.setObjectName("GBStopBits")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.GBStopBits)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.RBStopbits1 = QtWidgets.QRadioButton(self.GBStopBits)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RBStopbits1.setFont(font)
        self.RBStopbits1.setObjectName("RBStopbits1")
        self.gridLayout_4.addWidget(self.RBStopbits1, 0, 0, 1, 1)
        self.RBStopbits15 = QtWidgets.QRadioButton(self.GBStopBits)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RBStopbits15.setFont(font)
        self.RBStopbits15.setObjectName("RBStopbits15")
        self.gridLayout_4.addWidget(self.RBStopbits15, 1, 0, 1, 1)
        self.RBStopbits2 = QtWidgets.QRadioButton(self.GBStopBits)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RBStopbits2.setFont(font)
        self.RBStopbits2.setObjectName("RBStopbits2")
        self.gridLayout_4.addWidget(self.RBStopbits2, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.GBStopBits, 2, 0, 1, 1)
        self.GBHandshaking = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GBHandshaking.setFont(font)
        self.GBHandshaking.setObjectName("GBHandshaking")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.GBHandshaking)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.RBHandRts = QtWidgets.QRadioButton(self.GBHandshaking)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RBHandRts.setFont(font)
        self.RBHandRts.setObjectName("RBHandRts")
        self.gridLayout_5.addWidget(self.RBHandRts, 1, 0, 1, 1)
        self.RBHandNone = QtWidgets.QRadioButton(self.GBHandshaking)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RBHandNone.setFont(font)
        self.RBHandNone.setObjectName("RBHandNone")
        self.gridLayout_5.addWidget(self.RBHandNone, 0, 0, 1, 1)
        self.RBHandXOnOFf = QtWidgets.QRadioButton(self.GBHandshaking)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RBHandXOnOFf.setFont(font)
        self.RBHandXOnOFf.setObjectName("RBHandXOnOFf")
        self.gridLayout_5.addWidget(self.RBHandXOnOFf, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.GBHandshaking, 2, 1, 1, 1)
        self.GBCRC = QtWidgets.QGroupBox(Form)
        self.GBCRC.setObjectName("GBCRC")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.GBCRC)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.SpinPoly = QtWidgets.QSpinBox(self.GBCRC)
        self.SpinPoly.setMaximum(9999)
        self.SpinPoly.setProperty("value", 4129)
        self.SpinPoly.setObjectName("SpinPoly")
        self.gridLayout_9.addWidget(self.SpinPoly, 0, 1, 1, 1)
        self.LblPoly = QtWidgets.QLabel(self.GBCRC)
        self.LblPoly.setObjectName("LblPoly")
        self.gridLayout_9.addWidget(self.LblPoly, 0, 0, 1, 1)
        self.LblStart = QtWidgets.QLabel(self.GBCRC)
        self.LblStart.setObjectName("LblStart")
        self.gridLayout_9.addWidget(self.LblStart, 1, 0, 1, 1)
        self.SpinStart = QtWidgets.QSpinBox(self.GBCRC)
        self.SpinStart.setMaximum(65535)
        self.SpinStart.setObjectName("SpinStart")
        self.gridLayout_9.addWidget(self.SpinStart, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.GBCRC, 2, 3, 1, 1)
        self.CBTextSettings = QtWidgets.QGroupBox(Form)
        self.CBTextSettings.setObjectName("CBTextSettings")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.CBTextSettings)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.CBEndLine = QtWidgets.QCheckBox(self.CBTextSettings)
        self.CBEndLine.setChecked(True)
        self.CBEndLine.setObjectName("CBEndLine")
        self.gridLayout_8.addWidget(self.CBEndLine, 0, 0, 1, 1)
        self.CBTime = QtWidgets.QCheckBox(self.CBTextSettings)
        self.CBTime.setObjectName("CBTime")
        self.gridLayout_8.addWidget(self.CBTime, 0, 1, 1, 1)
        self.CBBytes = QtWidgets.QCheckBox(self.CBTextSettings)
        self.CBBytes.setChecked(True)
        self.CBBytes.setObjectName("CBBytes")
        self.gridLayout_8.addWidget(self.CBBytes, 1, 0, 1, 1)
        self.CBScroll = QtWidgets.QCheckBox(self.CBTextSettings)
        self.CBScroll.setChecked(True)
        self.CBScroll.setObjectName("CBScroll")
        self.gridLayout_8.addWidget(self.CBScroll, 1, 1, 1, 1)
        self.CBShowSent = QtWidgets.QCheckBox(self.CBTextSettings)
        self.CBShowSent.setChecked(True)
        self.CBShowSent.setObjectName("CBShowSent")
        self.gridLayout_8.addWidget(self.CBShowSent, 2, 0, 1, 1)
        self.LblDecode = QtWidgets.QLabel(self.CBTextSettings)
        self.LblDecode.setObjectName("LblDecode")
        self.gridLayout_8.addWidget(self.LblDecode, 3, 0, 1, 1)
        self.CBDecode = QtWidgets.QComboBox(self.CBTextSettings)
        self.CBDecode.setObjectName("CBDecode")
        self.CBDecode.addItem("")
        self.CBDecode.addItem("")
        self.CBDecode.addItem("")
        self.gridLayout_8.addWidget(self.CBDecode, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.CBTextSettings, 0, 3, 2, 1)
        self.GBColor = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GBColor.setFont(font)
        self.GBColor.setObjectName("GBColor")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.GBColor)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.BtnFont = QtWidgets.QPushButton(self.GBColor)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.BtnFont.setFont(font)
        self.BtnFont.setObjectName("BtnFont")
        self.gridLayout_6.addWidget(self.BtnFont, 0, 0, 1, 3)
        self.LblFont = QtWidgets.QLabel(self.GBColor)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.LblFont.setFont(font)
        self.LblFont.setObjectName("LblFont")
        self.gridLayout_6.addWidget(self.LblFont, 0, 3, 1, 1)
        self.GBBackColor = QtWidgets.QGroupBox(self.GBColor)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GBBackColor.setFont(font)
        self.GBBackColor.setObjectName("GBBackColor")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.GBBackColor)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BtnBackgroundColor = QtWidgets.QPushButton(self.GBBackColor)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.BtnBackgroundColor.setFont(font)
        self.BtnBackgroundColor.setObjectName("BtnBackgroundColor")
        self.horizontalLayout.addWidget(self.BtnBackgroundColor)
        self.LblBackgroundColor = QtWidgets.QLabel(self.GBBackColor)
        self.LblBackgroundColor.setStyleSheet("background-color: rgb(255,255,255)")
        self.LblBackgroundColor.setText("")
        self.LblBackgroundColor.setObjectName("LblBackgroundColor")
        self.horizontalLayout.addWidget(self.LblBackgroundColor)
        self.gridLayout_6.addWidget(self.GBBackColor, 1, 0, 2, 4)
        self.GBSent = QtWidgets.QGroupBox(self.GBColor)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GBSent.setFont(font)
        self.GBSent.setObjectName("GBSent")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.GBSent)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BtnSentColor = QtWidgets.QPushButton(self.GBSent)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.BtnSentColor.setFont(font)
        self.BtnSentColor.setObjectName("BtnSentColor")
        self.horizontalLayout_2.addWidget(self.BtnSentColor)
        self.LblSentColor = QtWidgets.QLabel(self.GBSent)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.LblSentColor.setFont(font)
        self.LblSentColor.setStyleSheet("background-color: rgb(255,255,255); color: rgb(00,102,51)")
        self.LblSentColor.setObjectName("LblSentColor")
        self.horizontalLayout_2.addWidget(self.LblSentColor)
        self.gridLayout_6.addWidget(self.GBSent, 3, 0, 1, 4)
        self.GBReceived = QtWidgets.QGroupBox(self.GBColor)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GBReceived.setFont(font)
        self.GBReceived.setObjectName("GBReceived")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.GBReceived)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BtnReceivedColor = QtWidgets.QPushButton(self.GBReceived)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.BtnReceivedColor.setFont(font)
        self.BtnReceivedColor.setObjectName("BtnReceivedColor")
        self.horizontalLayout_3.addWidget(self.BtnReceivedColor)
        self.LblReceivedColor = QtWidgets.QLabel(self.GBReceived)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.LblReceivedColor.setFont(font)
        self.LblReceivedColor.setStyleSheet("background-color: white")
        self.LblReceivedColor.setObjectName("LblReceivedColor")
        self.horizontalLayout_3.addWidget(self.LblReceivedColor)
        self.gridLayout_6.addWidget(self.GBReceived, 4, 0, 1, 4)
        self.GBByteColor = QtWidgets.QGroupBox(self.GBColor)
        self.GBByteColor.setObjectName("GBByteColor")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.GBByteColor)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.BtnColorByte = QtWidgets.QPushButton(self.GBByteColor)
        self.BtnColorByte.setObjectName("BtnColorByte")
        self.gridLayout_7.addWidget(self.BtnColorByte, 0, 0, 1, 1)
        self.LblColorByte = QtWidgets.QLabel(self.GBByteColor)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.LblColorByte.setFont(font)
        self.LblColorByte.setStyleSheet("background-color:rgb(255, 255, 255); color:rgb(255, 0, 0);")
        self.LblColorByte.setObjectName("LblColorByte")
        self.gridLayout_7.addWidget(self.LblColorByte, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.GBByteColor, 5, 0, 1, 4)
        self.gridLayout.addWidget(self.GBColor, 0, 4, 3, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.RBDatabits5, self.RBDatabits6)
        Form.setTabOrder(self.RBDatabits6, self.RBDatabits7)
        Form.setTabOrder(self.RBDatabits7, self.RBDatabits8)
        Form.setTabOrder(self.RBDatabits8, self.RBParityNone)
        Form.setTabOrder(self.RBParityNone, self.RBParityOdd)
        Form.setTabOrder(self.RBParityOdd, self.RBParityEven)
        Form.setTabOrder(self.RBParityEven, self.RBParityMark)
        Form.setTabOrder(self.RBParityMark, self.RBParitySpace)
        Form.setTabOrder(self.RBParitySpace, self.RBStopbits1)
        Form.setTabOrder(self.RBStopbits1, self.RBStopbits15)
        Form.setTabOrder(self.RBStopbits15, self.RBStopbits2)
        Form.setTabOrder(self.RBStopbits2, self.RBHandNone)
        Form.setTabOrder(self.RBHandNone, self.RBHandRts)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Settings"))
        self.GBDatabits.setTitle(_translate("Form", "Data bits"))
        self.RBDatabits6.setText(_translate("Form", "6"))
        self.RBDatabits5.setText(_translate("Form", "5"))
        self.RBDatabits7.setText(_translate("Form", "7"))
        self.RBDatabits8.setText(_translate("Form", "8"))
        self.GBParity.setTitle(_translate("Form", "Parity"))
        self.RBParityMark.setText(_translate("Form", "Mark"))
        self.RBParityNone.setText(_translate("Form", "None"))
        self.RBParityOdd.setText(_translate("Form", "Odd"))
        self.RBParityEven.setText(_translate("Form", "Even"))
        self.RBParitySpace.setText(_translate("Form", "Space"))
        self.GBStopBits.setTitle(_translate("Form", "Stop bits"))
        self.RBStopbits1.setText(_translate("Form", "1"))
        self.RBStopbits15.setText(_translate("Form", "1.5"))
        self.RBStopbits2.setText(_translate("Form", "2"))
        self.GBHandshaking.setTitle(_translate("Form", "Handshaking"))
        self.RBHandRts.setText(_translate("Form", "RTS/CTS"))
        self.RBHandNone.setText(_translate("Form", "None"))
        self.RBHandXOnOFf.setText(_translate("Form", "XON/XOFF"))
        self.GBCRC.setTitle(_translate("Form", "CRC16 params"))
        self.LblPoly.setText(_translate("Form", "Polynom:"))
        self.LblStart.setText(_translate("Form", "Start Value: "))
        self.CBTextSettings.setTitle(_translate("Form", "TextSettings"))
        self.CBEndLine.setText(_translate("Form", "CR = LF"))
        self.CBTime.setText(_translate("Form", "Show &Timestamp"))
        self.CBBytes.setText(_translate("Form", "Use Byte Codes"))
        self.CBScroll.setText(_translate("Form", "Scr&oll"))
        self.CBShowSent.setText(_translate("Form", "S&how sent "))
        self.LblDecode.setText(_translate("Form", "For non-ASCII characters"))
        self.CBDecode.setItemText(0, _translate("Form", "Ignore"))
        self.CBDecode.setItemText(1, _translate("Form", "Red ? symbols"))
        self.CBDecode.setItemText(2, _translate("Form", "Decode in Win-1251"))
        self.GBColor.setTitle(_translate("Form", "TextField Style"))
        self.BtnFont.setText(_translate("Form", "Select Font Style"))
        self.LblFont.setText(_translate("Form", "Font  Style"))
        self.GBBackColor.setTitle(_translate("Form", "Background color"))
        self.BtnBackgroundColor.setText(_translate("Form", "Select Color"))
        self.GBSent.setTitle(_translate("Form", "Font Sent Color"))
        self.BtnSentColor.setText(_translate("Form", "Select Color"))
        self.LblSentColor.setText(_translate("Form", "Sent"))
        self.GBReceived.setTitle(_translate("Form", "Font Received Color"))
        self.BtnReceivedColor.setText(_translate("Form", "Select Color"))
        self.LblReceivedColor.setText(_translate("Form", "Received"))
        self.GBByteColor.setTitle(_translate("Form", "BytesCodes Color"))
        self.BtnColorByte.setText(_translate("Form", "Select Color"))
        self.LblColorByte.setText(_translate("Form", "$FF"))
import logo_rc
