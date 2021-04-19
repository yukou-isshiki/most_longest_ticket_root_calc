from graphillion import GraphSet as gs
from decimal import Decimal
import gc
import read_root
import re

def set_graph(s_s, e_s, s_dict, file):
    univ = []
    weights = {}
    most_distance = Decimal("0.0")
    longest_root = ""
    start_number = ""
    end_number = ""
    with open(file) as f:
        for line in f:
            dat = line.split(",")
            dat[0] = s_dict[dat[0]]
            dat[1] = s_dict[dat[1]]
            edge = tuple(dat[0:2])
            univ.append(edge)
            weights[(dat[0],dat[1])] = float(dat[2].replace("\n", ""))
            del dat
            del edge
            gc.collect()
    f.close()
    del f
    gc.collect()
    gs.set_universe(univ)
    if s_s != "スタート" and e_s != "ゴール":
        s = s_dict[s_s]
        start_number = s
        e = s_dict[e_s]
        end_number = e
        longest_root = root_calc(s, e, weights)
        most_distance = calc_distance(longest_root, weights)
    elif s_s != "スタート":
        s = s_dict[s_s]
        start_number = s
        for e_key in s_dict:
            e = s_dict[e_key]
            if s == e:
                continue
            max_path = root_calc(s, e, weights)
            distance = calc_distance(max_path, weights)
            if most_distance < distance:
                most_distance = distance
                longest_root = max_path
                end_number = e
    elif e_s != "ゴール":
        e = s_dict[e_s]
        end_number = e
        for s_key in s_dict:
            s = s_dict[s_key]
            if s == e:
                continue
            max_path = root_calc(s, e, weights)
            distance = calc_distance(max_path, weights)
            if most_distance < distance:
                most_distance = distance
                longest_root = max_path
                start_number = s
    else:
        station_list = []
        for s_key in s_dict:
            s = s_dict[s_key]
            station_list.append(s)
            for e_key in s_dict:
                e = s_dict[e_key]
                if e in station_list:
                    continue
                max_path = root_calc(s, e, weights)
                if max_path == []:
                    continue
                distance = calc_distance(max_path, weights)
                if most_distance < distance:
                    most_distance = distance
                    longest_root = max_path
                    start_number = s
                    end_number = e
    return longest_root, most_distance, start_number, end_number

def root_calc(start, end, weights):
    paths = gs.paths(start, end)
    print(start, end)
    try:
        max_path = next(paths.max_iter(weights))
    except StopIteration:
        max_path = []
        print(start, end, "pass")
    return max_path

def calc_distance(path, weights):
    distance = Decimal("0.0")
    for edge in path:
        distance += Decimal(str(weights[edge]))
    return distance

def root_print(path, search, end, station_dict, root_list):
    another = ""
    for i in path:
        if search in i:
            if search == i[0]:
                station = get_keys_from_value(station_dict, i[0])[0]
            else:
                station = get_keys_from_value(station_dict, i[1])[0]
            if re.search("[0-9]", station[-1]) == None:
                root_list.append(station)
            root_list_old = list(i)
            path.remove(i)
            root_list_old.remove(search)
            another = root_list_old[0]
            break
        else:
            another = search
            continue
    if another != "":
        root_print(path, another, end, station_dict, root_list)
    return root_list

def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]



if __name__ == '__main__':
    start = # 出発駅
    end = # 終着駅
    filename = # 読み込みたいファイル名
    station_dict = read_root.dict_create(filename)
    print(station_dict)
    root, distance, s_number, e_number = set_graph(start, end, station_dict, filename)
    creat_list = root_print(root, s_number, e_number, station_dict, [])
    end_station = [k for k, v in station_dict.items() if v == e_number]
    if re.search("[0-9]", end_station[0][-1]) != None:
        creat_list.append(end_station[0][:-1])
    else:
        creat_list.append(end_station[0])
    most_longest_root = "→".join(creat_list)
    print(most_longest_root)
    print(f"総距離{distance}km")