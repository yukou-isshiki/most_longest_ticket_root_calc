from graphillion import GraphSet as gs
import gc
import read_root


def root_calc(start, end, station_dict, filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    univ = []
    for line in lines:
        dat = line.split(",")
        dat[0] = station_dict[dat[0]]
        dat[1] = station_dict[dat[1]]
        dat[2] = float(dat[2])
        edge = tuple(dat[0:3])
        univ.append(edge)
        del dat
        del edge
        gc.collect()
    w = gs.set_universe(univ)
    start = station_dict[start]
    end = station_dict[end]
    paths = gs.paths(start, end)
    for path in paths.max_iter():
        break
    return path

def root_print(path, search, end, station_dict, root_list):
    another = ""
    for i in path:
        if search in i:
            if search == i[0]:
                station = get_keys_from_value(station_dict, i[0])[0]
                root_list.append(station)
            elif search == i[1]:
                station = get_keys_from_value(station_dict, i[1])[0]
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
    path = root_calc(start, end, station_dict, filename)
    start_number = station_dict[start]
    end_number = station_dict[end]
    root_list = []
    creat_list = root_print(path, start_number, end_number, station_dict, root_list)
    creat_list.append(end)
    most_longest_root = "→".join(creat_list)
    print(most_longest_root)