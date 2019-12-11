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

start = ""
end = ""
distance = 0
file2 = # 書き込みたい路線データ
f2 = open(file2, "w")
stop_station_list = # 分岐駅では無いが、路線名が途中で変わる駅(神戸・金沢等)や、強制的に分割したい駅を入れる
for line in lines:
    line_data = line.split(",")
    if start == "":
        start = line_data[0]
    if (station_dict[line_data[1]] != 2) or (line_data[1] in stop_station_list):
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
f2.close()