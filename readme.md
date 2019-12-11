# JRの最長経路を出すためのプログラム

all_line_data JR全線全駅の駅間データを格納(2019年11月ダイヤ改正対応)

graphillion_data 上記のデータからgraphillion解析用に生成したデータ

root_analysis.py 計算プログラム本体

read_root.py 駅名をid変換する(メモリー削減目的)

railway_data_create.py 通常の路線生成プログラム

start_railway_data_create.py 開始地点を含む路線生成プログラム

end_railway_data_create.py 終端地点を含む路線生成プログラム



GCP Comute Engine n1-highmem-96（96 vCPU、メモリ 624 GB）で動作検証済

※ (2019/12/11現在、九州の路線データのみ上記でもメモリ不足で計算出来ず…)

 無改変での第三者への配布はおやめ下さい