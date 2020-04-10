import macros_design
from PyQt5 import QtWidgets, QtCore
import data_types
from typing import List, Optional
import common_functions
from dataclasses import asdict
import json


class Macros(QtWidgets.QWidget, macros_design.Ui_Form):

    applied_signal = QtCore.pyqtSignal(str)
    edited_signal = QtCore.pyqtSignal()

    def __init__(self, current_macros: data_types.MacroSet, all_macros: List[data_types.MacroSet]):
        super().__init__()
        self.setupUi(self)
        self.macros_names_list = [self.LineName1, self.LineName2, self.LineName3, self.LineName4, self.LineName5,
                                  self.LineName6, self.LineName7, self.LineName8, self.LineName9, self.LineName10,
                                  self.LineName11, self.LineName12, self.LineName13, self.LineName14, self.LineName15,
                                  self.LineName16, self.LineName17, self.LineName18, self.LineName19, self.LineName20]

        self.macros_command_list = [self.LineCommand1, self.LineCommand2, self.LineCommand3, self.LineCommand4,
                                    self.LineCommand5, self.LineCommand6, self.LineCommand7, self.LineCommand8,
                                    self.LineCommand9, self.LineCommand10, self.LineCommand11, self.LineCommand12,
                                    self.LineCommand13, self.LineCommand14, self.LineCommand15, self.LineCommand16,
                                    self.LineCommand17, self.LineCommand18, self.LineCommand19, self.LineCommand20]
        self.macros_dict = {i: (self.macros_names_list[i], self.macros_command_list[i])
                            for i in range(data_types.max_macros)}
        self.all_macros = all_macros
        self.current_macros = current_macros
        self.load_current_set()
        self.BtnSave.clicked.connect(self.save_pressed)
        self.BtnApply.clicked.connect(self.apply_pressed)
        self.BtnAll.clicked.connect(self.all_pressed)
        self.CBMacros.currentTextChanged.connect(self.selected_changed)

    def load_current_set(self):
        """
        loads current macros to ui
        :return:
        """
        self.CBMacros.addItem('None')
        self.CBMacros.addItems([macrosset.name for macrosset in self.all_macros])
        if self.current_macros.macros:
            self.load_macros(self.current_macros)

    def load_macros(self, macros: data_types.MacroSet):
        """
        loads macroset to controls
        :param macros: macros to load
        :return:
        """
        self.LineNameSet.setText(macros.name)
        self.CBMacros.setCurrentText(macros.name)
        for (index, macro) in enumerate(macros.macros):
            self.macros_dict[index][0].setText(macro.name)
            self.macros_dict[index][1].setText(macro.command)

    def selected_changed(self):
        """
        loads data of selected macros
        :return:
        """
        macros = data_types.get_macros_by_name(self.CBMacros.currentText(), self.all_macros)
        if macros:
            self.load_macros(macros)


    def create_macros_set(self, unique: bool) -> Optional[data_types.MacroSet]:
        """
        create new macros from data from fields and add it to all macroses
        :return: new macros
        """
        name = self.LineNameSet.text()
        if not name:
            common_functions.error_message("Macros Set Name is empty")
            return None
        if unique and name in [macro.name for macro in self.all_macros]:
            common_functions.error_message("Macros Name already used")
            return None
        macros_set = data_types.MacroSet(name=name, macros=list())
        for key in self.macros_dict.keys():
            macros_set.macros.append(data_types.Macro(
                name=self.macros_dict[key][0].text(), command=self.macros_dict[key][1].text()))
        if name not in [macro.name for macro in self.all_macros]:
            self.all_macros.append(macros_set)
        return macros_set

    def apply_pressed(self):
        """
        add macros as current
        :return:
        """
        new_macros_set = self.create_macros_set(False)
        if new_macros_set:
            self.current_macros = new_macros_set
            self.applied_signal.emit(new_macros_set.name)
            self.LblStatus.setText("Macros set applied")

    def save_pressed(self):
        """
        save macros to file and not add to current
        :return:
        """
        new_macros_set = self.create_macros_set(True)
        if new_macros_set:
            with open("macros.json", "w") as f:
                dump = {'Macros': [asdict(macros) for macros in self.all_macros]}
                json.dump(dump, f, indent=4)
            self.LblStatus.setText("Macros set saved")
            self.edited_signal.emit()

    def all_pressed(self):
        new_macros_set = self.create_macros_set(True)
        if new_macros_set:
            self.current_macros = new_macros_set
            dump = {'Macros': [asdict(macros) for macros in self.all_macros]}
            with open("macros.json", "w") as f:
                json.dump(dump, f, indent=4)
            self.LblStatus.setText("Macros set saved and applied")
            self.applied_signal.emit(new_macros_set.name)
