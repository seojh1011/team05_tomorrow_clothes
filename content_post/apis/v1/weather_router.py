import json

from django.http import HttpRequest
from ninja import Router
import requests
import pandas as pd
from app.local_settings import SERVICE_KEY

from content_post.apps import ContentPostConfig

content = Router(tags=["test"])


@content.post("", url_name="weather")
def get_weather(request: HttpRequest) -> json:
    # 37.626656, 127.0222314 지훈님댁
    x = request.POST['x']
    y = request.POST['y']
    url = 'https://dapi.kakao.com/v2/local/geo/coord2regioncode.json'
    params = {
        'x': x,
        'y': y
    }
    headers = {
        'Authorization': f'KakaoAK {SERVICE_KEY["kakao"]}'
    }
    # 좌표값을 토대로 행정구역표 가져오는 서비스
    response = requests.get(url, params=params, headers=headers)
    # 행정구역표를 가져와서 날씨API에서 필요한 격자 X 격자 Y로 바꿔주는 함수
    division = division_code(response)
    # print(division)
    # 받아온 x, y좌표를 뿌려준다.
    y, x, add_1, add_2, add_3 = division.values[0]
    address = add_1 + add_2 + add_3
    # print(x, y)
    # 좌표를 넣어서 날씨 API에 맞는 형식으로 바꿔주는 클래스
    k_weather = TimeWeather(x, y)
    response = requests.get(k_weather.url, params=k_weather.params)
    database = response.json().get('response').get('body').get('items').get('item')

    pre_tmp = list()
    for db in database:
        if db.get('fcstTime') == k_weather.now and db.get('category') == 'TMP':
            pre_tmp.append(db)
    return {'tmp': pre_tmp, 'address': address}


def division_code(response):
    code = response.json().get('documents')[1].get('code')
    # 엑셀 파일 read(서버실행시 실행)
    xlsx = ContentPostConfig.exel
    add_num_1 = xlsx.query(f"행정구역코드 <= {code}").sort_values(by='행정구역코드', ascending=False).head(1)
    add_num_2 = xlsx.query(f"행정구역코드 >= {code}").head(1)
    if add_num_2[['행정구역코드']].values[0] < add_num_1[['행정구역코드']].values[0]:
        result = add_num_2
    elif add_num_2[['행정구역코드']].values[0] > add_num_1[['행정구역코드']].values[0]:
        result = add_num_1
    else:
        result = add_num_2
    address = result[['1단계', '2단계', '3단계']]
    print(address.values[0])
    division = result[['격자 Y', '격자 X', '1단계', '2단계', '3단계']]
    return division


import datetime
import pytz


# 지역 서울로 마출것


class TimeWeather:
    TZ = pytz.timezone('Asia/Seoul')
    t = datetime.datetime.now(TZ)

    def __init__(self, x, y):
        today, now = self.time(self.t)
        self.today = today
        self.now = now
        self.url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
        self.params = {
            'serviceKey': SERVICE_KEY['weather'],
            'pageNo': '1',
            'numOfRows': '1000',
            'dataType': 'json',
            'base_date': today,
            'base_time': '0500',
            'nx': x,
            'ny': y,
        }

    def time(self, t):
        if t.hour < 5:
            t_1 = t.replace(day=t.day - 1)
            today = t_1.strftime('%Y%m%d')
            now = t_1.strftime('%H') + "00"
            return today, now
        else:
            today = t.strftime('%Y%m%d')
            now = t.strftime('%H') + "00"
            return today, now
