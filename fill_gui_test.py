import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import gui.gui_fillblank
import gui.input_frame
from graph import subway_graph
from graph.subway_graph import init_graph_fillblank

num = 0  # 节点数
i = 0
list_node = []  # 节点信息列表
list_overload = []  # 负载列表
num_animate = 0  # 粒子数

# 图 G
G = subway_graph.SubwayGraph()


class Form1(QtWidgets.QDialog, gui.input_frame.Ui_dialog):
    def __init__(self):
        super(Form1, self).__init__()
        self.setupUi(self)


# 填入总结点数
def event1(ui):  # 将节点数传回
    global num
    num = int(ui.lineEdit.text())
    print("total nodes in graph: ", num)
    return


def event2(d1):  # 将节点信息与负载装入列表
    global i
    global num
    # TODO 这里的增加边的次数和点数不是一定相等的，最好提供按钮来手动添加一组边，点击确定才停
    if i < num:
        node1 = d1.lineEdit.text()
        node2 = d1.lineEdit_2.text()
        nodeTuple = (int(node1), int(node2))
        list_node.append(nodeTuple)
        d1.lineEdit.setText("")
        d1.lineEdit_2.setText("")
        load = d1.lineEdit_3.text()
        list_overload.append(int(load))
        d1.lineEdit_3.setText("")
        i = i + 1
        d1.label.setText("第" + str(i + 1) + "个节点信息：")
    if i >= num:
        d1.close()
        print("all input nodes are:", list_node)
        print("all load are:", list_overload)
    return


def event3(ui):  # 传回粒子数
    global num_animate
    num_animate = int(ui.lineEdit_2.text())
    print("attack random nodes are:", num_animate)
    return

def event4(ui):  # 生成图
    # 初始化图
    G.init_subway_graph(num, 0.5, 0, num_animate)
    print("Subway graph has been initialed",G.edges)
    init_graph_fillblank(G, list_node,list_overload)
    return

if __name__ == "__main__":  # 创建gui函数
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = gui.gui_fillblank.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    d1 = Form1()
    ui.pushButton.clicked.connect(lambda: d1.show())
    ui.pushButton.clicked.connect(lambda: event1(ui))
    d1.pushButton.clicked.connect(lambda: event2(d1))
    ui.pushButton_2.clicked.connect(lambda: event3(ui))
    ui.pushButton_3.clicked.connect(lambda: event4(ui))
    sys.exit(app.exec_())

# create_gui()
