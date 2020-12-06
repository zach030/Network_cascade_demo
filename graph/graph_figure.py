import matplotlib
import networkx as nx
import numpy as np

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# 创建一个matplotlib图形绘制类

class MyFigure(FigureCanvas):
    G = nx.Graph

    def __init__(self, G, width=5, height=4, dpi=100):
        self.G = G
        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # 第二步：在父类中激活Figure窗口
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)

    # 第四步：就是画图，【可以在此类中画，也可以在其它类中画】
    def plotGraph(self):
        nx.draw_networkx(self.G,pos=nx.circular_layout(self.G))

