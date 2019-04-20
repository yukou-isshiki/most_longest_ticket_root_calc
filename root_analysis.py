from graphillion import GraphSet as gs
import gc

def root_calc():
    filename = # 読み込みたいファイル名
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    univ = []
    for line in lines:
        dat = line.split(",")
        dat[2] = float(dat[2])
        edge = tuple(dat[0:3])
        univ.append(edge)
        del dat
        del edge
        gc.collect()
    w = gs.set_universe(univ)
    start = # 出発駅
    end = # 終着駅
    paths = gs.paths(start, end)
    del w
    gc.collect()
    for path in paths.min_iter():
        root_print(path, start, end)
        break

def root_print(path, search, end):
    another = ""
    for i in path:
        if search in i:
            root_list = list(i)
            print(root_list)
            path.remove(i)
            root_list.remove(search)
            another = root_list[0]
            break
        else:
            another = search
            continue
    if another != "":
        root_print(path, another, end)


if __name__ == '__main__':
    root_calc()