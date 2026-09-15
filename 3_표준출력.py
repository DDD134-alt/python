# 파일 이름은 띄어쓰기를 사용하지 않기. 띄어쓰기가 있어도 열고 닫는건 가능하지만
# 링크를 걸때 파일명에 띄어쓰기가 있으면 오류날 수 있음

# 정수 출력
print(30)
age = 23
print("나이:" + str(age))
print(f"나이:{age}") # f-string 방식으로 출력

# 실수 출력
avg = 76.6667
print(f"성적:{avg:.2f}")

# 문자열 출력
name = "곰돌사육사"
print(f"이름:{name}")
print("이름:"+name)

# 리스트 출력 : 파이썬은 기본적으로 배열이 없고 리스트로 연속된 데이터를 관리 함
score = [99, 88, 77]
print(f"성적:{score}")
print(f"성적:{score[0]}")     # 첫번째꺼 출력
print(f"성적:{score[0:2]}")   # 0이상 2미만 (첫번째부터 세번째 이전)까지 출력

# 여러줄 출력
print("""동해물과 백두산이 마르고 닳도록 
하느님이 보우하사 우리나라 만쉐이~""")

# 줄바꿈 문자 확인
# \n : 줄 바꿈, Newline (뉴라인) 또는 Line Feed (라인 피드)의 약자
print("\n동해물과 \n백두산이 \n마르고 \n닳도록 \n")

"""
# \r : 커서를 현재 줄의 맨 앞(맨 왼쪽)으로 이동, Carriage Return (캐리지 리턴)의 약자
import time
for i in range(1, 6):
    # print 끝에는 줄바꿈이 기본적으로 들어가 있으므로,
    # end=""로 기본 줄바꿈을 막고, \r로 커서를 맨 앞으로 돌립니다.
    print(f"\r진행률: {i * 20}% 완료...", end="")
    time.sleep(0.5) # 0.5초 대기
print("\n작업 끝!")
"""

# 제어문자, escape sequence : \n, \t, \r, \\, \b
# 백슬러시 다음에 나오는 특수문자가 표기될 수 있도록 한다 (\")
print("apple\tbanana\tkiwi\tgraoe")
print("""동해물과\n백두산이\t마르고닳도록 
하느님이\\보우하사\b우리나라 만쉐이~
무궁화 \"삼천리\" 화려강산 
대한 \r사람 대한으로 길이보전하쉐이~~""")

# end : 문자열을 출력하고 난 다음의 동작, 기본값이 줄바꿈(\n)
# sep : 문자열 사이에서 콤마를 만나면 동작, 기본값이 스페이스
print("파이썬")
print("파"+"이"+"썬")
print("파""이""썬")
print("파","이","썬") # 콤마(,):세퍼레이터(sep구분자) 콜론(:) 세미콜론(;)

print("Life is shot, you need phython")
print("Life is shot","you need phython")
print("Life is shot", end=" & ")
print("you need phython")
print("Life", "is", "shot", "you", "need", "phython", sep="\n")

# 정렬과 포맷 지점
num1 = 10
num2 = 100
num3 = 1000
# > : 오른쪽 정렬 (공간이 있을시 기본값)
print(f"|{num1:5}|")
print(f"|{num2:5}|")
print(f"|{num3:5}|")

# < : 왼쪽 정렬
print(f"|{num1:<5}|")
print(f"|{num2:<5}|")
print(f"|{num3:<5}|")

# ^ : 중앙 정렬
print(f"|{num1:^5}|")
print(f"|{num2:^5}|")
print(f"|{num3:^5}|") # 공간이 부족해 중간 정렬 안됨, 6정도 공간이면 중앙정렬 됨

# 소수점 이하 출력
PI = 3.141592
print(f"{PI:.2f}")

# 다양한 출력 스타일
name = "곰돌곰돌"
age = 60
gender = "M"
jobs = "개발자"
addr = "충청남도 천안시"

# 파이썬 스타일
# f와 {} 사용
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gender}")
print(f"직업 : {jobs}")
print(f"주소 : {addr}\n")

# 자바 스타일
print("이름 : " + name)
print("이름 : " + str(age))
print("이름 : " + gender)
print("이름 : " + jobs)
print("이름 : " + addr)

# 1. \n, \t를 사용하여 아래와 같은 형태로  자시소개를 한 줄의 문으로 출력
# 이름:  김민준
# 직업:  백엔드 개발자
print("이름:\t김민준\n직업:\t백엔드 개발자")

# 2. 따옴표 출력하기, 아래의
# "오늘도 좋은 하루 되세요!"라고 인사했습니다
print("\"오늘도 좋은 하루 되세요!\"라고 인사했습니다")

# 3. \r로 커서 이동 확인하기
# 사과 바나나 키위 입력후 키위만 나오도록 출력
print("사과\r바나나\r키위")

# 4. "010", "1234", "5678" 세 문자열을 sep="-"을 사용해 아래와 같이 출력
# 010-1234-5678
print("010","1234","5678",sep="-")

# 5. 세 개의 프린트문을 작성하되, end 옵션으로 하나의 줄로 출력하기
# 결과: 파이썬은 즐겁다
print("결과:", end=" ")
print("파이썬은", end=" ")
print("즐겁다", end="\n\n")

# 6. 두가지 스타일로 자기 소개 하기
print(f"안녕하십니까, 제 이름은 {name} 입니다.")
print(f"나이는 {age}세 입니다.")
print(f"직업은 {jobs} 이지요")

print("이름 : " + name)
print("나이 : " + str(age))
print("직업 : " + jobs)

# 7. 정렬로 표 만들기
num11 = 7
num22 = 42
num33 = 365
# 위 세 변수를 각각 너비 6칸 가운데 정렬하여 출력
print(f"|{num11:^6}|")
print(f"|{num22:^6}|")
print(f"|{num33:^6}|")

# 8. 반지름을 이용하여 너비를 구한 뒤, 폭 10칸, 오른쪽 절렬, 소수점 둥째자리까지 출력
r = 5
print(f"넓이:{PI * r * r:>10.2f}")
