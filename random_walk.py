import random

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import networkx as nx


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


def update(num):
    ax.clear()

    # Background nodes
    null_nodes = nx.draw_networkx_nodes(G, pos=pos, nodelist=set(G.nodes()), node_color="white", ax=ax)
    null_nodes.set_edgecolor("black")
    nx.draw_networkx_edges(G, pos=pos, ax=ax, edge_color="gray")

    nx.draw_networkx_labels(G, pos=pos, font_color="black", ax=ax)
    nx.draw_networkx_nodes(G, pos=pos, nodelist=[seed], node_color='red', ax=ax)

    for step_i in range(1, num):
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[path[step_i - 1]], node_color='lightcoral', ax=ax)
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[path[step_i]], node_color='red', ax=ax)
        nx.draw_networkx_edges(G, pos=pos, edgelist=[(path[step_i - 1], path[step_i])], width=2., ax=ax)

        # Scale plot ax
        ax.set_title("Frame %d" % step_i, fontweight="bold")
        ax.set_xticks([])
        ax.set_yticks([])

    nx.draw_networkx_nodes(G, pos=pos, nodelist=[path[0]], node_color='blue', ax=ax)
    plt.axis('off')


G = nx.Graph()
steps = 10
seed = []
pos = {}
path = []
# Build plot
fig, ax = plt.subplots(figsize=(8, 6))
plt.axis('off')


def subwayRandomWalker(Graph):
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
        print("Graph seed is:\n", seed)
        for k in range(1, G.initNodeSizeList[i-1] + 1):
            path = random_weighted_walk(G, seed, steps)
            print("no." + str(k) + " random node path is:")
            print(path)
            AllPath.append(path)
    print(AllPath)
    # for size in AllPath:

    currentLoad = {}
    # {"1":2,"2":,......} 再与initNodeSizeList进行比较
    ani = animation.FuncAnimation(fig, update, frames=len(path), interval=1000, repeat=True)
    plt.show()
