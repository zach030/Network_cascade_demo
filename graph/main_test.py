from graph.subway_graph import *
from utils.animated_random_walk import *
from utils.cascade import *


def Start():
    # 建立地铁网络模型
    G = SubwayGraph()  # 增加总粒子数作为入参
    G.init_subway_graph(10, 0.5, 0, 28)
    # 初始化网络数据
    init_graph_manual(G)
    # 随机行走模拟网络失效
    init_failure = subway_random_walker(G)
    # 网络级联失效
    cascading_failure_node(G, '../data/C.txt', '../data/L.txt', init_failure)
    print("\n最大联通子图节点数变化list:", "\t")
    print(G.largest_component_nodes)
    print("剩余存活节点数变化list:", "\t")
    print(G.active_nodes)
    write_txt('cascade.txt', G.active_nodes)


if __name__ == '__main__':
    Start()
