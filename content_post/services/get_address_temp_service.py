# import datetime
# import pytz
#
# # 지역 서울로 마출것
# from app.local_settings import SERVICE_KEY
# from content_post.apps import ContentPostConfig
#
#
# class TimeWeather:
#     TZ = pytz.timezone('Asia/Seoul')
#     t = datetime.datetime.now(TZ)
#
#     def __init__(self, x, y):
#         today, now = self.time(self.t)
#         self.today = today
#         self.now = now
#         self.url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
#         self.params = {
#             'serviceKey': SERVICE_KEY['weather'],
#             'pageNo': '1',
#             'numOfRows': '1000',
#             'dataType': 'json',
#             'base_date': today,
#             'base_time': '0500',
#             'nx': x,
#             'ny': y,
#         }
#
#     def time(self, t):
#         if t.hour < 5:
#             t_1 = t.replace(day=t.day - 1)
#             today = t_1.strftime('%Y%m%d')
#             now = t_1.strftime('%H') + "00"
#             return today, now
#         else:
#             today = t.strftime('%Y%m%d')
#             now = t.strftime('%H') + "00"
#             return today, now
#
#
# class DivisionCode:
#
#     def __init__(self, x, y):
#         self.url = 'https://dapi.kakao.com/v2/local/geo/coord2regioncode.json'
#         self.params = {
#             'x': x,
#             'y': y
#         }
#         self.headers = {
#             'Authorization': f'KakaoAK {SERVICE_KEY["kakao"]}'
#         }
#
#     def division_code(self, response):
#
#         code = response.json().get('documents')[1].get('code')
#         # 엑셀 파일 read(서버실행시 실행)
#         xlsx = ContentPostConfig.exel
#         add_num_1 = xlsx.query(f"행정구역코드 <= {code}").sort_values(by='행정구역코드', ascending=False).head(1)
#         add_num_2 = xlsx.query(f"행정구역코드 >= {code}").head(1)
#         if add_num_2[['행정구역코드']].values[0] < add_num_1[['행정구역코드']].values[0]:
#             result = add_num_2
#         elif add_num_2[['행정구역코드']].values[0] > add_num_1[['행정구역코드']].values[0]:
#             result = add_num_1
#         else:
#             result = add_num_2
#         address = result[['1단계', '2단계', '3단계']]
#         print(address.values[0])
#         division = result[['격자 Y', '격자 X', '1단계', '2단계', '3단계']]
#         return division.values[0]
