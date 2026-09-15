# 문자열 : 문자가 연속으로 존재하는 것, 파이썬은 문자와 문자열을 구분하지 않음 (전부 문자열)
# "", '', """ """, ''' '''

# 인덱싱과 슬라이싱
# 인덱싱은 인덱스로 원하는 값을 추출

# 자료 가져오기의 2가지 방법
# - 인덱스 가져오기
# - 키로 가져오기 (주민등록 번호, 학번 같은 고유 정보를 키라고 생각하면 됨)

text = "안녕하세요. 파이썬 입니다."
"""
print(text[0])  # 안
print(text[7])  # 파
print(text[-1]) # 다

print(text[7:10]) # 파이썬
print(text[::-1]) # 처음부터 마지막까지 역순으로 출력
print(text[:5])   # 처음부터 5번째까지 추출
"""

# 현제 날짜 가져오기
from datetime import datetime
current_year = datetime.now().year

# 주민등록번호 입력시 아래와 같은 정보가 출력
# 주민등록번호 : 010222-3164414
# 생년월일 : 2001년 2월 22일
# 성별 : 남성
# 나이 : 25살
"""
jumin = input()
key = int(jumin[7])
year = int(jumin[:2])
mon = int(jumin[3:5])
day = int(jumin[4:6])

if key ==1 or key == 2:
    year += 1900
    print(f"생년월일 : {year}년 {mon:02}월 {day:02}일")
    print(f"나이 : {current_year - year}살")
else:
    year += 2000
    print(f"생년월일 : {year}년 {mon:02}월 {day:02}일")
    print(f"나이 : {current_year - year}살")

if key ==1 or key == 3:
    print("성별 : 남성")
else:
    print("성별 : 여성")
"""

# isupper(), islower()
# 입력 받은 문자열에서 소문자는 대문자로, 대문자는 소문자로 변경
"""
a = input("문자열을 입력하세요: ")
for e in a:
    if e.islower():
        print(f"{e.upper()}", end="")
    elif e.isupper():
        print(f"{e.lower()}", end="")
    else:
        print(e, end="")
print()
"""

# 문자열 변경 : replace("", "")
"""
input_str = "Hello Python Program"
new_str = input_str.replace("Python", "JavaScript")
print(input_str)
print(new_str)
"""

# 문자 갯수 세기 : count
text = "Google Kakao naver openAI oole"
print(text.count("a")) # 결과 : 3

# 문자열 길이 : len()
text = "Hello World"
print(len(text)) # 11

# 문자열 찾기 : find()와 rfind(), 그리고 index()
# find() : 찾은 부분 문자열의 첫 번때 인덱스를 반환, 부분 문자열을 찾지 못하면 -1을 반복
# index() : 찾은 부분 문자열의 첫번째 인덱스르 반환, 부분 문자열을 찾지 못하면 ValueError 예외를 발생
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))    # o
print(phrase.rfind("가장"))   # 뒤에서부터 찾지만 인덱스는 앞에서 부터

print(phrase.index("포기"))

print(phrase.find("나에게"))   # 찾는 결과가 없으면 -1
print(input_b.index("나에게"))  # 해당 단어가 없으므로 애러가 발생

# 문자열 양옆의 공백 제거
# strip() : 양쪽 공백 제거
# lstrip() : 왼쪽 공백 제거
# rstrip() : 오른쪽 공백 제거
"""
input_a = """
    안녕하세요.
문자열 함수를 알아 봅니다.

    """
print(input_a.strip())
"""
