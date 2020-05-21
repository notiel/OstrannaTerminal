from typing import List
from PyQt5 import QtWidgets, QtGui
import pyqtgraph
import common_functions

colors = ['green', 'red', 'blue', 'magenta', 'yellow', 'darkGreen', 'darkMagenta', 'darkRed', 'black', 'cyan',
          'darkCyan', 'darkYellow', 'darkBlue', 'gray', 'darkGray']


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.data_x: List[float] = list()
        self.data_y: List[List[float]] = list()
        self.graphWidget = pyqtgraph.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.setTitle("<span style=\"color:green;font-size:30px\">QuetimaGraph</span>")
        self.graphWidget.setBackground('w')
        self.graphWidget.setLabel('left', "<span style=\"color:black;font-size:10px\"></span>")
        self.graphWidget.setLabel('bottom', "<span style=\"color:black;font-size:10px\"></span>")
        self.graphWidget.showGrid(x=True, y=True)
        self.data_lines = list()

    def create_graph(self, data_x: float, data_y: List[float]):
        """
        creates grapg with several lines for received data
        :param data_x: first x symbol
        :param data_y: list of y data
        :return:
        """
        pen = pyqtgraph.mkPen(color=(255, 255, 255))
        self.data_x = [data_x]
        for y in data_y:
            self.data_y.append([y])
        for y_data in self.data_y:
            self.data_lines.append(self.graphWidget.plot(self.data_x, y_data, pen=pen, symbol='o',
                                                         symbolSize=10,
                                                         symbolBrush=(QtGui.QColor(colors[self.data_y.index(y_data)]))))

    def update_plot_data(self, data_x: float, data_y: List[float]):
        """
        updates plot with new values
        :param data_x: new x data
        :param data_y: list with new y data
        :return:
        """
        self.data_x.append(data_x)
        for (i, y) in enumerate(data_y):
            try:
                self.data_y[i].append(y)
            except IndexError:
                common_functions.error_message('Too many items in data')
        for (i, line) in enumerate(self.data_lines):
            line.setData(self.data_x, self.data_y[i])
