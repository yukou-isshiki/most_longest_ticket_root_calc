def dict_create(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    station_dict = {}
    i = 1
    for line in lines:
        data = line.split(",")
        for j in range(0, 2):
            station = data[j]
            if (station not in station_dict) == True:
                station_dict[station] = i
                i += 1
    return station_dict
