import variables_design
import common_functions
from PyQt5 import QtWidgets, QtCore
import json
import os


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
        self.BtnAdd.clicked.connect(self.add_pressed)
        self.var_dict = {'length': '0', 'crc': '0', 'filedata': ""}
        self.load()

    def max_changed(self):
        """
        changes max value of var
        :return:
        """
        self.SpinMin.setMaximum(self.SpinMax.value())
        self.SliderVar.setMaximum(self.SpinMax.value())
        self.save()

    def min_changed(self):
        """
        changes max value of var
        :return:
        """
        self.SpinMax.setMinimum(self.SpinMin.value())
        self.SliderVar.setMinimum(self.SpinMin.value())
        self.save()

    def step_changed(self):
        """
        changes max value of var
        :return:
        """
        self.SliderVar.setSingleStep(self.SpinStep.value())
        self.save()

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
        if self.SliderVar.value() != self.current_var:
            self.LineCurrent.setText(str(self.SliderVar.value()))
            self.current_var = self.SliderVar.value()
            if self.CBAuto.isChecked():
                self.send_pressed()

    def send_pressed(self):
        """
        send button pressed and we need send command to serial port
        :return:
        """
        self.save()
        command = self.LineCommand.text().replace("$%s" % self.LineVarName.text(), str(self.LineCurrent.text()))
        self.send_signal.emit(command)

    def add_pressed(self):
        """
        add new variable
        :return:
        """
        name = self.LineName.text()
        if name:
            value = self.LineValue.text()
            self.var_dict[name] = value
            self.ListVariables.addItem("$%s = %s" % (name, value))
            self.save()

    def save(self):
        """
        saves variables data
        """
        with open("variables.json", "w") as f:
            var_dict_to_save = {key: self.var_dict[key] for key in self.var_dict.keys()
                                if key not in ['length', 'crc', 'filedata']}
            range_var_dict_to_save = {'name': self.LineVarName.text(), 'min_value': self.SpinMin.value(),
                                      'max_value': self.SpinMax.value(), 'step': self.SpinStep.value(),
                                      'is_autosend': self.CBAuto.isChecked(), 'command': self.LineCommand.text()}
            json.dump({'Variables': var_dict_to_save, 'Range': range_var_dict_to_save}, f, indent=4)

    def load(self):
        """
        loads variable data from variables.json
        :return:
        """
        if os.path.exists("variables.json"):
            with open("variables.json") as f:
                try:
                    var_data = json.load(f)
                    if 'Variables' in var_data.keys() and isinstance(var_data['Variables'], dict):
                        for key in var_data['Variables'].keys():
                            self.var_dict[key] = var_data['Variables'][key]
                            self.ListVariables.addItem("$%s = %s" % (key, var_data['Variables'][key]))
                    if 'Range' in var_data.keys() and isinstance(var_data['Range'], dict):
                        range_data = var_data['Range']
                        try:
                            if 'name' in range_data.keys():
                                self.LineVarName.setText(range_data['name'])
                            if 'min_value' in range_data.keys():
                                self.SpinMin.setValue(range_data['min_value'])
                            if 'max_value' in range_data.keys():
                                self.SpinMax.setValue(range_data['max_value'])
                            if 'step' in range_data.keys():
                                self.SpinStep.setValue(range_data['step'])
                            if 'is_autosend' in range_data.keys():
                                self.CBAuto.setChecked(range_data['is_autosend'])
                            if 'command' in range_data.keys():
                                self.LineCommand.setText(range_data['command'])
                            self.value_changed()
                        except (AttributeError, ValueError):
                            common_functions.error_message('Cannot load saved variables')
                except json.JSONDecodeError:
                    common_functions.error_message("Cannot load saved variables")
