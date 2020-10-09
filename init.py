import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


class SubwayGraph(nx.Graph):
    # 图中节点数
    node_num = 0
    # 图的OD三元组列表
    node_od = []
    # 节点load列表
    node_load = []
    # 图中最大度
    max_degree = 0
    # 归一化的度列表
    aver_degree_list = []
    # 失效容限列表
    failure_tolerance = []
    # 初始节点所含粒子数列表
    init_node_size_list = []
    # 图中最大介数中心性
    max_betweenness = 0
    # 归一化的介数中心性列表
    aver_betweenness_list = []
    # 节点capacity列表
    capacity_list = []
    # 最大联通子图节点数list
    largest_component_nodes = []
    # 参数 w
    w = 0
    # 参数 β
    b = 0
    # 参数 a
    a = 0

    def __init__(self, nums, w, b):
        super(SubwayGraph, self).__init__()
        self.node_num = nums
        self.w = w
        self.b = b

    def load_nodes(self):
        nodes = range(1, self.node_num)
        self.add_nodes_from(nodes)

    def load_edges(self, filename):
        edges = pd.read_csv(filename, sep=',', header=None)
        edgeLists = [tuple(xi) for xi in edges.values]
        self.add_edges_from(edgeLists)

    def load_OD(self, filename):
        loads = pd.read_csv(filename, sep=',', header=None)
        loadData = [tuple(li) for li in loads.values]
        loadList = []
        for ld in loadData:
            loadList.append(ld)
        self.node_od = loadList

    def show_graph(self):
        nx.draw_networkx(self)
        plt.show()

    def init_load(self):
        sumOD_list = []
        for i in range(1, self.node_num):
            sumOD = 0
            for node_load in self.node_od:
                if (node_load[0] == i) or (node_load[1] == i):
                    sumOD += node_load[2]
            sumOD_list.append(sumOD)
        maxLoad = max(sumOD_list)
        for load in sumOD_list:
            self.node_load.append(load / maxLoad)

    def init_capacity(self):
        raw_capacity_list = []
        for i in range(0, self.node_num - 1):
            raw_capacity_list.append(self.w * self.aver_degree_list[i] + (1 - self.w) * self.aver_betweenness_list[i])
        loadBalance = []
        for i in range(0, self.node_num - 1):
            loadBalance.append(self.node_load[i] / raw_capacity_list[i])
        self.a = max(loadBalance)
        for i in range(0, self.node_num - 1):
            self.capacity_list.append((1 + self.b) * self.a * raw_capacity_list[i])

    def init_largest_component_nodes_list(self):
        self.largest_component_nodes.append(self.number_of_nodes())

    def get_graph_degree(self):
        degreeList = []
        for number in range(1, self.node_num):
            degreeList.append(self.degree(number))
        # 网络最大度
        self.max_degree = max(degreeList)
        for degree in degreeList:
            self.aver_degree_list.append(degree / self.max_degree)

    def get_graph_betweeness(self):
        # 存放各站点介数中心性的字典
        score = nx.betweenness_centrality(self)
        # 求出最大的介数中心性
        self.max_betweenness = max(score.values())
        # 求Bi/Bmax
        for x in score.values():
            self.aver_betweenness_list.append(x / self.max_betweenness)

    # 初始失效容限
    def init_failure_tolerance(self):
        for number in range(1, self.node_num):
            self.failure_tolerance.append(self.degree(number) +
                                         (self.degree(number)
                                          * (1 - self.degree(number) / (2 * self.size()))) ** 0.5)

    # 模拟每个节点的初始粒子数
    def init_node_size(self):
        for number in range(1, self.node_num):
            self.init_node_size_list.append(self.degree(number))
        print("each node initial random_granule num list is:", self.init_node_size_list)


def write_txt(filename, data):
    # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print(filename + "文档保存成功!")


# 删除信息函数
def delete_txt(fileName):
    file = open(fileName, 'r+')
    file.truncate()
    print(fileName + "文档清空成功!")


def init_graph(G):
    G.load_edges('G.txt')
    G.load_nodes()
    G.load_OD('OD.txt')
    G.init_load()
    # write_txt('L.txt', G.node_load)
    G.get_graph_degree()
    G.get_graph_betweeness()
    G.init_capacity()
    G.init_failure_tolerance()
    G.init_node_size()
    G.init_largest_component_nodes_list()
    # write_txt('C.txt', G.capacity_list)
    # G.show_graph()
    # print("degree list is ", G.aver_degree_list, ", max degree is ", G.max_degree)
    # print("betweenness list is ", G.aver_betweenness_list, ", max betweenness is ", G.max_betweenness)
    # print("capacity list is ", G.capacity_list)
