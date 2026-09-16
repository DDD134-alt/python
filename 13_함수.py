# 함수(function)는 코드의 특정 블록을 하나의 이름으로 묶어둔 것
# 반복적으로 사용해야 하는 코드나 논리적인 작업을 함수로 정의하면 재사용성, 가독성, 유지보수성을 높일 수 있음
# 함수는 생성 이후 호출을 해야 실행 됨
# 매게 변수(빵 재료) > 함수(빵만드는 기계) > 출력(빵) 근데 추력이 없을 수도...
# def 키워드 사용
# 일반적으로 식별자 뒤에 ()소괄호가 있으면 함수

# 함수의 재사용 : 매개변수 존재, 반환값 없음
"""
def name_card(name, addr, phone):
    print(f"이름 : {name}")
    print(f"전화번호 : {phone}")
    print(f"주소 : {addr}")
    print("-"*30)

card = [
    ("안유진", "서울시 강남구 역삼동", "010-1234-5678"),
    ("장원영", "서울시 강남구 삼성동", "010-2345-6789"),
    ("김가을", "서울시 강남구 청담동", "010-3456-7891")
]

for name, addr, phone in card:
    name_card(name, addr, phone)
"""

# 매개변수 O, 반환값 X
# 1-1 이름(name), 나이(age), 취미(hobby)를 매개변수로 받아서 아래 형식으로 출력하는 함수 intro_card()를 작성하시오.
"""
def intro_card(name, age, hobby):
    print(f"이름 : {name}")
    print(f"나이 : {age}")
    print(f"취미 : {hobby}")
    print("-"*30)

name = input("이름을 입력하세. ")
age = int(input("나이를 입력하세. "))
hobby = input("취미를 입력하세. ")

intro_card(name, age, hobby)
"""

# 1-2 과목명(subject)과 점수(score)를 매개변수로 받아 "수학 점수: 90점"
# 형식으로 출력하는 함수 print_score()를 작성하고, 서로 다른 3개 과목으로 호출해보시오.
"""
def card(subject, score):
    print(f"{subject} 점수 : {score}점")

subject = input("과목 : ")
score = int(input("점수 : "))

card(subject, score)
"""

# 매개변수 O, 반환값 O
# 2-1 두 정수를 입력받아 큰 수를 반환하는 함수 get_max(a, b)를 작성하시오. (if문 사용)
"""
def get_max(a, b):
    if a > b:
        return print("a가 더 큰 정수입니다.")
    elif a < b:
        return print("b가 더 큰 정수입니다.")
    else:
        return print("a와 b는 같은 크기의 정수입니다.")

print("두 개의 정수값을 입력해 주세요.")
while True:
    try:
        a = int(input("a : "))
        break
    except ValueError:
        print("정수를 입력해 주세요!")

while True:
    try:
        b = int(input("b : "))
        break
    except ValueError:
        print("정수를 입력해 주세요!")

get_max(a, b)
"""

# 2-2 원의 반지름을 입력받아 원의 넓이를 반환하는 함수 circle_area(r)를 작성하시오. (원주율은 3.14 사용)
"""
def circle_area(r):
    area = 3.141592 * (r ** 2)
    print(f"반지름 {r}의 원의 넓이는 {area:.2f}㎠입니다")

while True:
    try:
        r = int(input("반지름 : "))
        circle_area(r)
        break
    except ValueError:
        print("숫자를 입력해 주세요!")
"""

# 2-3 정수를 입력받아 짝수면 "짝수", 홀수면 "홀수"를 반환하는 함수 check_even_odd(num)를 작성하시오.
"""
def check_even_odd(num):
    if num % 2 == 0:
        return print("짝수임ㅋ")
    else:
        return print("홀수임ㅋ")

while True:
    try:
        num = int(input("짝인지 홀인지 맞춰드림ㅋ. "))
        check_even_odd(num)
        break
    except ValueError:
        print("숫자를 입력해야지!")
"""

