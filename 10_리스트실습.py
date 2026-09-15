# 3개의 햄버거와 2개의 음료 가격을 입력받아 각자 제일 싼 메뉴 합과 50원 할인한 값을 구하기
# - 콘솔로 연속해서 햄버거 3개 가격과 음료 2개의 가격을 입력 받음
# - 햄버거 3개 중 가장 싼 가격을 선택하고 음료둘 중 싼 음료의 가격을 합산하고 여기서 50원 할인

# my문제풀이
"""
burger = list(map(int, input("3종류의 햄버거 값을 입력하세요. ").split()))
drink = list(map(int, input("2종류의 음료수 값을 입력하세요. ").split()))
print(f"햄버거 : {min(burger)}원\n음료수 : {min(drink)}원\n세트 50원 할인! 총합 : {min(burger) + min(drink) - 50}원")
"""

# 햄버거와 음료를 정해진 갯수로만 입력하도록
"""
while True:
    try:
        burger = list(map(int, input("3종류의 햄버거 값을 입력하세요. ").split()))
        if len(burger) == 3:
            break
        else:
            print("3종류의 햄버거 가격을 입력해 주세요!")
    except ValueError:
        print("가격으로 입력해 주세요!")
        continue
while True:
    try:
        drink = list(map(int, input("2종류의 음료수 값을 입력하세요. ").split()))
        if len(drink) == 2:
            break
        else:
            print("2종류의 음료 가격을 입력해 주세요!")
    except ValueError:
        print("가격으로 입력해 주세요!")
        continue

min_b = min(burger)
min_d = min(drink)
total = min_b + min_d - 50

print(f'''
최저가 햄버거 : {min_b}원
최저가 음료수 : {min_d}원
세트 50원 할인! 총합 : {total}원
''')
"""

# 햄버거 3개 가격을 하나씩 입력받아 리스트에 추가
"""
burger = []
for i in range(3):
    while True:
        try:
            price = int(input(f"{i+1}번째 햄버거 가격을 입력하세요 : "))
            burger.append(price)
            break  # 숫자로 올바르게 입력되면 while문 탈출 후 다음 burger 입력
        except ValueError:
            print("❌가격을 숫자로만 입력해 주세요!")

drink = []
for i in range(2):
    while True:
        try:
            price = int(input(f"{i+1}번째 음료수 가격을 입력하세요 : "))
            drink.append(price)
            break  # 숫자로 올바르게 입력되면 while문 탈출 후 다음 drink 입력
        except ValueError:
            print("❌가격을 숫자로만 입력해 주세요!")

# 계산 및 출력
min_b = min(burger)
min_d = min(drink)
total = (min_b + min_d) * 0.9

print(f'''
최저가 햄버거 : {min_b}원
최저가 음료수 : {min_d}원
세트 10% 할인! 총합 : {total:.0f}원
''')
"""

# 한개의 리스트로 구현하기
"""
prices = list(map(int, input("햄버거 3개, 음료 2개 연속 입력: ").split()))
burgers = prices[:3]
drinks = prices[3:]

choice_burger = min(burgers)
choice_drink = min(drinks)

print(f"세트 메뉴 가격: {choice_burger + choice_drink - 50}")
"""


# 리스트 순회 하기 : 5대의 자동차 이름을 입력 받음
# - 범위기반 for문으로 순회해서 출력: for i in range()
# - 시퀀스 for문으로 순회해서 출력: for e in 시퀀스
# - 오름차순, 내림차순 출력

# 에아이가 말아준 문으로 한 번 작성해 본 풀이
"""
car =[]
for i in range(5):
    name = input(f"{i+1}번째 차 이름을 입력하세요. ")
    car.append(name)

car.sort()
for name in car:
    print(name)
"""
# 문제 풀이
"""
cars = list(input("자동차 이름을 입력하세요. ").split())
for i in range(len(cars)):
    print(f"{cars[i]}", end=" ")
print()

for e in cars:
    print(f"{e}", end=" ")
print()

print(f"{sorted(cars)}")
print(f"{sorted(cars, reverse=True)}")
"""
