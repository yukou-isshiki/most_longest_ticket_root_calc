def change_station(station):
    if (station not in end_dict) == True:
        end_dict[station] = 1
    else:
        end_dict[station] = end_dict[station] + 1
    changed_station = f"{station}{end_dict[station]}"
    return changed_station, end_dict



file1 = # 読み込みたい路線データ
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

end_list = []

keys = [k for k, v in station_dict.items() if v > 2]
for key in keys:
    end_list.append(key)

start = ""
end = ""
distance = 0
file2 = # 書き込みたい路線データ
f2 = open(file2, "w")
stop_station_list = # 分岐駅では無いが、路線名が途中で変わる駅(神戸・金沢等)や、強制的に分割したい駅を入れる
end_dict = {}
for line in lines:
    line_data = line.split(",")
    if start == "":
        start = line_data[0]
    if (station_dict[line_data[1]] != 2) or (line_data[1] in stop_station_list) or (line_data[1] in end_list):
        end = line_data[1]
    if end == "":
        distance += float(line_data[2])
        distance = round(distance, 1)
    else:
        distance += round(float(line_data[2]),2)
        distance = round(distance, 1)
        if start in end_list:
            start, end_dict = change_station(start)
        if end in end_list:
            end, end_dict = change_station(end)
        print("{0},{1},{2}".format(start, end, distance))
        write_list = [start, end, str(distance)]
        write_line = ",".join(write_list)
        f2.write(write_line)
        f2.write("\n")
        start = ""
        end = ""
        distance = 0
f.close()

for end_station in end_list:
    limit = end_dict[end_station]
    for i in range(1, limit+1):
        write_list = [end_station, f"{end_station}{i}", "0.0"]
        write_line = ",".join(write_list)
        f2.write(write_line)
        f2.write("\n")
        write_list = ["ゴール", f"{end_station}{i}", "0.0"]
        write_line = ",".join(write_list)
        f2.write(write_line)
        f2.write("\n")

tail_list = [k for k, v in station_dict.items() if v == 1]

for tail in tail_list:
    write_list = ["ゴール", tail, "0.0"]
    write_line = ",".join(write_list)
    f2.write(write_line)
    f2.write("\n")

f2.close()