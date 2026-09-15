# 반복문 : 주어진 조건이 참인 동안은 반복 수행함
# while문
# 복합 대입연산
# while문은 True 말고도 조건을 입력할 수 있지만 그러면 for문과 성질과 같다.
# 반복 회수를 모를때, while문을. 반복 회수를 알때 for문이 적절하다.
"""
n = int(input("정수 입력 : "))
total = 0       # 합계를 저장할 변수
# ===============================================================
while n > 0:    # 반복문의 조건인 n의 값이 0보다 크면 참으로 반복 수행
    total += n  # total = total + n
    n -= 1      # n = n - 1 : n의 값을 변경해서 반복문을 빠져 나가게 함
# ===============================================================
for i in range(1, n + 1):
    total += i
# ===============================================================
while True:
    total += n
    n -= 1
    if n ==0:
        break
# ===============================================================
print(f"합 : {total}")
# 세 코드 다 같은 결과를 낸다.
"""
# 작동원리
# 정수입력 : 10
# total(10) = total(0) + n(10)  > total 값이 10이 됨
# n(9) = n(10) - 1              > n 값은 9가 됨
# total(19) = total(10) + n(9)  > total 값이 10이 됨
# 이런 식으로, n이 0이 될때까지 반복. 다라서 55가 됨
"""
n = int(input("정수 입력 : "))
total = 0
for i in range(1, n + 1):   # i에는 순서대로 1, 2, 3이 들어갑니다.
    total += i              # total = total + i 와 같은 뜻 (누적 덧셈)
print(f"합 : {total}")
"""

# while 문은 반복 횟수를 알 수 없을때 사용하면 좋음
# 성별을 받는데 남성은 M, 여성은 F로 입력받되, 이외는 반복 질문하기
"""
while True:
    gender = input("성별을 입력하게.").upper()
    if gender == "M" or gender == "F":
        break
    print("성별에 오타 있냐?")
print(f"{'남성' if gender == 'M' else '여성'} 입니다.")
"""
"""
name = input("이름 : ")
while True:
    kor = int(input("국어 : "))
    eng = int(input("영어 : "))
    mat = int(input("수학 : "))
    if (0 <= kor <= 100) and (0 <= eng <= 100) and (0 <= mat <= 100):
        break
    print("성적을 잘 못 입력 하셨습니다.")

total = kor + eng + mat
avg = total / 3
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"
print(f"총점 : {total}, 평균 {avg:.0f}")
print(f"{name}님의 등급은 {grade} 입니다.")
"""
"""
name = input("이름 : ")
while True:
    kor = int(input("국어 : "))
    if 0 <= kor <= 100:
        break
    print("잘 못 입력 하셨습니다.")
while True:
    eng = int(input("영어 : "))
    if 0 <= eng <= 100:
        break
    print("잘 못 입력 하셨습니다.")
while True:
    mat = int(input("수학 : "))
    if 0 <= mat <= 100:
        break
    print("잘 못 입력 하셨습니다.")

sum = kor + eng + mat
avg = sum / 3
if avg >= 90:
    victory = " 축하합니다!"
    grade = "A"
elif avg >= 80:
    victory = " 잘 하셨습니다."
    grade = "B"
elif avg >= 70:
    victory = " 그럭저럭 괜찮았어요."
    grade = "C"
elif avg >= 60:
    victory = " 좀 더 노력하세요."
    grade = "D"
else:
    victory = " 더욱 노력해 주세요..."
    grade = "F"

print(f"{name}님의 총점은 {sum}점 이고, 평균은 {avg:.0f}점 입니다")
print(f"당신의 등급은 {grade}입니다.{victory}")
"""
