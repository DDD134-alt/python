# [] : 대괄호 리스트 읽고쓰기 가능
# () : 괄호 튜플 읽기가능, 수정 불가능

# 문제1회원정보를 입력 받아서 출력 하는 예제 진행
# - 이름 입력
# - 나이 입력 : 1 ~ 199까지 입력 받고 잘못된 값이 오면 재 입력 요청을 한다.
# - 성별 입력 : 영문자 (M과m은 남성) (F와 f는 여성)으로 입력 받고 나머지는 재 입력 요청을 한다. (남성과 여성으로 출력)
# - 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고 나머지는 재 입력 요청 한다.
# - 결과는 마지막에 한번에 출력 한다.

# 잇츠 미 풀이
"""
jop1 = "학생"
jop2 = "회사원"
jop3 = "주부"
jop4 = "무적"

name = input("이름. ")
while True:
    age = int(input("나이. "))
    if not 0 < age < 200:
        print("정확한 나이를 입력해 주세요.")
    else:
        break

while True:
    gender = input("성별(M/F). ").upper()
    if gender != "M" and gender != "F":
        print("해당하는 성별을 정확히 입력해 주세요.")
    else:
        break
print("[1] 학생  [2] 회사원  [3] 주부  [4] 무적")
while True:
    jop = int(input("해당하는 직업의 숫자를 기입해 주세요. "))
    if jop == 1:
        print(f"이름 : {name}")
        print(f"나이 : {age}")
        print(f"성별 : {'남성' if gender == 'M' else '여성'}")
        print(f"직업 : {jop1}")
        break
    elif jop == 2:
        print(f"이름 : {name}")
        print(f"나이 : {age}")
        print(f"성별 : {'남성' if gender == 'M' else '여성'}")
        print(f"직업 : {jop2}")
        break
    elif jop == 3:
        print(f"이름 : {name}")
        print(f"나이 : {age}")
        print(f"성별 : {'남성' if gender == 'M' else '여성'}")
        print(f"직업 : {jop3}")
        break
    elif jop == 4:
        print(f"이름 : {name}")
        print(f"나이 : {age}")
        print(f"성별 : {'남성' if gender == 'M' else '여성'}")
        print(f"직업 : {jop4}")
        break
    else:
        print("정확한 직업을 다시 선택해 주세요.")
"""
# dictionary, try-except, continue 으로 간략화하고 오류 방지한 풀이
"""
jops = {
    1: "학생",
    2: "회사원",
    3: "주부",
    4: "무적"
}

name = input("이름. ")
while True:
    try:
        age = int(input("나이. "))
    except ValueError:
        print("숫자를 입력해 주세요!")
        continue

    if not 0 < age <= 100:
        print("정확한 나이를 입력해 주세요.")
    else:
        break

while True:
    gender = input("성별(M/F). ").lower()
    if gender == "m" or gender == "f":
        break
    print("성별을 잘 못 입력 하셨습니다.")

print("[1] 학생  [2] 회사원  [3] 주부  [4] 무적")
while True:
    try:
        jop = int(input("해당하는 직업의 숫자를 기입해 주세요. "))
        # try-except 문을 쓰는 이유!
        # jop에 int(숫자로 인식해라)문을 썻으므로 숫자 이외 정보를 입력하면 오류가 생김
        # 이때, ValueError(정수로 바꿀 수 없는 문자/실수 입력 시 발생)를 사용해 오류 예방
    except ValueError:
        print("숫자로 입력해 주세요!")
        continue
        # 숫자가 아닌 문자를 입력하면 아래 if문으로 가지 않고 즉시 재입력 해라!는 의미로 continue를 덧붙임

    if jop in jops:
        # jop에 넣은 값이 jops에 있는 정보인지 묻기위해 in을 넣음
        print(f"이름 : {name}")
        print(f"나이 : {age}")
        print(f"성별 : {'남성' if gender == 'm' else '여성'}")  # "M" -> 'M' 수정
        print(f"직업 : {jops[jop]}")
        break

    else:
        print("정확한 직업을 다시 선택해 주세요.")
"""
# 튜플과 isdigit을 사용한 풀이
"""
name = input("이름을 입력 하세요 : ")
while True:
    age = input("나이를 입력하세요 : ")
    if age.isdigit():
        # .isdigit() : 문자열이 양의 정수인지만 확인하는 함수
        age = int(age)
        if 0 < age < 200:
            break
    print("나이를 잘못 입력 하셨습니다. 다시 입력 하세요.")

while True:
    gender = input("성별을 입력 하세요 : ").lower()
    if gender == "m" or gender == "f": break
    print("성별을 잘 못 입력 하셨습니다.")

while True:
    jobs = input("직업을 입력 하세요 : ")
    if jobs.isdigit():
        jobs = int(jobs)
        if 0 < jobs < 5: break
    print("직업이 잘못 입력되었습니다. 다시 입력해주세요.")

if gender == 'm':
    gen_name = "남성"
else:
    gen_name = "여성"

jobs_name = ("", "학생", "회사원", "주부", "무직")  # 튜플 사용

print("=" * 3, "회원정보", "=" * 3)
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gen_name}")
print(f"직업 : {jobs_name[jobs]}")
"""

# 문제2 짝수/홀수 개수 세기
# 정수를 하나씩 계속 입력받다가, -1이 입력되면 반복을 종료합니다.
# 그동안 입력받은 숫자 중 짝수의 개수와 홀수의 개수를 각각 출력하세요.
# while과 break 사용
"""
n = int(input("정수. "))
count1 = 0
count2 = 0
while n > 0:
    if n % 2 == 0:
        count1 += 1
    else:
        count2 += 1
    n -= 1
print(f"짝수 : {count1}, 홀수 : {count2}")
"""
"""
even_cnt = 0
odd_cnt = 0
while True:
    n = int(input("정수 입력 (-1 종료): "))
    if n == -1:
        break
    if n % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

print(f"짝수 개수: {even_cnt}")
print(f"홀수 개수: {odd_cnt}")
"""

# 문제3 구구단 중 특정 단만 출력하기
# # 2~9 사이의 정수를 입력하세요: 3

# 모든 구구단이 여기에 있다!
"""
n = int(input("구구단. "))
for i in range(n, n + 1):
    for j in range(1, 10):
        print(f"{i} × {j} = {i * j}")
    j += 1
    print()
"""
# 좀 더 간략한 이 세상의 모든 구구단
"""
n = int(input("구구단. "))
for i in range(1, 10):
    print(f"{n} × {i} = {n * i}")
"""
# 그런데 출력하는 구구단이 정해져 있었다...
"""
while True:
    dan = int(input("2 ~ 9 사이의 정수 입력: "))
    if 2 <= dan <= 9:
        break
    print("잘못된 입력 입니다.")

for i in range(1, 10):
    print(f"{dan} x {i} = {dan * i}")
"""
