# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'testplot2pyqt5.ui'
# Created by: PyQt5 UI code generator 5.10
# WARNING! All changes made in this file will be lost!

# -*-coding:utf-8-*-
import sys

import matplotlib
import networkx as nx
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 544)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = PlotCanvas(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.widget.setObjectName("widget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class PlotCanvas(
    FigureCanvas):  # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键

    def __init__(self, parent=None, width=500, height=500, dpi=100):
        fig = Figure(figsize=(width, height),
                     dpi=dpi)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        self.axes = fig.add_subplot(111)  # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

        self.plot()

        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self):
        G = nx.DiGraph()
        G.add_node(1)
        G.add_node(2)
        G.add_edge(1, 2)
        nx.draw(G, pos=nx.spring_layout(G), node_color='w', ax=self.axes,
                edge_color='b', with_labels=True, alpha=1,
                font_size=10, node_size=20, arrows=True)

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    # app.installEventFilter(main)
    sys.exit(app.exec_())
