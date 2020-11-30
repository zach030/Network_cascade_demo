import linecache

import networkx as nx


def load_restribution(graph, load, capacity, failure_node_number, failed_list):
    # 更新load字典的值
    current_load = load[failure_node_number]
    print("当前失效节点: " + str(failure_node_number) + ", 负载为: " + str(current_load))
    # 存邻居节点的列表
    neighbors_nodes = [*graph.neighbors(failure_node_number)]
    neighbors_nodes = set(neighbors_nodes).difference(set(failed_list))
    print("该失效邻居节点为: " + str(neighbors_nodes))
    # 如果不存在邻居节点,则直接return
    if len(neighbors_nodes) == 0:
        print("该节点已无邻居节点")
        load[failure_node_number] = 'f'
        return load
    # 求邻居节点的当前容量总和 sum_neighbor_capacity
    sum_neighbor_capacity = 0.0
    for neighbors_capacity in neighbors_nodes:
        # 所有邻居节点负载总和sum_neighbor_load,也就是式子中的分母
        print("邻居节点: " + str(neighbors_capacity) + " 容量为:" + str(capacity[neighbors_capacity]))
        sum_neighbor_capacity += float(capacity[neighbors_capacity])
    print("邻居节点总容量为: " + str(sum_neighbor_capacity))
    # 更新后的节点负载字典
    for neighbors_node in neighbors_nodes:
        load[neighbors_node] = load[neighbors_node] * (
                    1 + graph.capacity_list[neighbors_node - 1] / sum_neighbor_capacity)
    print("更新后邻居节点负载为：")
    for neighbors_node in neighbors_nodes:
        print(str(load[neighbors_node]) + " ")
    # 标记失效节点
    load[failure_node_number] = 'f'
    return load


def get_graph_info(graph, components_list, live_list):
    try:
        largest_components = max(nx.connected_components(graph))
    except ValueError:
        components_list.append(0)
        print("当前图中最大联通子图节点数: " + str(0))
    else:
        largest_components = max(nx.connected_components(graph))
        components_list.append(len(largest_components))
        print("当前图中最大联通子图节点数: " + str(len(largest_components)))
    live_num = graph.number_of_nodes()
    print("当前图中未失效节点数为: " + str(live_num))
    live_list.append(live_num)
    print("当前节点失效流程已结束")


# 级联失效主函数
def cascading_failure_node(graph, capacity_file, load_file, failure_node_list):
    # 存入load和capacity字典
    load = {}
    capacity = {}
    # 加载load以及capacity字典
    for i in range(1, graph.number_of_nodes() + 1):
        load[i] = float((linecache.getline(load_file, i).strip()))
        capacity[i] = float((linecache.getline(capacity_file, i).strip()))
    print("初始失效节点列表为：")
    print(failure_node_list)
    # 当前失效节点的负载，待分配负载
    for i in range(0, len(failure_node_list)):
        load = load_restribution(graph, load, capacity, failure_node_list[i], failure_node_list)
        # 删除失效节点
        graph.remove_node(failure_node_list[i])
        print("节点:" + str([failure_node_list[i]]) + "失效！信息已删除！")
    get_graph_info(graph, graph.largest_component_nodes, graph.active_nodes)
    print("第一级初始节点列表失效仿真结束！")
    for ki in range(2, 11):
        print("---------------第" + str(ki) + "级失效！--------------")
        # 检查load字典
        failed_lists = []
        neighbors_judge = {}
        for key, values in load.items():
            if values != 'f':
                neighbors_judge[key] = float(capacity[key]) - float(load[key])
                if neighbors_judge[key] < 0:
                    print("第" + str(key) + "号节点失效！")
                    failed_lists.append(key)
        if len(failed_lists) != 0:
            for failed_node in failed_lists:
                load = load_restribution(graph, load, capacity, failed_node, failed_lists)
            for failed_node in failed_lists:
                graph.remove_node(failed_node)
                print("节点:" + str(failed_node) + "失效！信息已删除！")
        else:
            print("本级无失效节点")
        get_graph_info(graph, graph.largest_component_nodes, graph.active_nodes)
        print("当前剩余节点:", graph.nodes())
