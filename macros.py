import macros_design
from PyQt5 import QtWidgets
import data_types
from typing import List, Optional
import common_functions


class Settings(QtWidgets.QWidget, macros_design.Ui_Form):

    def __init__(self, current_macros: data_types.MacroSet, all_macros: List[data_types.MacroSet]):
        super().__init__()
        self.setupUi(self)

        self.macros_names_list = [self.LineName1, self.LineName2, self.LineName3, self.LineName4, self.LineName5,
                                  self.LineName6, self.LineName7, self.LineName8, self.LineName9, self.LineName10,
                                  self.LineName11, self.LineName12, self.LineName13, self.LineName14, self.LineName15,
                                  self.LineName16, self.LineName17, self.LineName18, self.LineName19, self.LineName20]

        self.macros_command_list = [self.LineCommand1, self.LineCommand2, self.LineCommand3, self.LineCommand4,
                                    self.LineCommand5, self.LineCommand6, self.LineCommand7, self.LineCommand8,
                                    self.LineCommand, self.LineCommand10, self.LineCommand11, self.LineCommand12,
                                    self.LineCommand13, self.LineCommand14, self.LineCommand15, self.LineCommand16,
                                    self.LineCommand17, self.LineCommand18, self.LineCommand19, self.LineCommand20]
        self.macros_dict = {i: (self.macros_names_list[i], self.macros_command_list[i])
                            for i in range(data_types.max_macros)}
        self.all_macros = all_macros
        self.current_macros = current_macros

    def create_macros_set(self) -> Optional[data_types.MacroSet]:
        """

        :return:
        """
        name = self.LineNameSet.text()
        if not name:
            common_functions.error_message("Macros Set Name is empty")
            return None
        if name in [macro.name for macro in self.all_macros]:
            common_functions.error_message("Macros Name already used")
            return None
        macros_set = data_types.MacroSet(name=name, macros=list())
        for key in self.macros_dict.keys():
            macros_set.macros.append(data_types.Macro(
                name=self.macros_dict[key][0].text(), command=self.macros_dict[key][1].text()))
        return macros_set

    def apply_pressed(self):
        new_macros_set = self.create_macros_set()
        if new_macros_set:
            self.current_macros = new_macros_set
