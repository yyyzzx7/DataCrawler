# @Time    : 28/2/2023 17:03
# @Author  : chrisyuhimself@gmail.com

import requests
import numpy as np

# Crawling station code
url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9236"
html = requests.get(url)
data = html.text.encode(html.encoding).decode('utf-8')
station_dict = {}
for item in data.split("@")[1:]:
    name = item.split("|")[1]
    code = item.split("|")[2]
    print(name, code, sep=",")
    station_dict[name] = code

np.save("station_dict.npy", station_dict)

# Get Hong Kong high speed rail line station code
station_dict = np.load("station_dict.npy", allow_pickle=True).item()
names = ["香港西九龙", "福田", "深圳北", "东莞南", "东莞", "光明城", "虎门", "庆盛", "广州东", "广州南"]
codes = [] # ['XJA', 'NZQ', 'IOQ', 'DNA', 'RTQ', 'IMQ', 'IUQ', 'QSQ', 'GGQ', 'IZQ']
hk_station_name_code = {}
for name in names:
    code = station_dict.get(name)
    hk_station_name_code[name] = code
    codes.append(code)

print(names)
print(codes)
print(hk_station_name_code)
