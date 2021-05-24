import macros_design
from PyQt5 import QtWidgets, QtCore, QtGui
import data_types
from typing import List, Optional
import common_functions
from dataclasses import asdict
import json
import os


class Macros(QtWidgets.QWidget, macros_design.Ui_Form):

    applied_signal = QtCore.pyqtSignal(str)
    edited_signal = QtCore.pyqtSignal()
    send_signal = QtCore.pyqtSignal(str)

    def __init__(self, current_macros: data_types.MacroSet, all_macros: List[data_types.MacroSet], current_font):
        super().__init__()
        self.setupUi(self)
        self.macros_names_list, self.macros_command_list, self.btn_send_list = list(), list(), list()
        self.btn_icon_list, self.current_icon_paths = list(), list()
        self.create_data_lists()
        self.all_macros = all_macros
        self.current_macros = current_macros
        self.load_current_set()
        self.BtnSave.clicked.connect(self.save_pressed)
        self.BtnAll.clicked.connect(self.all_pressed)
        self.BtnDelete.clicked.connect(self.delete_pressed)
        self.BtnAdd.clicked.connect(self.add_pressed)
        self.CBMacros.currentTextChanged.connect(self.selected_changed)
        for line in self.macros_command_list:
            line.setFont(current_font)
        self.BtnImport.clicked.connect(self.append_pressed)
        self.BtnExport.clicked.connect(self.export_pressed)

    def create_data_lists(self):
        """
        creates listif ob buttons and fields
        :return:
        """
        self.macros_names_list = [self.LineName1, self.LineName2, self.LineName3, self.LineName4, self.LineName5,
                                  self.LineName6, self.LineName7, self.LineName8, self.LineName9, self.LineName10,
                                  self.LineName11, self.LineName12, self.LineName13, self.LineName14, self.LineName15,
                                  self.LineName16, self.LineName17, self.LineName18, self.LineName19, self.LineName20,
                                  self.LineName21, self.LineName22, self.LineName23, self.LineName24, self.LineName25,
                                  self.LineName26, self.LineName27, self.LineName28, self.LineName29, self.LineName30]

        self.macros_command_list = [self.LineCommand1, self.LineCommand2, self.LineCommand3, self.LineCommand4,
                                    self.LineCommand5, self.LineCommand6, self.LineCommand7, self.LineCommand8,
                                    self.LineCommand9, self.LineCommand10, self.LineCommand11, self.LineCommand12,
                                    self.LineCommand13, self.LineCommand14, self.LineCommand15, self.LineCommand16,
                                    self.LineCommand17, self.LineCommand18, self.LineCommand19, self.LineCommand20,
                                    self.LineCommand21, self.LineCommand22, self.LineCommand23, self.LineCommand24,
                                    self.LineCommand25, self.LineCommand26, self.LineCommand27, self.LineCommand28,
                                    self.LineCommand29, self.LineCommand30]

        self.btn_send_list = [self.BtnSend1, self.BtnSend2, self.BtnSend3, self.BtnSend4, self.BtnSend5,
                              self.BtnSend6, self.BtnSend7, self.BtnSend8, self.BtnSend9, self.BtnSend10,
                              self.BtnSend11, self.BtnSend12, self.BtnSend13, self.BtnSend14, self.BtnSend15,
                              self.BtnSend16, self.BtnSend17, self.BtnSend18, self.BtnSend19, self.BtnSend20,
                              self.BtnSend21, self.BtnSend22, self.BtnSend23, self.BtnSend24, self.BtnSend25,
                              self.BtnSend26, self.BtnSend27, self.BtnSend28, self.BtnSend29, self.BtnSend30]

        self.btn_icon_list = [self.BtnIcon1, self.BtnIcon2, self.BtnIcon3, self.BtnIcon4, self.BtnIcon5,
                              self.BtnIcon6, self.BtnIcon7, self.BtnIcon8, self.BtnIcon9, self.BtnIcon10,
                              self.BtnIcon11, self.BtnIcon12, self.BtnIcon13, self.BtnIcon14, self.BtnIcon15,
                              self.BtnIcon16, self.BtnIcon17, self.BtnIcon18, self.BtnIcon19, self.BtnIcon20,
                              self.BtnIcon21, self.BtnIcon22, self.BtnIcon23, self.BtnIcon24, self.BtnIcon25,
                              self.BtnIcon26, self.BtnIcon27, self.BtnIcon28, self.BtnIcon29, self.BtnIcon30]
        self.current_icon_paths = [""] * 30
        for btn in self.btn_send_list:
            btn.clicked.connect(self.btn_clicked)
        for btn in self.btn_icon_list:
            btn.clicked.connect(self.icon_clicked)

    def load_current_set(self):
        """
        loads current macros to ui
        :return:
        """
        self.CBMacros.addItem('None')
        self.CBMacros.addItems([macrosset.name for macrosset in self.all_macros])
        if self.current_macros and self.current_macros.macros:
            self.load_macros(self.current_macros)

    def load_macros(self, macros: data_types.MacroSet):
        """
        loads macroset to controls
        :param macros: macros to load
        :return:
        """
        self.current_macros = macros
        self.LineNameSet.setText(macros.name)
        self.CBMacros.setCurrentText(macros.name)
        for (index, macro) in enumerate(macros.macros):
            self.macros_names_list[index].setText(macro.name)
            self.macros_command_list[index].setText(macro.command)
            icon = QtGui.QIcon(macro.icon_path) if macro.icon_path else QtGui.QIcon()
            self.btn_send_list[index].setIcon(icon)
        self.current_icon_paths = [macro.icon_path for macro in macros.macros]

    def selected_changed(self):
        """
        loads data of selected macros
        :return:
        """
        if self.CBMacros.currentText() == 'None':
            self.clear()
        else:
            macros = data_types.get_macros_by_name(self.CBMacros.currentText(), self.all_macros)
            if macros:
                self.load_macros(macros)

    def create_macros_set(self) -> Optional[data_types.MacroSet]:
        """
        create new macros from data from fields and add it to all macroses
        :return: new macros
        """
        name = self.LineNameSet.text()
        if not name:
            common_functions.error_message("Macros Set Name is empty")
            return None
        if name not in [macro.name for macro in self.all_macros]:
            new_macros_set = data_types.MacroSet(name=name, macros=list())
            for i in range(data_types.max_macros):
                new_macros_set.macros.append(data_types.Macro(name=self.macros_names_list[i].text(),
                                                              command=self.macros_command_list[i].text(),
                                                              icon_path=self.current_icon_paths[i]))
            self.all_macros.append(new_macros_set)
            self.CBMacros.addItem(name)
            self.CBMacros.setCurrentText(name)
            return new_macros_set
        else:
            macros_used = data_types.get_macros_by_name(name, self.all_macros)
            for i in range(data_types.max_macros):
                macros_used.macros[i].name = self.macros_names_list[i].text()
                macros_used.macros[i].command = self.macros_command_list[i].text()
                macros_used.macros[i].icon_path = self.current_icon_paths[i]
            return macros_used

    def delete_pressed(self):
        name = self.LineNameSet.text()
        if name and name in [macro.name for macro in self.all_macros]:
            # noinspection PyCallByClass
            reply = QtWidgets.QMessageBox.question(self, 'Message', 'Do you really want to delete "%s" macros set?'
                                                   % name, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                macros_to_delete = data_types.get_macros_by_name(name, self.all_macros)
                self.all_macros.remove(macros_to_delete)
                self.CBMacros.clear()
                self.CBMacros.addItem('None')
                self.CBMacros.addItems([macrosset.name for macrosset in self.all_macros])
                self.save()
        self.CBMacros.setCurrentText('None')
        self.edited_signal.emit()

    def clear(self):
        """
        clears macros fields
        :return:
        """
        self.LineNameSet.clear()
        for field in self.macros_command_list:
            field.clear()
        for field in self.macros_names_list:
            field.clear()
        for btn in self.btn_send_list:
            btn.setIcon(QtGui.QIcon())

    def save_pressed(self):
        """
        save macros to file and not add to current
        :return:
        """
        new_macros_set = self.create_macros_set()
        if new_macros_set:
            self.save()
            self.LblStatus.setText("Macros set saved")
            self.edited_signal.emit()

    def all_pressed(self):
        new_macros_set = self.create_macros_set()
        if new_macros_set:
            self.current_macros = new_macros_set
            self.save()
            self.LblStatus.setText("Macros set saved and applied")
            self.applied_signal.emit(new_macros_set.name)

    def save(self):
        """
        saves macros data to file
        :return:
        """
        dump = {'Macros': [asdict(macros) for macros in self.all_macros]}
        with open("macros.json", "w") as f:
            json.dump(dump, f, indent=4)

    def btn_clicked(self):
        """
        send send signal to main app
        :return:
        """
        index = self.btn_send_list.index(self.sender())
        self.send_signal.emit(self.macros_command_list[index].text())

    def icon_clicked(self):
        """
        selects icon for current macros.
        :return:
        """
        sender = self.sender()
        icon_filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Select icon...', "")[0]
        if icon_filename and os.path.splitext(icon_filename.lower())[1] in data_types.icon_exts:
            index = self.btn_icon_list.index(sender)
            icon = QtGui.QIcon()
            icon.addFile(icon_filename)
            self.btn_send_list[index].setIcon(icon)
            self.current_macros.macros[index].icon_path = icon_filename
            self.current_icon_paths[index] = icon_filename
            self.save()
        elif icon_filename:
            common_functions.error_message("Wrong icon format")

    def add_pressed(self):
        """
        for adding new macros
        :return:
        """
        self.CBMacros.setCurrentText('None')

    def append_pressed(self):
        """
        adds macroses from selected file.
        :return:
        """
        new_filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Select macro file', "")[0]
        if new_filename:
            with open(new_filename) as f:
                macros_data = json.load(f)
                new_macros, warning = data_types.create_macros_from_list(macros_data['Macros'])
                if new_macros:
                    self.all_macros.extend(new_macros)
                    self.save()
                    self.edited_signal.emit()

    def export_pressed(self):
        new_filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Select export file', "")[0]
        if new_filename:
            with open(new_filename, "w") as f:
                dump = {'Macros': [asdict(self.current_macros)]}
                json.dump(dump, f, indent=4)

