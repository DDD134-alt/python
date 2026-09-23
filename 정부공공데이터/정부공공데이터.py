import requests  # HTTP로 서버의 데이터를 수신하기 위해서 사용
import json      # 정부기관 공공데이터를 JSON형태로 수신 받기 위함
import datetime  # 시간 정보를 구하기 위해서

API_KEY = '9ab1d98b32a1d1cda76a639e72f4fc081899e7906cb1f447b9579c3363219f04'

# 요청 주소의 URL 지정
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'

# 날짜 및 시간 설정
now = datetime.datetime.now()  # 운영체제로 현재 시간과 날짜 정보를 가져 옴

# 년월일 정보를 추출하기 위해서 포맷 형식을 지정, base_date : 20260921
date = now.strftime('%Y%m%d')

# 시간 정보를 추출하기 위해서 포맷 형식을 지정, base_time : 1250
if now.minute < 30:   # 현재시간의 분이 30분 이전이면 전 시간대로 설정 (현제시간:1시20분 > 설정시간:1시00분)
    now = now - datetime.timedelta(minutes=30)
    time = now.strftime('%H%M')
else:
    time = now.strftime('%H%M')

# 예보 지점 좌표 (충청남도 천안시 청수동)
nx_val = 63
ny_val = 110

# 한 페이지에 포함된 결과 수
num_of_rows = 6
# 페이지 번호
page_no = 1
# 응답 데이터 형식 지정
data_type = 'JSON'

req_parameter = {'serviceKey': API_KEY,
                 'pageNo': page_no,
                 'numOfRows': num_of_rows,
                 'dataType': data_type,
                 'base_date': date,
                 'base_time': time,
                 'nx': nx_val, 'ny': ny_val
                 }
# 요청 및 응답 : 서버로 부터 데이터를 수신 받기 때문에 예외 처리가 필요
response = ""
try:
    response = requests.get(url, params=req_parameter)
except requests.exceptions.RequestException as e:
    print(f"날씨 정보 가져 오기 오류 : {e}")


# JSON 형태로 응답받은 데어터를 딕셔너리로 변환 (역직렬화)
dict_data = response.json()
print(json.dumps(dict_data, indent=2))

# 딕셔너리 데이터를 분석하여 원하는 데이터를 추출
weather_items = dict_data['response']['body']['items']['item']

for weather_item in weather_items:
    obsrValue = weather_item['obsrValue']
    category = weather_item['category']
    if category == 'T1H':
        print(f"현재기온 : {obsrValue}℃")
    elif category == 'REH':
        print(f"현재습도 : {obsrValue}%")
    elif category == 'RN1':
        print(f"1시간 강수량 : {obsrValue}MM")
