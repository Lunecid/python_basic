URL = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=%2B58fRxySTvs0PfFQUY4WIxmfUdNzO2PRCGrFR%2BwurNXadOEb4nRyU4TfZFft%2FX7IOwZchblSbWUzs2S9mm1q2Q%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'

import requests
from pprint import pprint #pretty print : python 내에 있는 이쁘게 출력하는 것

res = requests.get(URL)

data = res.json()

items = data['response']['body']['items']

for item in items:
    if item['stationName'] == '강남구' :
        print(item['pm10Value'])

