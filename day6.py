import re
from collections import defaultdict
import numpy as np

# Part 1

points = [str(x) for x in open("./input/day6-input.txt").readlines()]
pt_num = 0
x_coord_dict = defaultdict(int)
y_coord_dict = defaultdict(int)

for pt in points:
    x_coord, y_coord = pt.split(", ")
    x_coord_dict[pt_num] += int(x_coord)
    y_coord_dict[pt_num] += int(y_coord)
    pt_num += 1

x_coord_max = max(x_coord_dict.values())
y_coord_max = max(y_coord_dict.values())

area_by_pt_num = defaultdict(int)
pt_array = [[0 for y in range(y_coord_max + 1)] for x in range(x_coord_max + 1)]

for x in range(x_coord_max):
    for y in range(y_coord_max):
        best_pt_index = -1
        best_distance = x_coord_max + y_coord_max

        for p in range(pt_num):
            current_distance = abs(x - x_coord_dict[p]) + abs(y - y_coord_dict[p])
            if current_distance < best_distance:
                best_distance = current_distance 
                best_pt_index = p
            elif current_distance == best_distance:
                best_pt_index = -1

        pt_array[x][y] = best_pt_index
        area_by_pt_num[best_pt_index] += 1      

for x in range(x_coord_max):
    area_by_pt_num[pt_array[x][0]] = 0
    area_by_pt_num[pt_array[x][y_coord_max]] = 0

for y in range(y_coord_max):
    area_by_pt_num[pt_array[0][y]] = 0
    area_by_pt_num[pt_array[x_coord_max][y]] = 0

print(max(area_by_pt_num.values()))

# Part 2

max_allowable_distance = 10000
allowable_point_count = 0

for x in range(x_coord_max):
    for y in range(y_coord_max):
        running_distance_total = 0
        for p in range(pt_num):     
            running_distance_total += abs(x - x_coord_dict[p])
            running_distance_total += abs(y - y_coord_dict[p])
            if running_distance_total >= max_allowable_distance:
                break
        if running_distance_total < max_allowable_distance:
            allowable_point_count += 1

print(allowable_point_count)