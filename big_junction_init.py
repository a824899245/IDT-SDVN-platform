import numpy as np
# import q_learning as ql
import re
import Global_Par as Gp
import math
adj_martix = [[0 for i in range(268)] for i in range(268)]
junction_position = [[0 for i in range(2)] for i in range(268)]
junction_distance = [[0 for i in range(268)] for i in range(268)]
num_segement_martix = [[0 for i in range(4)] for i in range(268)]
veh_segement_martix = [[[] for i in range(4)] for i in range(268)]
junction_vehicle = [[0 for i in range(0)] for i in range(268)]
chosen_edge = [[0 for i in range(268)] for i in range(268)]
edge_list = []
e_arrival_time = [Gp.MAX for i in range(600)]
junction_dp_weight = [[0 for i in range(268)] for i in range(268)]
junction_greedy_weight = [[0 for i in range(268)] for i in range(268)]
i_x = 0
i_y = 0
junction_la_position = [[0 for i in range(2)] for i in range(268)]

def rad(d):
    return d * 3.141592657 / 180.0


def getDistance(lat1, lng1, lat2, lng2):
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a/2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b/2), 2)))
    s = s * EARTH_REDIUS
    return s

EARTH_REDIUS = 6378.137


def inti():
    with open('1551.txt') as f:
        for line in f:
            line_list = re.split('\t', line)
            item_list = []
            for item in line_list:
                if item != '\n' and item != '':
                    item_list.append(float(item))
            if item_list[2] >= 0:
                junction_la_position[int(item_list[2])][0] = item_list[0]
                junction_la_position[int(item_list[2])][1] = item_list[1]
            if len(item_list) == 4:
                adj_martix[int(item_list[2])][int(item_list[3])] = 1
                adj_martix[int(item_list[3])][int(item_list[2])] = 1
            else:
                if len(item_list) == 5:
                    adj_martix[int(item_list[2])][int(item_list[3])] = 1
                    adj_martix[int(item_list[3])][int(item_list[2])] = 1
                    adj_martix[int(item_list[2])][int(item_list[4])] = 1
                    adj_martix[int(item_list[4])][int(item_list[2])] = 1
                else:
                    if len(item_list) == 6:
                        adj_martix[int(item_list[2])][int(item_list[3])] = 1
                        adj_martix[int(item_list[3])][int(item_list[2])] = 1
                        adj_martix[int(item_list[2])][int(item_list[4])] = 1
                        adj_martix[int(item_list[4])][int(item_list[2])] = 1
                        adj_martix[int(item_list[2])][int(item_list[5])] = 1
                        adj_martix[int(item_list[5])][int(item_list[2])] = 1
                    else:
                        if len(item_list) == 3 and item_list[2] < 0:
                            i_x = item_list[0]
                            i_y = item_list[1]

            print(item_list)

    for key, i in enumerate(junction_la_position):
        junction_position[key][1] = getDistance(i_x, i_y, i[0], i_y) * 1000
        junction_position[key][0] = getDistance(i_x, i_y, i_x, i[1]) * 1000

    for key_i, i in enumerate(junction_la_position):
        for key_j, j in enumerate(junction_la_position):
            a = getDistance(i[0], i[1], j[0], j[1]) * 1000
            junction_distance[key_i][key_j] = a
            junction_distance[key_j][key_i] = a
