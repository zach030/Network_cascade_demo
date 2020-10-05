import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


class SubwayGraph(nx.Graph):
    # 图中节点数
    nodeNum = 0
    # 图的OD三元组列表
    nodeOD = []
    # 节点load列表
    nodeLoad = []
    # 图中最大度
    maxDegree = 0
    # 归一化的度列表
    averDegreeList = []
    # 图中最大介数中心性
    maxBetweenness = 0
    # 归一化的介数中心性列表
    averBetweennessList = []
    # 节点capacity列表
    capacityList = []
    # 参数 w
    w = 0
    # 参数 β
    b = 0
    # 参数 a
    a = 0

    def __init__(self, nums, w, b):
        super(SubwayGraph, self).__init__()
        self.nodeNum = nums
        self.w = w
        self.b = b

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

    def initLoad(self):
        sumOD_list = []
        for i in range(1, self.nodeNum):
            sumOD = 0
            for node_load in self.nodeOD:
                if (node_load[0] == i) or (node_load[1] == i):
                    sumOD += node_load[2]
            sumOD_list.append(sumOD)
        maxLoad = max(sumOD_list)
        for load in sumOD_list:
            self.nodeLoad.append(load / maxLoad)

    def initCapacity(self):
        rawCapacityList = []
        for i in range(0, self.nodeNum - 1):
            rawCapacityList.append(self.w * self.averDegreeList[i] + (1 - self.w) * self.averBetweennessList[i])
        loadBalance = []
        for i in range(0, self.nodeNum - 1):
            loadBalance.append(self.nodeLoad[i] / rawCapacityList[i])
        self.a = max(loadBalance)
        for i in range(0, self.nodeNum - 1):
            self.capacityList.append((1 + self.b) * self.a * rawCapacityList[i])

    def getGraphDegree(self):
        degreeList = []
        for number in range(1, self.nodeNum):
            degreeList.append(self.degree(number))
        # 网络最大度
        self.maxDegree = max(degreeList)
        for degree in degreeList:
            self.averDegreeList.append(degree / self.maxDegree)

    def getGraphBetweenness(self):
        # 存放各站点介数中心性的字典
        score = nx.betweenness_centrality(self)
        # 求出最大的介数中心性
        self.maxBetweenness = max(score.values())
        # 求Bi/Bmax
        for x in score.values():
            self.averBetweennessList.append(x / self.maxBetweenness)


def writeTxt(filename, data):
    # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print(filename + "文档保存成功!")

# 删除信息函数
def deleteTxt(fileName):
    file = open(fileName, 'r+')
    file.truncate()
    print(fileName + "文档清空成功!")

if __name__ == '__main__':
    G = SubwayGraph(11, 0.5, 0.2)
    G.loadEdges('G.txt')
    G.loadNodes()
    G.loadOD('OD.txt')
    G.initLoad()
    writeTxt('L.txt', G.nodeLoad)
    G.getGraphDegree()
    G.getGraphBetweenness()
    G.initCapacity()
    writeTxt('C.txt', G.capacityList)
    G.showGraph()
    print("degree list is ", G.averDegreeList, ", max degree is ", G.maxDegree)
    print("betweenness list is ", G.averBetweennessList, ", max betweenness is ", G.maxBetweenness)
    print("capacity list is ", G.capacityList)
