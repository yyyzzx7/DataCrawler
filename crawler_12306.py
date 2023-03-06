# @Time    : 28/2/2023 17:21
# @Author  : chrisyuhimself@gmail.com

import requests
import json
import datetime


def get_response(date, from_station_code, to_station_code):
    """
    Get and Process 12306 ticket query response
    :param date: train_date
    :param from_station_code:
    :param to_station_code:
    :return: json format
    """
    params = {
        "leftTicketDTO.train_date": date,
        "leftTicketDTO.from_station": from_station_code,
        "leftTicketDTO.to_station": to_station_code,
        "purpose_codes": "ADULT"
    }
    url = "https://kyfw.12306.cn/otn/leftTicketPrice/queryAllPublicPrice"
    res = requests.get(url, params=params)
    return json.loads(res.text).get("data")


date = datetime.datetime.today()
date = date.strftime("%Y-%m-%d")

# 1. Hong Kong as from_station
from_station_code = 'XJA'
to_station_code_list = ['NZQ', 'IOQ', 'DNA', 'RTQ', 'IMQ', 'IUQ', 'QSQ', 'GGQ', 'IZQ']

for to_station_code in to_station_code_list:
    get_response(date, from_station_code, to_station_code)

# 2. Hong Kong as to_station
from_station_code_list = ['NZQ', 'IOQ', 'DNA', 'RTQ', 'IMQ', 'IUQ', 'QSQ', 'GGQ', 'IZQ']
to_station_code = 'XJA'
for from_station_code in from_station_code_list:
    get_response(date, from_station_code, to_station_code)
