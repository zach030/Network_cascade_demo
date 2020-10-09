from Animated_Random_Walk import *
from cascade import *
from init import *

if __name__ == '__main__':
    # 建立地铁网络模型
    G = SubwayGraph(11, 0.5, 0.2)
    # 初始化网络数据
    initGraph(G)
    # 随机行走模拟网络失效
    init_failure = subwayRandomWalker(G)
    print(init_failure[0])
    cascading_failure_node(G, 'C.txt', 'L.txt', init_failure[0])
