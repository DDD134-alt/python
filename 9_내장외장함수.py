# 내장함수 : 파이썬에서 기본 제공, import 없이 사용
"""
ls = [23, 45, 56, 34, 36, 67, 78, 89] # 연속된 값을 저장할때 리스트를 사용
print(f"리스트 출력 : {ls}")
print(f"합계 구하기 : {sum(ls)}")
print(f"평균 구하기 : {sum(ls) / len(ls)}")
print(f"최대값 : {max(ls)}")
print(f"최소값 : {min(ls)}")
print(f"몫과 나머지 : {divmod(11, 5)}")
print(f"오름차순 정렬 : {sorted(ls)}")
print(f"내림차순 정렬 : {sorted(ls, reverse=True)}")
"""
# 함수는 한 번에 하나의 일만 수행하고 하나의 결과값을 내는게 유리하다.
# 여러 일을 수행하려고 하면 비용도 많이 나가고 용도에 맞게 사용하려면 범위의 한계가 명확하기 때문에 비효율적이다.

# 이름과 5과목의 정석을 입력 받아 이름, 총점, 평균, 최대값, 최소값 구하기
"""
name = input("이름. " )
kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
sci = int(input("과학 점수 : "))
mat = int(input("수학 점수 : "))
his = int(input("역사 점수 : "))

list = [kor, eng, sci, mat, his]

print(f"총점 : {sum(list)}")
print(f"평균 : {sum(list) / len(list)}")
print(f"최고점 : {max(list)}")
print(f"최하점 : {min(list)}")
"""
"""
name = input("이름 입력 : " )
score = list(map(int, input("5과목 성적 입력 : ").split()))
print(f'''
이름 : {name},
총점 : {sum(score)},
평균 : {sum(score) / len(score)},
최고점 : {max(score)},
최하점 : {min(score)}
''')
"""


# 외장함수 : 파이썬에서 기본 제공, 단 import 해서 사용
# 랜덤 함수 : 난수 발생기
import random
# - randint(시작값, 끝값) : 지정된 범위 안의 임의의 정수 생성
"""
for i in range(20):
    print(f"{random.randint(1, 10)}", end=" ") # 1에서 10 사이의 임의의 값 생성
print()
"""
# - randrange(시작값, 끝보다 1 많은 값, 건너뛰기 값)
"""
for i in range(20):
    print(f"{random.randrange(1, 10, 2)}", end=" ")
    # 1에서 10미만 까지의, 2씩 증가하는 수(따라서 1, 3, 5, 7, 9)에서 무작위로 값 생성
print()
"""
# 무인도 탈출 게임
# 두개의 주사위를 굴려 갇은 값이 나오면 "무인도 탈출! 탈출 시도 횟수, 두개의 주사위 값"
"""
cnt = 0
while True:
    rand1 = random.randint(1, 6)
    rand2 = random.randint(1, 6)
    print("탈출시도.....실패!")
    cnt += 1
    if rand1 == rand2:
        print(f"무인도 탈출 성공!\n탈출 시도 횟수 : {cnt}\n탈출 주사위 값 : {rand1}")
        break
"""

# 로또번호 생성하기 (1~45 사이의 임의의 숫자 6개. 단, 중복 안됨)
"""
lotto = [] # 값을 기억하기 위한 빈 리스트
while True:
    value = random.randint(1, 45)
    if value not in lotto:      # 생성된 난수가 로또 리스트에 포함되어 있지 않으면,
        lotto.append(value)     # 리스트의 마지막 값 추가
    if len(lotto) == 6: break   # 중복되지 않은 번호가 6개가 되면 반복문 탈툴
print(lotto)
"""

# 날짜 및 시간 관련 처리 모듈
from datetime import datetime
# datetime.today()        # 운영체제로부터 시간 가져오기
# datetime.today().year   # 현재 연도 가져오기
# datetime.today().month  # 현재 월 가져오기
# datetime.today().day    # 현재 일 가져오기
# datetime.today().hour   # 현재 시간 가져오기
"""
print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)
"""
# 현재 시간 가져오기
# %Y: 4자리 연도
# %m: 2자리 월 (01~12)
# %d: 2자리 일 (01~31)
# %A: 요일 이름 (Locale 설정에 따라 표시)
# %H: 24시간 형식의 시 (00~23)
# %M: 2자리 분 (00~59)
# %S: 2자리 초 (00~59)

# 원하는 출력 형식 만들기
today = datetime.now()
formatted = today.strftime("오늘은 %Y년 %m월 %d일(%A) %H시 %M분 %S초 입니다.")
print(formatted)

