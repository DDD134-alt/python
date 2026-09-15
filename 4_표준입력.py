# 표준입력이란 콘솔(이 쌔까만 화면)로 부터 사용자의 입력을 받음
# 기본적으로 문자열로 반환되면, 다른 데이터 형으로 변환하려면 형변환 함수를 사용해야 함

"""
# 이름(문자열), 나이(정수), 성별(문자열), 주소(문자열), 평균(실수) 입력 받아 출력 해보기
name = input("이름 : ")
age = int(input("나이 : ")) # 문자열로 입력받은 나이를 정수로 반환
gender = input("성별(M/F) : ").upper() # 입력받은 문자열을 대문자로 반환
addr = input("주소 : ")
# 국어 영어 수학 성적을 입력 받아 총점, 평균으로 출력
kor = int(input("국어 : "))
eng = int(input("영어 : "))
mat = int(input("수학 : "))

print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {'남성' if gender == "M" else "여성"}")
print(f"주소 : {addr}")
print(f"총점 : {kor + eng + mat}")
print(f"평균 : {(kor + eng + mat) / 3 : .2f}")
"""
"""
# 국어 영어 수학 성적을 한번에 입력받아 총점과 평균으로 출력
score = list(map(int, input("국어 영어 수학: ").split()))
# split() : 공란을 기준으로 쪼개겠다
# map(A, B) : B를 A의 성질로 바꾸라
# list() : 괄호안의 내용을 리스트로 만들어라

print(f"총점 : {sum(score)}")
print(f"평균 : {sum(score) / 3 : .2f}")
"""
"""
# 시간을 24제로, 23:56:45 입력받아 12제로 변환해서 11시56분45초 형대로 출력하기
hour, minute, sec = input("24시간 시:분:초 > ").split(":")
hour = int(hour)
minute = int(minute)
sec = int(sec)
if hour == 12:
    print(f"오후{hour:02}시{minute:02}분{sec:02}초")
elif hour > 12:
    hour -= 12 # hour = hour - 12
    print(f"오후{hour:02}시{minute:02}분{sec:02}초")
else:
    print(f"오후{hour:02}시{minute:02}분{sec:02}초")
"""


# 1.이름과 주소를 공백으로 구분하여 한 번에 입력 받아 두 값을 각각 출력 되도록
name, addr = input("이름과 주소를 입력하세요 : ").split()
print("이름 : " + name)
print("주소 : " + addr)

# 2."14:5:9" 형대의 시간을 콜론(:) 기준으로 구분하여 각 2자리 폭에 빈칸은 0으로 채워 추력 되도록
hour, minute, sec = map(int, input("시분초 사이 :을 넣어 입력해주세요. ").split(":"))
print(f"{hour:02}:{minute:02}:{sec:02}")

# 3.국어 영어 수학을 한 버에 받아 공잔으로 구분하여 평균이 60점이면 "합격", 아니면 "불합격"이 되도록 출력
score = list(map(int, input("국어, 영어, 수학 : ").split()))
print(f"총합 : {sum(score)}")
print(f"평균 : {sum(score) / 3 : .0f}")
if sum(score) / 3 >= 60:
    print("합격")
elif sum(score) / 3 < 60:
    print("불합격")

# 3.훨 간단한 코드
kor, eng, mat = map(int, input("국어 영어 수학 : ").split())
avg = (kor + eng + mat) / 3
print(f"{'축하합니다, 합격입니다!' if avg >= 60 else '안타깝습니다, 불합격입니다!'}")
