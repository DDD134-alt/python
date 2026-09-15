# 반복문 : 주어진 조건이 참인 동안은 반복 수행함
# for문 : 정해진 법위만큼 반복 수행 할 때 효과적
# for 요소 in 시퀀스:
# for 변수 in range(시작값, 최종값, 증감값):
"""
ive = ["안유진", "장원영", "이서", "가을", "레이", "리즈"]

for e in ive:       # 시퀀스형 데이터를 자동으로 반복 수행 하면서 요소의 값을 복사하면서 수행
    e += "*"        # 변경해도 원본 데이터에 영향을 주지 않음
    print(e, end=" ")
print()
for i in range(len(ive)):   #생략된 문, 원레는 (0, len(ive) 1) 이렇게 작성
    print(ive[i], end=" ")
print()
for i in range(0, len(ive), 1):
    ive [i] += "*"  # 요거는 원본 데이터를 변경함
    print(ive[i], end=" ")
print()
for i in range(len(ive) -1, 0 - 1, -1):
    print(ive[i], end=" ")
"""
# 1에서 ~ 100사이의 3의 배수 출력하기
"""
cnt = 0                             # 1. 출력한 개수를 세기 위한 카운터 변수 (처음엔 0개)

for i in range(1, 100 + 1):         # 2. i에 1, 2, 3 ... 100까지 숫자를 순서대로 넣으며 100번 반복!
    if i % 3 == 0:                  # 3. 만약 i를 3으로 나눈 나머지가 0이라면? (3의 배수 판별)
        print(f"{i:2}", end=" ")    # 4. 숫자 i를 2칸에 맞추어 출력하고, 옆으로 한 칸 띔 (줄 바꿈 안 함)
        cnt += 1                    # 5. 출력했으니까 개수 카운터(cnt)를 1 올림

        if cnt >= 10:               # 6. 만약 한 줄에 출력된 개수(cnt)가 10개가 되었다면?
            print()                 # 7. 엔터를 쳐서 다음 줄로 줄 바꿈!
            cnt = 0                 # 8. 새 줄이 시작되었으니 개수를 다시 0으로 리셋!
"""
# 에이아이가 말아주는 폴문 예시
"""
import time

for i in range(1, 101):
    # \r을 맨 앞에 넣어 매번 커서를 줄의 맨 앞으로 이동시킵니다.
    # end=""를 지정하여 줄 바꿈(엔터)이 일어나지 않게 막습니다.
    print(f"\r진행률: {i}% [{'=' * (i // 5)}{' ' * (20 - i // 5)}]", end="")
    time.sleep(0.05)  # 진행 효과를 시각적으로 보여주기 위한 0.05초 대기

print("\n다운로드 완료!")
"""
# 입력 받은 숫자 범위 내에 7의 배수를 출력.
# 한 줄에 10개씩 출력
# 정렬을 적용해 줄 맞추기 {n:5}

# 풀이, 7증가를 때렸더니 0이 함께 달려나옴
"""
num = int(input("정수를 입력하게요 : "))
cnt = 0
for i in range(0, num + 1, 7):
    print(f"{i:^3}", end=" ")
    cnt += 1
    if cnt >= 10:
        print()
        cnt = 0
"""
# 풀아 과정, 내가 푼 것과 달리 0이 나오지 않음
"""
num = int(input("정수 입력 : "))
cnt = 0
for i in range(1, num + 1):
    if i % 7 == 0:
        print(f"{i:^3}", end=" ")
        cnt += 1
        if cnt >= 10:
            print()
            cnt = 0
"""

# 입력 받은 문자열을 뒤집어 출력
# 입력 : abcdef → fedcba
"""
text = input("문자입력 : ")
for i in range(len(text) - 1, -1, -1): 
    print(text[i], end="")
"""

