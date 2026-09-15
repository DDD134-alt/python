
# 딕셔너리 : 별도의 키를 통해 각 요소를 접근 할 수 있도록 만들어진 데이터 타입
# {}로 선언, 각 요소는 쉼표(,)를 사용해 구분
# 키 : 값 -> 키와 값은 콜론(:)으로 구분되며 한쌍으로 구성된다.
# 대괄호[]: 리스트, 중괄호{}: 딕셔너리, 소괄호(): 튜풀

# 파이썬과 자바는 딕셔너리가 다르다!
# Python : Dictionary
# Java : Map (HachMap) key:Value 타입
"""
coffee_menu = {"Americano": 2500, "Esspresso": 1000, "Latte": 4000, "Moca": 4500}
print(coffee_menu)
print(coffee_menu["Esspresso"]) # 키 값 확인하는 방법
print(coffee_menu.get("Latte")) # 키 값 확인하는 방법
"""

# 추가, 삭제, 키 존재 여부 확인
"""
coffee_menu["ColdBrew"] = 5500  # 새로운 키와 값 추가
del coffee_menu["Latte"]        # 키와 값 제거

for e in coffee_menu:
    print(f"키 : {e}, 값 : {coffee_menu[e]}")
"""

# update 함수 사용하기 : 딕셔너리 데이터를 한꺼번에 변경 가능
"""
coffee_menu.update({"Americano": 3000, "Esspresso": 1500, "Latte": 3000, "Moca": 4000, "smoothie": 5000})
# 똑같은 키가 있다면 값을 업데이트해주고, 똑같은 키가 없다면 새로 추가
print(coffee_menu)
"""

# 1.
student_score = {"철수": 90, "영희": 85, "민수": 78}
print(student_score)

# 2.
coffee_menu = {"Americano": 2500, "Esspresso": 1000, "Latte": 4000, "Moca": 4500}
print(coffee_menu.get("Moca"))          # 출력 > 4500
print(coffee_menu.get("Cappuccino"))    # 출력 > None

# 3.
coffee_menu.update({"Cappuccino": 4800})
print(coffee_menu)  # 딕셔너리 끝에 카푸치노 4,800원 추가
del coffee_menu["Moca"]
print(coffee_menu)  # 딕셔너리에 모카 제거

# 4.
for e in coffee_menu:
    if coffee_menu[e] >= 4000:
        print(f"{e} : {coffee_menu[e]}원")

# 5.

for key, value in coffee_menu.items():
    coffee_menu[key] = int(value * 1.1)
print(coffee_menu)
if "Latte" in coffee_menu:
    print("라떼 메뉴가 있습니다")
else:
    print("라떼 메뉴가 없습니다")