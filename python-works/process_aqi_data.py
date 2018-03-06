# -*- coding: utf-8 -*-
# 处理原始的AQI数据
# 数据开始时间 2018/02/15 12

import numpy as np
import pandas as pd
import time
import csv


input_file_path = 'F:/Projects/Private/data/input'
output_file_path = ''


def read_station_ids():
    station_df = pd.read_csv(input_file_path + '/aqi_stations_detail_amap.csv', index_col=False)
    return np.array(station_df['id']).tolist()


def create_aqi_data(start_date, end_date):
    curr_date = start_date
    station_ids = read_station_ids()
    hours = hour_set()
    while curr_date < end_date:
        aqi_df = read_data_frame(curr_date)
        for i in range(len(hours)):
            hour = hours[i]
            # writer = csv.writer(open(output_file_path + time.strftime('/%Y_%m_%d/', curr_date) + hour + '.csv', encoding='utf-8'))
            # writer.writerow(['id', 'pm2.5', 'pm10', 'so2', 'no2', 'o3', 'co'])

            print(aqi_df[aqi_df['hour'] == 1])


            # for id in station_ids:
            #     print(aqi_df[id].iloc[1 + i * 15])
            #     print(aqi_df[id].iloc[3 + i * 15])
            #     print(aqi_df[id].iloc[5 + i * 15])
            #     print(aqi_df[id].iloc[7 + i * 15])
            #     print(aqi_df[id].iloc[9 + i * 15])
            #     print(aqi_df[id].iloc[13 + i * 15])
            #     break
            # print(i)
        # 时间增加24个小时
        curr_date = time.localtime(time.mktime(curr_date) + 24 * 60 * 60)


# 读取某一天的数据
def read_data_frame(date):
    return pd.read_csv(input_file_path + '/aqi/station/china_sites_' + time.strftime('%Y%m%d.csv', date))


# 创建时间集合
def hour_set():
    temp = []
    for i in range(24):
        if i // 10  == 0:
            temp.append(str(0) + str(i))
        else:
            temp.append(str(i))
    return temp


create_aqi_data(time.strptime('2018-02-15 00', '%Y-%m-%d %H'), time.strptime('2018-02-16 00', '%Y-%m-%d %H'))