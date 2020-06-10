import variables_design
from PyQt5 import QtWidgets, QtCore, QtGui


class Variables(QtWidgets.QWidget, variables_design.Ui_Form):

    send_signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.SpinMax.valueChanged.connect(self.max_changed)
        self.SpinMin.valueChanged.connect(self.min_changed)
        self.SpinStep.valueChanged.connect(self.step_changed)
        self.SliderVar.valueChanged.connect(self.value_changed)
        self.BtnSend.clicked.connect(self.send_pressed)
        self.current_var = self.SliderVar.value()

    def max_changed(self):
        """
        changes max value of var
        :return:
        """
        self.SpinMin.setMaximum(self.SpinMax.value())
        self.SliderVar.setMaximum(self.SpinMax.value())

    def min_changed(self):
        """
        changes max value of var
        :return:
        """
        self.SpinMax.setMinimum(self.SpinMin.value())
        self.SliderVar.setMinimum(self.SpinMin.value())

    def step_changed(self):
        """
        changes max value of var
        :return:
        """
        self.SliderVar.setSingleStep(self.SpinStep.value())

    def value_changed(self):
        """
        slider value changed
        :return:
        """
        current = self.SliderVar.value()
        delta = current - self.current_var if current > self.current_var else self.current_var - current
        step = self.SliderVar.singleStep()
        delta %= step
        if delta > 0:
            if current > self.current_var:
                self.SliderVar.setValue(current - delta)
            else:
                self.SliderVar.setValue(current - step + delta)
        self.LineCurrent.setText(str(self.SliderVar.value()))
        self.current_var = self.SliderVar.value()
        if self.CBAuto.isChecked():
            self.send_pressed()

    def send_pressed(self):
        """
        send button pressed and we need send command to serial port
        :return:
        """
        command = self.LineCommand.text().replace("$%s" % self.LineVarName.text(), str(self.LineCurrent.text()))
        self.send_signal.emit(command)