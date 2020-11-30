import random

import networkx as nx

from utils.animated_random_walk import *

G = nx.Graph()
steps = 50
seed = []
pos = {}
path = []


# 对一个节点的一个粒子的行走路径
def random_weighted_walk(G, initial_node, steps):
    walk_list = [initial_node]
    prob_list = []
    for i in range(steps):
        for node in G.neighbors(walk_list[i]):
            for node_multiply in range(G.degree(node)):
                prob_list.append(node)
        walk_list.append(random.choice(prob_list))
        prob_list = []
    return walk_list


def subway_random_walker(Graph):
    global G
    G = Graph
    global pos
    pos = nx.spring_layout(G)
    # 起始节点
    global path
    global seed
    AllPath = []
    # 10个节点多个粒子同时行走得到list
    for i in range(1, G.number_of_nodes() + 1):
        seed = i
        # print("Graph initial seed is:\n", seed)
        for k in range(1, G.init_node_size_list[i - 1] + 1):
            # 遍历一个节点的所有粒子
            path = random_weighted_walk(G, seed, steps)
            # 所有的粒子走50步的结果list
            AllPath.append(path)
    print(AllPath)
    # 当前时间步下所有粒子的分布list
    currentGraphLoad = {}  # key:时间步，value：所有粒子分布的list
    # 当前时间步下每个节点的粒子数负载list
    currentNodeLoad = {}  # 当前时间步下：key:图节点 value：此节点上的粒子数
    # 初始失效节点list
    initialFailureList = []
    for k in range(0, steps):  # 依据步数进行遍历
        currentNode = []  # 当前时间步下：粒子分布情况的list
        for size in AllPath:
            currentNode.append(size[k])
        # print(currentNode)
        currentGraphLoad[k] = currentNode
        for j in range(1, G.number_of_nodes() + 1):
            currentNodeLoad[j] = currentNode.count(j)  # 统计此时间步下，每个节点的粒子数
        print("step " + str(k) + ": each node contain granule num dict is: ")
        print(currentNodeLoad)
        for node, load in currentNodeLoad.items():
            if G.failure_tolerance[node - 1] < load:
                initialFailureList.append(node)
        if len(initialFailureList) != 0:
            print("Find node failed, got failed node list !")
            break
    return initialFailureList
