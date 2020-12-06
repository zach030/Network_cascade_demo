import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import gui.gui_fillblank
import gui.input_frame
import gui.input_Overload
from graph import subway_graph
from graph.subway_graph import init_graph_fillblank

n = 0  # 边数
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


class Form2(QtWidgets.QDialog, gui.input_Overload.Ui_Dialog):
    def __init__(self):
        super(Form2, self).__init__()
        self.setupUi(self)


# 填入总结点数
def event1(ui):  # 将节点数传回
    global num
    num = int(ui.lineEdit.text())
    print("total nodes in graph: ", num)
    return


def event2(d1):  # 将节点信息装入列表
    global n
    global num
    # TODO 这里的增加边的次数和点数不是一定相等的，最好提供按钮来手动添加一组边，点击确定才停 @zhang
    node1 = d1.lineEdit.text()
    node2 = d1.lineEdit_2.text()
    nodeTuple = (int(node1), int(node2))
    print(node1+node2)
    list_node.append(nodeTuple)
    d1.lineEdit.setText("")
    d1.lineEdit_2.setText("")
    n = n + 1
    d1.label.setText("第" + str(n + 1) + "条边信息：")
    return


def event5(d1):  # 结束输入边信息
    d1.close()
    # print("all input nodes are:", list_node)
    return


def event6(d2):  # 输入负载
    global i
    global num
    # TODO 这里的增加边的次数和点数不是一定相等的，最好提供按钮来手动添加一组边，点击确定才停 @zhang
    if i < num:
        load = d2.lineEdit.text()
        print(load)
        list_overload.append(int(load))
        d2.lineEdit.setText("")
        i = i + 1
        d2.label.setText("第" + str(i + 1) + "个节点负载：")
    if i >= num:
        d2.close()
        print("all load are:", list_overload)
    return


def event3(ui):  # 传回粒子数
    global num_animate
    num_animate = int(ui.lineEdit_2.text())
    print("attack random nodes are:", num_animate)
    return


def event4():  # 生成图
    # 初始化图
    # TODO 按开始攻击之后，前两个函数会出现问题，print无法输出 @ zhou
    G.init_subway_graph(num, 0.5, 0, num_animate)
    init_graph_fillblank(G, list_node, list_overload)
    print("Subway graph has been initialed", G.edges)
    return


if __name__ == "__main__":  # 创建gui函数
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = gui.gui_fillblank.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    d1 = Form1()
    d2 = Form2()
    ui.pushButton.clicked.connect(lambda: d1.show())
    ui.pushButton.clicked.connect(lambda: event1(ui))
    d1.pushButton.clicked.connect(lambda: event2(d1))
    d1.pushButton_2.clicked.connect(lambda: event5(d1))  # d1.close()
    d1.pushButton_2.clicked.connect(lambda: d2.show())
    ui.pushButton_2.clicked.connect(lambda: event3(ui))
    ui.pushButton_3.clicked.connect(lambda: event4())
    d2.pushButton.clicked.connect(lambda: event6(d2))
    sys.exit(app.exec_())

# create_gui()
