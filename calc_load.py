import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
# def readTxtFile():
#     G.add_nodes_from()


if __name__ == '__main__':
    G = nx.Graph()
    nodesList = range(1, 11)
    # 读节点
    G.add_nodes_from(nodesList)
    edges = pd.read_csv('G.txt', sep=',', header=None)
    edge_lists = [tuple(xi) for xi in edges.values]
    # 读边
    for edge_list in edge_lists:
        G.add_edge(*edge_list)
    nx.draw_networkx(G)
    plt.show()
