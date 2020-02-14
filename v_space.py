import Packet as Pkt
import Global_Par as Gp
import dij_test1 as dij
import networkx as nx
import v_jhmmtg
import v_jhmmtg_1
import v_jhmmtg_2
import v_jhmmtg_3
import v_jhmmtg_4
import v_jhmmtg_5
import junction_init as ji
import big_junction_init as bji
import math as m
import bf_test as bf
import jhmmtg as jh
import big_jhmmtg as bjh
import tgeaa as tg
import HRLB as hr
# import big_HRLB as bhr
import HMMM as hm
import time as tim
import random
import mcds

v_graph = nx.DiGraph()


def calibration(node_num, node_info_dict, time_interval):
    v_graph.clear()
    for i in range(0, node_num):
        for j in range(0, i):
            a = pow((node_info_dict[i][0][0] + node_info_dict[i][1][0] * time_interval) - (
                        node_info_dict[j][0][0] + node_info_dict[j][1][0] * time_interval), 2) + pow(
                (node_info_dict[i][0][1] + node_info_dict[i][1][1] * time_interval) - (
                            node_info_dict[j][0][1] + node_info_dict[j][1][1] * time_interval), 2)
            if a < pow(Gp.com_dis, 2):
                v_graph.add_edge(i, j, weight=a)
                v_graph.add_edge(j, i, weight=a)

def delay_cal(routing):
    delay = 0
    for i in range(len(routing)-1):
        if(v_graph.has_edge(routing[i],routing[i+1])):
            delay += v_graph[routing[i]][routing[i+1]]['weight']
        else:
            return -1
    return delay

