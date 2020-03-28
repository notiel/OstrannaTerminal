from PyQt5.QtWidgets import QMessageBox


def error_message(text: str):
    error = QMessageBox()
    error.setIcon(QMessageBox.Critical)
    error.setText(text)
    error.setWindowTitle('Error!')
    error.setStandardButtons(QMessageBox.Ok)
    error.exec_()

# text = ''.join(self._lines_queue)
#         self._plain_edit.setPlainText(text)
#         maximum = self._plain_edit.verticalScrollBar().maximum()
#         self._plain_edit.verticalScrollBar().setValue(maximum)
