# JRの最長経路を出すためのプログラム

* (現在書き換え作業中)

1.はじめに

このスクリプトはJRの旅客営業規則に基づき、最も長い経路を算出するためのスクリプトです。

スクリプトには、経路を算出する"read_root.py"と全駅データから計算用のデータを作成する"*railway_data_create.py"があります。

最低限必要な計算用データを"graphillion_data"ディレクトリに格納してあります。

JR全線(貨物専用線を除く)の全駅間データは"all_line_data"ディレクトリに格納しています。



(以下作業前の状態)

all_line_data JR全線全駅の駅間データを格納(2020年3月ダイヤ改正・5月札沼線部分廃線対応)

graphillion_data 上記のデータからgraphillion解析用に生成したデータ

root_analysis.py 計算プログラム本体

read_root.py 駅名をid変換する(メモリー削減目的)

railway_data_create.py 通常の路線生成プログラム

start_railway_data_create.py 開始地点を含む路線生成プログラム

end_railway_data_create.py 終端地点を含む路線生成プログラム



GCP Comute Engine n1-highmem-96（96 vCPU、メモリ 624 GB）で動作検証済

※ (2019/12/11現在、九州の路線データのみ上記でもメモリ不足で計算出来ず…)

 無改変での第三者への配布はおやめ下さい