def resolve_error(node_list, x_id, next_hop_id, des_id, node_num):
    choice = 0
    min = 10000000
    print()
    ## 原状
    reward = [[0 for i in range(80)] for i in range(80)]
    v_jhmmtg.junction_reward(reward, node_list[des_id].junction[0])
    h_s1, h_s2 = v_jhmmtg.hidden_seq_generate(reward, node_list[x_id].junction[0], node_list[des_id].junction[0])
    ji.e_arrival_time[x_id] = 0
    v_jhmmtg.hidden_to_obverse(x_id, des_id, node_list, h_s1)
    v_jhmmtg.hidden_to_obverse(x_id, des_id, node_list, h_s2)
    a, b = tg.earliest_arrival(ji.edge_list, x_id, des_id, node_num)
    route7 = []
    tg.s_routing(b, x_id, des_id, route7)
    a = delay_cal(route7)
    if a != -1 and len(route7)!=0:
        if a < min:
            min = a
            choice = 7
    v_jhmmtg.delete()

    ## 动规参数上涨
    reward = [[0 for i in range(80)] for i in range(80)]
    v_jhmmtg_1.junction_reward(reward, node_list[des_id].junction[0])
    h_s1, h_s2 = v_jhmmtg_1.hidden_seq_generate(reward, node_list[x_id].junction[0], node_list[des_id].junction[0])
    ji.e_arrival_time[x_id] = 0
    v_jhmmtg_1.hidden_to_obverse(x_id, des_id, node_list, h_s1)
    v_jhmmtg_1.hidden_to_obverse(x_id, des_id, node_list, h_s2)
    a, b = tg.earliest_arrival(ji.edge_list, x_id, des_id, node_num)
    route6 = []
    tg.s_routing(b, x_id, des_id, route6)
    a = delay_cal(route6)
    if a != -1 and len(route6)!=0:
        if a < min:
            min = a
            choice = 1
    v_jhmmtg_1.delete()
    ## 贪婪参数上涨
    reward = [[0 for i in range(80)] for i in range(80)]
    v_jhmmtg_2.junction_reward(reward, node_list[des_id].junction[0])
    h_s1, h_s2 = v_jhmmtg_2.hidden_seq_generate(reward, node_list[x_id].junction[0], node_list[des_id].junction[0])
    ji.e_arrival_time[x_id] = 0
    v_jhmmtg_2.hidden_to_obverse(x_id, des_id, node_list, h_s1)
    v_jhmmtg_2.hidden_to_obverse(x_id, des_id, node_list, h_s2)
    a, b = tg.earliest_arrival(ji.edge_list, x_id, des_id, node_num)
    route1 = []
    tg.s_routing(b, x_id, des_id, route1)
    a = delay_cal(route1)
    if a != -1:
        if a < min and len(route1)!=0:
            min = a
            choice = 2
    v_jhmmtg_2.delete()

    ## 密度参数上涨
    reward = [[0 for i in range(80)] for i in range(80)]
    v_jhmmtg_3.junction_reward(reward, node_list[des_id].junction[0])
    h_s1, h_s2 = v_jhmmtg_3.hidden_seq_generate(reward, node_list[x_id].junction[0], node_list[des_id].junction[0])
    ji.e_arrival_time[x_id] = 0
    v_jhmmtg_3.hidden_to_obverse(x_id, des_id, node_list, h_s1)
    v_jhmmtg_3.hidden_to_obverse(x_id, des_id, node_list, h_s2)
    a, b = tg.earliest_arrival(ji.edge_list, x_id, des_id, node_num)
    route2 = []
    tg.s_routing(b, x_id, des_id, route2)
    a = delay_cal(route2)
    if a != -1:
        if a < min and len(route2)!=0:
            min = a
            choice = 3
    v_jhmmtg_3.delete()

    ## 历史路由参数上涨
    reward = [[0 for i in range(80)] for i in range(80)]
    v_jhmmtg_4.junction_reward(reward, node_list[des_id].junction[0])
    h_s1, h_s2 = v_jhmmtg_4.hidden_seq_generate(reward, node_list[x_id].junction[0], node_list[des_id].junction[0])
    ji.e_arrival_time[x_id] = 0
    v_jhmmtg_4.hidden_to_obverse(x_id, des_id, node_list, h_s1)
    v_jhmmtg_4.hidden_to_obverse(x_id, des_id, node_list, h_s2)
    a, b = tg.earliest_arrival(ji.edge_list, x_id, des_id, node_num)
    route3 = []
    tg.s_routing(b, x_id, des_id, route3)
    a = delay_cal(route3)
    if a != -1:
        if a < min and len(route3)!=0:
            min = a
            choice = 4
    v_jhmmtg_4.delete()

    ## 错误节点删除
    reward = [[0 for i in range(80)] for i in range(80)]
    v_jhmmtg_5.junction_reward(reward, node_list[des_id].junction[0])
    h_s1, h_s2 = v_jhmmtg_5.hidden_seq_generate(reward, node_list[x_id].junction[0], node_list[des_id].junction[0])
    ji.e_arrival_time[x_id] = 0
    v_jhmmtg_5.hidden_to_obverse(x_id, des_id, node_list, h_s1, next_hop_id)
    v_jhmmtg_5.hidden_to_obverse(x_id, des_id, node_list, h_s2, next_hop_id)
    a, b = tg.earliest_arrival(ji.edge_list, x_id, des_id, node_num)
    route4 = []
    tg.s_routing(b, x_id, des_id, route4)
    a = delay_cal(route4)
    if a != -1:
        if a < min and len(route4)!=0:
            min = a
            choice = 5
    v_jhmmtg_4.delete()

    ## dijkstra
    # dijkstra
    try:
        dij.Dijkstra(v_graph, x_id, des_id)
    except nx.NetworkXError as err1:
        route = None
    else:
        route = dij.Dijkstra(v_graph, x_id, des_id)

    if route:
        print(route)
        with open('dijkstra.txt', 'a') as f:
            a = ""
            for i in route:
                a += str(i)
                a += ' '
            a += '\n'
            f.write(a)
            route5 = route
    else:
        route5 = [x_id, des_id]
    a = delay_cal(route5)
    if a != -1:
        if a < min and len(route5)!=0:
            min = a
            choice = 6

    if choice == 1:
        jh.alpha_martix[node_list[route[0]].big_junction][node_list[route[1]].big_junction] = 0.75
        return route6
    if choice == 2:
        jh.alpha_martix[node_list[route[0]].big_junction][node_list[route[1]].big_junction] = 0.25
        return route1
    if choice == 3:
        jh.k_i_martix[node_list[route[0]].big_junction][node_list[route[1]].big_junction] = 1.5
        return route2
    if choice == 4:
        jh.k_i_martix[node_list[route[0]].big_junction][node_list[route[1]].big_junction] = 0.5
        return route3
    if choice == 5:
        return route4
    if choice == 6:
        return route5
    if choice == 7:
        jh.alpha_martix[node_list[route[0]].big_junction][node_list[route[1]].big_junction] = 0.5
        jh.k_i_martix[node_list[route[0]].big_junction][node_list[route[1]].big_junction] = 1
        return route7
    return 1
        





