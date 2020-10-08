import networkx as nx
import linecache

def load_restribution(graph, load, failure_node_number, failed_list):
    # 更新load字典的值
    current_load = load[failure_node_number]
    print("当前失效节点负载为:" + str(current_load))
    # 存邻居节点的列表
    neighbors_nodes = [*graph.neighbors(failure_node_number)]
    neighbors_nodes = set(neighbors_nodes).difference(set(failed_list))
    print("邻居节点为: " + str(neighbors_nodes))
    # 求邻居节点的当前负载总和sum_neighbor_load
    sum_neighbor_load = 0.0
    for neighbors_node in neighbors_nodes:
        # 所有邻居节点负载总和sum_neighbor_load,也就是式子中的分母
        sum_neighbor_load += float(load[neighbors_node])
    # print("邻居节点总负载为: " + str(sum_neighbor_load))
    # 更新后的节点负载字典
    for neighbors_node in neighbors_nodes:
        load[neighbors_node] = load[neighbors_node] * (1 + float(current_load) / sum_neighbor_load)
    # print("更新后邻居节点负载为：")
    # for neighbors_node in neighbors_nodes:
    #     print(str(load[neighbors_node]) + " ")
    # 标记失效节点
    load[failure_node_number] = 'f'
    return load

def get_graph_info(graph, components_list, live_list):
    try:
        largest_components = max(nx.connected_components(G))
    except ValueError:
        components_list.append(0)
        print("当前图中最大联通子图节点数: " + str(0))
    else:
        largest_components = max(nx.connected_components(G))
        components_list.append(len(largest_components))
        print("当前图中最大联通子图节点数: " + str(len(largest_components)))
    live_num = graph.number_of_nodes()
    print("当前图中未失效节点数为: " + str(live_num))
    live_list.append(live_num)


# 级联失效主函数
def cascading_failure_node(graph, capacity_file, load_file, failure_node_number):
    # 存入load和capacity字典
    load = {}
    capacity = {}
    for i in range(1, stations_nums + 1):
        load[i] = float((linecache.getline(load_file, i).strip()))
        capacity[i] = float((linecache.getline(capacity_file, i).strip()))
    print("当前失效节点为：" + str(failure_node_number), end='\t')
    # 当前失效节点的负载，待分配负载
    load = load_restribution(graph, load, failure_node_number, [failure_node_number])
    # 删除失效节点
    graph.remove_node(failure_node_number)
    print("节点:" + str(nodes[failure_node_number - 1]) + "失效！信息已删除！")
    get_graph_info(graph, largest_components_list, not_fail_nodes)

    for ki in range(2, 51):
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
        for failed_node in failed_lists:
            load = load_restribution(graph, load, failed_node, failed_lists)
        for failed_node in failed_lists:
            graph.remove_node(failed_node)
            print("节点:" + str(nodes[failed_node - 1]) + "失效！信息已删除！")
        get_graph_info(graph, largest_components_list, not_fail_nodes)