# 실습 1: 나의 생일까지 남은 일수 계산하기
# 오늘 날짜와 올해 생일(예: 12월 25일)까지 남은 일수를 계산해보세요
"""
today = datetime.today()
birthday = datetime(today.year, 3, 28)  # 원하는 날짜로 변경
print(f"생일까지 남은 날: {(birthday - today).days}")
"""
# !!!올해 생일이 지났을때 남은 일수가 마이너스로 나오는 오류를 수정!!!
"""
today = datetime.today()
birthday = datetime(today.year, 3, 28)
if birthday < today:
    birthday = datetime(today.year + 1, 3, 28)
d_day = (birthday - today).days
print(f"다음 생일까지 남은 날: {d_day}일")
"""

# 실습 2: 요일별 인사말 출력하기
# 오늘 요일에 따라 다른 메시지를 출력해보세요
# 월~금: "오늘은 평일입니다. 힘내세요!"
# 토, 일: "오늘은 주말입니다. 푹 쉬세요!"
"""
weekday = today.weekday()
if 0 <= weekday < 4:    # 0(월), 1(화), 2(수),.... 6(일)
    print("평일입니다, 힘내세요!")
else:
    print("주말입니다, 푹 쉬세요!")
"""

# 실습 3: 현재 시간대별 인사말 만들기
# 현재 시각(hour)에 따라 다른 인사말을 출력해보세요
# 06~11시: "좋은 아침입니다"
# 12~17시: "좋은 오후입니다"
# 18~22시: "좋은 저녁입니다"
# 그 외: "늦은 밤이네요, 얼른 주무세요"
"""
hour = datetime.today().hour
if 6 <= hour < 11:
    print("좋은 아침 입니다.")
elif 12 <= hour < 17:
    print("좋은 오후 입니다.")
elif 18 <= hour < 22:
    print("좋은 저녁 입니다.")
else:
    print("잘 시간입니다, 안녕히주무세요.")
"""

# 실습 4: 원하는 형식으로 파일명 생성하기
# strftime을 활용해서 로그 파일명을 만들어보세요
# 예: "backup_20261014_1530.txt" 같은 형식
"""
now = datetime.now()
form = now.strftime("backup_%Y%m%d_%H%M.txt")
print(form)
"""

# math 모듈
import math
print(math.sin(100))    # 사인값을 구합니다.
print(math.cos(100))    # 코사인값을 구합니다.
print(math.tan(100))    # 탄젠트값을 구합니다.
print(math.log(100))    # 로그값을 구합니다.
print(math.ceil(100))   # 소수점 이하를 올림.
print(math.floor(100))  # 소수점 이하를 내림.

# 실습 문제 1: 가위바위보 승부 판정 (random)
# 컴퓨터가 random.randint로 가위(0)/바위(1)/보(2) 중 하나를 뽑고, 사용자가 입력한 값과 비교해서 승패를 판정하는 프로그램을 작성하세요.
# 무승부가 나오면 같은 값이 나올 때까지가 아니라,
# 무승부 횟수를 세어 "총 N번 만에 승부가 났습니다"를 출력하도록 반복문을 구성해보세요.
# 힌트: 무인도 탈출 게임의 while True + cnt 패턴 재사용
# 출력 예시: 무승부! 다시 도전합니다... → 당신의 승리! 총 3번 만에 승부가 났습니다.

# 0 가위 1 바위 2 보
# 가위0 > 보2
# 바위1 > 가위0
# 보2 > 바위1

choices = ["가위", "바위", "보"]
user = int(input("가위(0) 바위(1) 보(2) 중 선택: "))
cnt = 0

while True:
    computer = random.randint(0, 2)
    cnt += 1

    if user == computer:
        print(f"무승부!!! {choices[user]} 다시 도전 합니다.")
        continue

    # 승패판정
    if (user - computer) % 3 == 1:
        print(f"컴퓨터: {choices[computer]} -> 당신의 승리! 총 {cnt}번 만에 승부가 났습니다.")
    else:
        print(f"컴퓨터: {choices[computer]} -> 당신의 패배! 총 {cnt}번 만에 승부가 났습니다.")
    break

# 실습 문제 2: 로그인 시도 시간 기록기 (datetime + math)
# 사용자가 로그인을 시도할 때마다 현재 시각을 strftime으로 "%Y-%m-%d %H:%M:%S" 형식으로 출력하고,
# 최초 로그인 시각부터 현재까지 경과된 시간을 초 단위로 계산해서 math.floor로 소수점을 버린 정수 초로 출력하세요.
# (같은 코드 안에서 time.sleep으로 몇 초 지연을 준 뒤 두 번째 시각을 구해 차이를 계산하면 됩니다.)
# 힌트: (now2 - now1).total_seconds() 결과에 math.floor 적용
# 출력 예시: 로그인 시각: 2026-09-14 10:31:05 → 2번째 접속까지 경과 시간: 12초
