# 기본메뉴추가
# {}중괄호를 사용해 선언. 각 요소는 쉼표(,)로 구분
# 키와 값은 콜론(:)으로 구분
# 딕셔너리 내부에 리스트를 가짐
import json

menu = {
    "americano": ["coffee", 2000, "기본 커피 입니다."],
    "espresso": ["coffee", 2500, "커피 원액 입니다."],
    "latte": ["coffee", 4000, "커피에 탄 우유 입니다."],
    "green tea": ["tea", 4500, "녹차 입니다."],
    "black tea": ["tea", 4500, "홍차 입니다."]
}

# 전체 메뉴 만들기
# [1] 전체 메뉴 보기
def print_menu():
    for e in menu:
        print(f"{e} : {menu[e]}")

# [2] 개별 메뉴 조회
def get_menu(name):
    if name in menu:
        print(f"가격 : {menu[name][1]:,}원\n설명 : {'커피' if menu[name][0] == "coffee" else '티'}이며, {menu[name][2]}")
    else:
        print("찾는 메뉴가 없습니다.")

# [3] 메뉴 추가
def add_menu(name, category, price, desc):   # 메뉴의 정보를 매개변수로 전달 받음
    if name not in menu:                     # 딕셔너리에 해당 메뉴가 없으면 추가
        menu[name] = [category, price, desc] # 키를 생성하고, 값을 추가(값이 리스트 임)
        print(f"{name} 메뉴가 추가 되었습니다.")
    else:
        print("메뉴가 이미 존재 합니다.")

# [4] 메뉴 삭제
def del_menu(name):     # 함수의 매개변수로 키값을 전달 받아 해당 메뉴를 삭제
    if name in menu:    # 삭제할 메뉴가 메뉴 딕셔너리에 존재하는지 확인
        del menu[name]  # del 키워드를 사용해 키에 해당하는 메뉴 삭제
        print(f"{name} 메뉴가 삭제 되었습니다.")
    else:
        print("삭제할 메뉴가 없습니다.")

# [5] 메뉴 수정
def modify_menu(name, category, price, desc):
    if name in menu:
        menu[name] = [category, price, desc]
        print("메뉴 정보가 수정 되었습니다.")
    else:
        print("수정할 메뉴가 없습니다.")

# [6] 수정 메뉴 파일에서 불러오기
def load_menu():
    try: # try : 예외가 발생하기 쉬운 구간에 오류를 방지하기 위해 사용
         # 방어불가 : 외부 전원이 꺼질때
         # 방어가능 : 찾는 서버가 없을때, 찾는 파일이 없을때 등등
         # 파이썬은 예외문으로 try-except을 지원하지만 꼭 넣어야 하는건 아님
         # 자바는 예외문으로 try-catch, throws을 지원하지만 Checked Exception 한해 반드시 넣어야 함
         # (안전성을 제일 중시하기 때문)
         # C언어는 예외문이 없고, if문으로 함수의 반환값 검사
        with open("menu.json", "r", encoding="utf-8") as file:
            # .json : 자바스크립트의 이종간 통신가능(직렬화)한 파일.
            #         파이썬 파일을 자바에 열때 자바가 읽을 수 있도록 변형하는거
            #         피클(pickle)도 있지만 이건 파이썬 본연 단어는 전송할 수 없단 단점이 있어 제이슨을 사용
            # rt : 파일을 열때 읽기 권한으로 텍스트창 열기
            # rb : 컴퓨터 언어로 열기
            return json.load(file)
    except FileNotFoundError:
        print("해당 파일이 존재하지 않습니다.")
    except json.JSONDecodeError:
        print("JSON 디코딩 실패")

# [7] 수정 메뉴 파일에 저장하기
def save_menu():
    with open("menu.json", "w", encoding="utf-8") as file:
        json.dump(menu, file, ensure_ascii=False, indent=4)
        print("menu.json 파일에 저장완료")

# 전체 메뉴 만들기
# [1] 전체 메뉴 보기
# [2] 개별 메뉴 조회
# [3] 메뉴 추가
# [4] 메뉴 삭제
# [5] 메뉴 수정
# [6] 메뉴 로딩
# [7] 메뉴 저장
# [0] 종료 하기
while True:
    print("메뉴를 선택 하세요: ")
    choice = int(input("[1]전체 메뉴 [2]조회 [3]추가 [4]삭제 [5]수정 [6]로딩 [7]저장 [0]종료 : "))

    if choice == 1:
        print_menu()
    elif choice == 2:
        name = input("조회할 메뉴 이름 입력: ")
        get_menu(name)  # 매개변수로 값을 전달
    elif choice == 3:
        name = input("추가할 메뉴 입력 : ")
        category = input("분류 입력 : ")
        price = int(input("가격 입력 : "))
        desc = input("설명 입력 : ")
        add_menu(name, category, price, desc)
    elif choice == 4:
        name = input("삭제할 메뉴 입력 : ")
        del_menu(name)
    elif choice == 5:
        name = input("수정할 메뉴 입력 : ")
        category = input("분류 입력 : ")
        price = int(input("가격 입력 : "))
        desc = input("설명 입력 : ")
        modify_menu(name, category, price, desc)
    elif choice == 6:
        menu = load_menu()
    elif choice == 7:
        save_menu()
    elif choice == 0:
        print("프로그램을 종료 합니다.")
        break
    else:
        print("잘못된 메뉴 선택 입니다.")