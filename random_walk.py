import networkx as nx
import random
from animated_random_walk import *

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
            path = random_weighted_walk(G, seed, steps)
            # print("no." + str(k) + " random node path is:")
            # print(path)
            AllPath.append(path)
    # print(len(AllPath))
    # 当前时间步下所有粒子的分布list
    currentGraphLoad = {}
    # 当前时间步下每个节点的粒子数负载list
    currentNodeLoad = {}
    # 初始失效节点list
    initialFailureList = []
    for k in range(0, 10):
        currentNode = []
        for size in AllPath:
            currentNode.append(size[k])
        currentGraphLoad[k] = currentNode
        for j in range(1, 11):
            currentNodeLoad[j] = currentNode.count(j)
        print("step " + str(k) + ": each node contain granule num dict is: ")
        print(currentNodeLoad)
        for node, load in currentNodeLoad.items():
            if G.init_node_size_list[node - 1] < load:
                initialFailureList.append(node)
        if len(initialFailureList) != 0:
            print("Find node failed, got failed node list !")
            break
    # print("initial failure node list is :")
    # print(initialFailureList)
    return initialFailureList
