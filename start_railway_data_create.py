erea = ""
file1 = f"all_line_data/{erea}_all_line_data.txt"
f = open(file1, "r")
lines = f.readlines()
station_dict = {}
for line in lines:
    line_data = line.split(",")
    for i in range(0,2):
        if line_data[i] not in station_dict:
            station_dict[line_data[i]] = 1
        else:
            station_dict[line_data[i]] = station_dict[line_data[i]] + 1

start_list = []

# 分岐駅と隣駅でも分割する
for line in lines:
    line_data = line.split(",")
    if station_dict[line_data[0]] > 2:
        if (line_data[1] not in start_list) and (station_dict[line_data[1]] == 2):
            start_list.append(line_data[1])
    elif station_dict[line_data[1]] > 2:
        if (line_data[0] not in start_list) and (station_dict[line_data[0]] == 2):
            start_list.append(line_data[0])


start = ""
end = ""
distance = 0
file2 = f"graphillion_data/{erea}_start_graphillion.txt"
f2 = open(file2, "w")
stop_station_list = [] # 分岐駅では無いが、路線名が途中で変わる駅(神戸・金沢等)や、強制的に分割したい駅をリスト形式で入れる
for line in lines:
    line_data = line.split(",")
    if start == "":
        start = line_data[0]
    if (station_dict[line_data[1]] != 2) or (line_data[1] in stop_station_list) or (line_data[1] in start_list):
        end = line_data[1]
    if end == "":
        distance += float(line_data[2])
        distance = round(distance, 1)
    else:
        distance += round(float(line_data[2]),2)
        distance = round(distance, 1)
        print("{0},{1},{2}".format(start, end, distance))
        write_list = [start, end, str(distance)]
        write_line = ",".join(write_list)
        f2.write(write_line)
        f2.write("\n")
        start = ""
        end = ""
        distance = 0
f.close()

keys = [k for k, v in station_dict.items() if v == 1]
for key in keys:
    write_list = ["スタート", key, "0.0"]
    write_line = ",".join(write_list)
    f2.write(write_line)
    f2.write("\n")

for start_station in start_list:
    write_list = ["スタート", start_station, "0.0"]
    write_line = ",".join(write_list)
    f2.write(write_line)
    f2.write("\n")
f2.close()