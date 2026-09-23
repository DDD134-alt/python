# JSON(JavaScript Object Notation)은 데이터를 저장하고 교환하는 데 널리 사용되는 경량 텍스트 형식 입니다.
# - 파이썬에서는 json 기본 라이브러리를 통해 사용 가능
# - 경량 텍스트 포맷
# - 키와 값으로 구성
# - 언어 독립적
# - 웹 API 통신, 설정 파일, 데이터 저장 및 교환 등 다양한 분야에서 활용
import json

# 파이썬 객체를 json으로 직렬화
# 회원 정보 (이름, 주소, 나이, 성별, 포지션, 전화번호 2개) => 딕셔너리
# 회원 정보가 10개 인 리스트 => 리스트

members = [
    {
        "name": "안유진",
        "addr": "전라북도 전주시",
        "age": 23,
        "gender": "여성",
        "position": "리더, 메인보컬, 리드댄서",
        "phone": ["010-0000-0001", "041-000-0001"]
    },
    {
        "name": "가을",
        "addr": "서울특별시",
        "age": 24,
        "gender": "여성",
        "position": "메인댄서, 서브보컬",
        "phone": ["010-0000-0002", "041-000-0002"]
    },
    {
        "name": "레이",
        "addr": "일본 도쿄",
        "age": 22,
        "gender": "여성",
        "position": "메인래퍼, 서브보컬",
        "phone": ["010-0000-0003", "041-000-0003"]
    },
    {
        "name": "장원영",
        "addr": "대구광역시",
        "age": 22,
        "gender": "여성",
        "position": "센터, 서브보컬, 서브래퍼",
        "phone": ["010-0000-0004", "041-000-0004"]
    },
    {
        "name": "리즈",
        "addr": "경기도 성남시",
        "age": 21,
        "gender": "여성",
        "position": "메인보컬",
        "phone": ["010-0000-0005", "041-000-0005"]
    },
    {
        "name": "이서",
        "addr": "경기도",
        "age": 19,
        "gender": "여성",
        "position": "막내, 서브보컬, 서브래퍼",
        "phone": ["010-0000-0006", "041-000-0006"]
    }
]

# Python 객체를 JSON으로 직렬화
json_str = json.dumps(members, ensure_ascii=False, indent=4)
print(json_str)

# JSON을 Python으로 역직렬화
obj = json.loads(json_str)
print(obj)

print("-"*50)
for e in obj:
    print(e)
print("-"*50)


# 파일로 저장하기
# with는 파일을 자동으로 닫아줌
with open('members.json', 'w', encoding='utf-8') as json_file:
    json.dump(members, json_file, ensure_ascii=False, indent=4)

# 파일에서 읽기
with open('members.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

print(data)
