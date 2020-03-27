from PyQt5.QtWidgets import QMessageBox


def error_message(text: str):
    error = QMessageBox()
    error.setIcon(QMessageBox.Critical)
    error.setText(text)
    error.setWindowTitle('Error!')
    error.setStandardButtons(QMessageBox.Ok)
    error.exec_()
