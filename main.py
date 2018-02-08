#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 21:11
# @Author  : Mat
# @Email   : mat_wu@163.com
# @File    : main.py
# @Software: PyCharm

import requests


def check():
    response = requests.get('https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-29&leftTicketDTO.from_station=XMS&leftTicketDTO.to_station=CEH&purpose_codes=ADULT')

    result = response.json()
    return result['data']['result']

j=0
'''
3=车次
8=出发时间
9=到达时间
10=历史
26=无座
30=二等座
31=一等座

'''

for i in check():
    tmp_list=i.split('|')
    if tmp_list[31]=='无' or tmp_list[31]=='':
        print(tmp_list[3],"该车次没有1等票")
    else:
        print(tmp_list[3],'该车次1等票有余票{}张'.format(tmp_list[31]))