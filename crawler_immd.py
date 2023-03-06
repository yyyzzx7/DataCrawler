# @Time    : 28/2/2023 15:18
# @Author  : chrisyuhimself@gmail.com

import requests
from bs4 import BeautifulSoup
import datetime
import json


class ImmdItem:
    point = ""
    arrival_num_hk = 0
    arrival_num_sz = 0
    arrival_num_other = 0
    arrival_num_all = 0
    departure_num_hk = 0
    departure_num_sz = 0
    departure_num_other = 0
    departure_num_all = 0

    def to_json(self):
        return {
            self.point: {
                "arrival_num_hk": self.arrival_num_hk,
                "arrival_num_sz": self.arrival_num_sz,
                "arrival_num_other": self.arrival_num_other,
                "arrival_num_all": self.arrival_num_all,
                "departure_num_hk": self.departure_num_hk,
                "departure_num_sz": self.departure_num_sz,
                "departure_num_other": self.departure_num_other,
                "departure_num_all": self.departure_num_all,
            }
        }


def crawler_immd():
    res = {}
    # get last 7 days date string, URL example: https://www.immd.gov.hk/hkt/stat_20230220.html
    for i in range(1, 2, 1):
        date = datetime.datetime.today() - datetime.timedelta(i)
        date = date.strftime("%Y%m%d")
        url = "https://www.immd.gov.hk/hkt/stat_{}.html".format(date)
        res[date] = {}

        html = requests.get(url)
        data = html.text.encode(html.encoding).decode('utf-8')
        soup = BeautifulSoup(data, 'lxml')
        tr_list = soup.select(
            "body > section.main-content.main-content-hkt > div > div > div > div > table > tbody > tr")
        for tr in tr_list:
            td_list = tr.findChildren('td')
            item = ImmdItem()
            item.point = td_list[3].text
            item.arrival_num_hk = int(td_list[5].text.replace(",", ""))
            item.arrival_num_sz = int(td_list[6].text.replace(",", ""))
            item.arrival_num_other = int(td_list[7].text.replace(",", ""))
            item.arrival_num_all = int(td_list[8].text.replace(",", ""))
            item.departure_num_hk = int(td_list[10].text.replace(",", ""))
            item.departure_num_sz = int(td_list[11].text.replace(",", ""))
            item.departure_num_other = int(td_list[12].text.replace(",", ""))
            item.departure_num_all = int(td_list[13].text.replace(",", ""))
            res[date].update(item.to_json())

    res = json.dumps(res, ensure_ascii=False)  # 避免单引号问题，中文乱码问题
    return res


crawler_immd()