# 입력받은 문자를 소문자를 대문자로, 대문자를 소문자로 출력
"""
text = "Python123!"
new_text = ""

for e in text:
    if e.isupper():
        new_text += e.lower()
    elif e.islower():
        new_text += e.upper()
    else:
        new_text += e

print(new_text)
"""
# 입력받은 정수값을 3의 배수, 5의 배수로 1줄에 5개씩 출력
"""
num = int(input("정수 : "))
cnt = 0
for i in range(1, num + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(f"{i:^4}", end=" ")
        cnt += 1
        if cnt >= 10:
            print()
            cnt=0
"""
"""
num = int(input("정수 : "))
cnt = 0
for e in range(1, num + 1):
    if e % 3 == 0 or e % 5 == 0:
        print(f"{e:^5}", end=" ")
        cnt += 1
        if cnt == 5:
            print()
            cnt=0
"""

# 이중 for문
# 입력 받은 수가 10이라면 10 * 10 행렬 출력
"""
num = int(input("정수 입력 : "))
cnt = 0
for i in range(1, num + 1): # 0 ~ num 미만 돌아감
    for j in range(1, num + 1):
        cnt += 1
        print(f"{cnt:^3}", end="")
    print()
"""

# 단일 for문으로 변경하여 출력 해보기
# 반복문 범위를 num * num
# i % num == 0; print()
"""
num = int(input("정수 입력 : "))
for i in range(1, num * num + 1):
    print(f"{i:^4}", end="")
    if i % num == 0:
        print()
"""

# 구구단 2 ~ 9단 출력
# num = 2
# for i in range(2, 10):
#     for j in range(1, 9):
"""
for i in range(2, 10):  # 바깥쪽 loop: 2단부터 9단까지 (10 미만)
    print(f"--- {i}단 ---")
    for j in range(1, 10):  # 안쪽 loop: 각 단에 1부터 9까지 곱함 (10 미만)
        print(f"{i} * {j} = {i * j}")
    print()
"""
# map : 1급 고차함수
# map(함수, 시퀀스형 데이터)
# list : 배열의 제한이 없다. 몇개가 들어오던 담는거, 구연하기 편하지만 파이썬이 열쒸미 구른다.

# 입력받은 숫자의 합 구하기 (리스트)
"""
score = list(map(int, input("정수 입력. ").split()))
total = 0

for i in range(0, len(score)):
    total += score[i]

for e in score:
    total += e

# 입력 받은 값을 역순으로 출력
for i in range(len(score)-1, -1, -1):
    print(score[i], end="")
"""
# split은 연속되는 공백을 어떻게 처리하는가???
"""
square = list(map(lambda a: a**2, map(int, input("").split())))
print(square)
"""
# 결론 : split은 공백이 여러번 들어가도 하나로 처리해준다.

# 별 100개 찍기
"""
for i in range(10):
    print(f"|i={i}|", end=" ")
    for j in range(10):
        print("*", end=" ")
    print()
"""

# 별로 내리막길 만들기
"""
n = 1
for i in range(10):
    for j in range(n):
        print("*", end=" ")
    n += 1
    print()
"""
"""
for i in range(10):
    for j in range(i + 1):
        print("*", end=" ")
    print()
"""
# 별로 오르막길 만들기
"""
n = 0
for i in range(10):
    for j in range(10 + n):
        print("*", end=" ")
    n += -1
    print()
"""
"""
for i in range(10, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
"""

# 입력받은 값으로 별 내리막길 만들기
"""
n = int(input("별이 쌓인다. "))
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()
"""
# 입력받은 값으로 별 내리막길 만들기
"""
n = int(input("별이 쌓인다. "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    n -= 1
    print()
"""

# continue : 반복문에서 아래의 문장을 수행하지 않고 반복문으로 이동
# 입력받은 정수의 홀수만 출력하기
"""
n = int(input("정수입력. "))
cnt = 0
for i in range(n):
    if i % 2 == 0: continue
    print(f"{i:^3}", end=" ")
    cnt += 1
    if cnt >= 10:
        print()
        cnt = 0
"""
# 입력받은 정수의 3의 배수, 5의 배수만 출력하기
"""
n = int(input("정수입력. "))
cnt = 0
for i in range(n):
    if i % 3 == 0 or i % 5 == 0: continue
    print(f"{i:^3}", end=" ")
    cnt += 1
    if cnt >= 10:
        print()
        cnt = 0
"""