# 기본값 인자 : 함수 선언 시 매개 변수에 대한 기본값을 정의
# - 매개변수에 기본값이 정의 되어 있는 경우 함수 호출 시 인자값을 넣지 않으면 기본값으로 호출
"""
def profile(name, age = "응애", jop = "무직", addr = "지구"):
    print(f"이름 : {name}")
    print(f"나이 : {age}")
    print(f"취미 : {jop}")
    print(f"주소 : {addr}")
    print("="*30)

profile("안유진", 23, "우상", "대전시")
profile("장원영", 22, "우상")
profile("짜장")
"""

# 가변 매개 변수
"""
def profile(name, age, *lang):
    print(f"이름 : {name}, 나이 : {age}", end=" ")
    for e in lang:
        print(e, end=" ")
    print()

profile("나희도", 18, "Python", "Java", "C", "C++", "React", "kotlin")
profile("조세호", 38, "Python", "Java")
profile("유제석", 48, "Python", "Java", "C", "C++")
"""

# 실습 문제: 표준 체중 계산기
# 키(cm)와 성별을 입력받아 표준 체중을 계산하는 함수를 작성하시오.

# 조건
# 함수 이름은 std_weight로 하고, 매개변수는 키(h)와 성별(sex) 두 개를 받는다.
# 표준 체중 공식은 다음과 같다.
# 남성: (키(m))² × 22
# 여성: (키(m))² × 21
# 단, 입력받은 키는 cm 단위이므로 함수 내부에서 m 단위로 변환해야 한다. (h / 100)
# 함수는 계산된 표준 체중 값을 반환(return) 해야 한다. (출력 X)
# input()을 이용해 사용자로부터 키(cm)와 성별을 입력받는다.
# 키는 정수로 변환하여 저장 (int(input(...)))
# 성별은 "남성" 또는 "여성" 문자열로 입력받음
# 함수 호출 결과를 아래 형식으로 출력하시오. (소수점 둘째 자리까지)
"""
def std_weight(sex, h):
    h /= 100
    if sex == "남성":
        height = (h ** 2) * 22
    else:
        height = (h ** 2) * 21
    print(f"당신의 표중 체중은 {height:.2f}kg입니다.")

while True:
    sex = input("성별을 입력해 주세요(남성/여성) : ")
    if sex == "남성" or sex == "여성":
        break
    else:
        print("성별을 정확하게 입력해 주세요.")

while True:
    try:
        h = int(input("키를 입력해 주세요 : "))
        std_weight(sex, h)
        break
    except ValueError:
        print("숫자를 입력해 주세요!")
"""

# 입력 받은 정수보다 미만의 소수의 합을 구하는 함수를 만드세요.
# 예) 12이면 2+3+5+7+11 = 28
# 소수란 ? ***1과 자기 자신 이외의 자연수로 나눌 수 없는 1보다 큰 자연수를 의미***

# 단계1, 소수 판별하기
"""
def is_prime_func(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    return is_prime

n = int(input("정수를 입력: "))
if is_prime_func(n):
    print(f"{n}은 소수 입니다.")
else:
    print(f"{n}은 소수가 아닙니다.")
"""

# 2단계. 소수의 합 구하기
"""
def prime_func(n):
    is_prime = True           # 일단 n이 소수(True)란 판정표를 붙임 (is_...= "맞니?"란 뜻으로 붙인 이름)
    for i in range(2, n):
        if n % i == 0:        # 소수는 1외에 모든 수에 나머지 값이 남으므로 2, ..., n까지 나누어본다.
            is_prime = False  # 이때, 한 번이라도 0으로 나누어떨어지면 이는 소수가 아니므로 False 판정표로 바꾼다.
    if is_prime:
        return n              # 소수로 판정되면 그 숫자(n) 자체를 반환한다.
    else:
        return 0              # 소수가 아니면 합계에 영향을 주지 않도록 0을 반환한다.

n = int(input("정수 입력: "))

total = 0
for i in range(2, n):
    total += prime_func(i)
    # prime_func(i)를 실행해서 나온 결과값(소수 숫치 또는 0)을 total에 기존 값 + 새로 나온 값 형태로 계속 더함
print(total)
"""

# AI로 작성한 코드
# is_prime = True 판정표 없이 return True/False로 작성
def is_prim(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input("정수 입력: "))

total = 0
for i in range(2, n):
    if is_prim(i):
        total += i
print(f"소수 총합 : {total}")
