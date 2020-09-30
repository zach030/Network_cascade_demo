import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


class SubwayGraph(nx.Graph):
    nodeNum = 0
    nodeOD = []
    nodeLoad = []

    def __init__(self, nums):
        super(SubwayGraph, self).__init__()
        self.nodeNum = nums

    def loadNodes(self):
        nodes = range(1, self.nodeNum)
        self.add_nodes_from(nodes)

    def loadEdges(self, filename):
        edges = pd.read_csv(filename, sep=',', header=None)
        edgeLists = [tuple(xi) for xi in edges.values]
        self.add_edges_from(edgeLists)

    def loadOD(self, filename):
        loads = pd.read_csv(filename, sep=',', header=None)
        loadData = [tuple(li) for li in loads.values]
        loadList = []
        for ld in loadData:
            loadList.append(ld)
        self.nodeOD = loadList

    def showGraph(self):
        nx.draw_networkx(self)
        plt.show()

    def calcLoad(self):
        sumOD_list = []
        for i in range(1, self.nodeNum):
            sumOD = 0
            for node_load in self.nodeOD:
                if (node_load[0] == i) or (node_load[1] == i):
                    sumOD += node_load[2]
            sumOD_list.append(sumOD)
        maxLoad = max(sumOD_list)
        for load in sumOD_list:
            self.nodeLoad.append(load/maxLoad)


def writeTxt(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print(filename + "文件保存成功!")


if __name__ == '__main__':
    G = SubwayGraph(11)
    G.loadEdges('G.txt')
    G.loadNodes()
    G.loadOD('OD.txt')
    G.calcLoad()
    writeTxt('L.txt', G.nodeLoad)
