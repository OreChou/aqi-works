# -*- coding: utf-8 -*-
# 处理全国监测站所抓取的数据成训练样本
# 数据开始时间 2018/02/15 12


import pandas as pd
import time


input_file_path = '/Users/orechou/Desktop/Paper_Work/data/process/amap'
output_file_path = ''


# 读取高德地图的气象说明
def read_amap_weather_dictionary():
    file = open(input_file_path + '/amap_weather_dictionary', encoding='utf-8')
    dictionary = {}
    for line in file:
        contents = line.strip('\n').split(' ')
        dictionary[contents[1]] = int(contents[0]) + 1
    dictionary['-1'] = 0
    return dictionary


amap_weather_dictionary = read_amap_weather_dictionary()


# 根据传入的时间段，生成相应的数据文件
def create_record_file(start_time, end_time):
    curr_time = start_time
    # 获取不变的数据

    # 获取实时的数据
    while curr_time < end_time:
        try:
            file_name = time.strftime('%Y_%m_%d/%H', curr_time)
            weather_df = pd.read_csv(input_file_path + '/weather/' + file_name + '.csv')
            weather_owm_df = pd.read_csv(input_file_path + '/pressure/' + file_name + '.csv')
            traffic_df = pd.read_csv(input_file_path + '/traffic/' + file_name + '.csv')
            events_df = pd.read_csv(input_file_path + '/events/' + file_name + '.csv')
            for i in range(1576):
                weather = weather_df.iloc[i]
                weather_owm = weather_owm_df.iloc[i]
                traffic = traffic_df.iloc[i]
                event = events_df.iloc[i]
                print(gen_weather_amap_row_data(weather) + ' ' + gen_weather_owm_row_data(weather_owm) + ' ' + gen_traffic_row_data(traffic) + ' ' + gen_event_row_data(event))
            # 时间增加一个小时
            curr_time = time.localtime(time.mktime(curr_time) + 60 * 60)
        except Exception as e:
            print('异常发生 -> ' + str(e))
            break


def gen_weather_amap_row_data(item):
    return str(amap_weather_dictionary[item['weather']]) + ' ' + \
           str(item['temperature']) + ' ' + \
           str(item['windpower']).strip('≤') + ' ' + \
           str(item['humidity'])


def gen_weather_owm_row_data(item):
    return str(item['pressure']) + ' ' + str(item['visibility'])


def gen_traffic_row_data(item):
    if str(item['expedite']) == '0' and str(item['congested']) == '0' and str(item['blocked']) == '0' and str(item['unknown'] == '0'):
        return '100 0 0 0'
    return str(item['expedite']).strip('%') + ' ' + \
           str(item['congested']).strip('%') + ' ' + \
           str(item['blocked']).strip('%') + ' ' + \
           str(item['unknown']).strip('%')


def gen_event_row_data(item):
    return str(item['numbers'])


create_record_file(time.strptime('2018-02-18 00', '%Y-%m-%d %H'), time.strptime('2018-02-18 03', '%Y-%m-%d %H'))
