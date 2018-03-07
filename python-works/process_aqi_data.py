# -*- coding: utf-8 -*-
# 处理原始的AQI数据
# 数据开始时间 2018/02/15 12
# windows: F:/Projects/Private/data/input
# mac:
# hard-drive: /Volumes/SAMSUNG/

import numpy as np
import pandas as pd
import time
import csv
import os

hard_drive_input_path = '/Volumes/SAMSUNG/input'
hard_drive_output_path = '/Volumes/SAMSUNG/output'

input_file_path = hard_drive_input_path
output_file_path = hard_drive_output_path


def read_station_ids():
    station_df = pd.read_csv(input_file_path + '/aqi_stations_detail_amap.csv', index_col=False)
    return np.array(station_df['id']).tolist()


def create_aqi_data(start_date, end_date):
    curr_date = start_date
    station_ids = read_station_ids()
    hours = hour_set()
    while curr_date < end_date:
        # 创建属于该日期的文件夹
        create_dir_if_not_exist(output_file_path + time.strftime('/aqi/station/%Y_%m_%d/', curr_date))
        # 将缺失数据用0填充
        aqi_df = read_data_frame(curr_date).fillna(value=0)
        for i in range(len(hours)):
            hour = hours[i]
            writer = csv.writer(open(output_file_path + time.strftime('/aqi/station/%Y_%m_%d/', curr_date) + hour + '.csv', mode='a+', encoding='utf-8'))
            writer.writerow(['id', 'pm2.5', 'pm10', 'so2', 'no2', 'o3', 'co'])
            # 若长度为0则说明没有数据
            aqi_hour_df = aqi_df[aqi_df['hour'] == i]
            if not len(aqi_hour_df) == 0:
                for id in station_ids:
                    writer.writerow([id,
                                     aqi_hour_df[id].iloc[1],
                                     aqi_hour_df[id].iloc[3],
                                     aqi_hour_df[id].iloc[5],
                                     aqi_hour_df[id].iloc[7],
                                     aqi_hour_df[id].iloc[9],
                                     aqi_hour_df[id].iloc[13]])
        # 时间增加24个小时
        print('完成 ' + time.strftime('%Y%m%d', curr_date) + ' 数据的处理')
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


def create_dir_if_not_exist(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


create_aqi_data(time.strptime('2018-02-15 00', '%Y-%m-%d %H'), time.localtime(time.time()))
