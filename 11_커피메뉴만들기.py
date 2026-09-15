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
        print(f"가격 : {menu[name][1]}\n설명 : {'커피' if menu[name][0] == "coffee" else '티'}이며, {menu[name][2]}")
    else:
        print("찾는 메뉴가 없습니다.")

# [3] 메뉴 추가
def add_menu():
    menu.addend()

# [4] 메뉴 삭제
# [5] 메뉴 수정

# 파일에서 불러오기
def load_menu():
    try: # 예외가 발생하기 쉬운 구간에 오류를 방지하기 위해 사용
         # 방어불가 : 외부 전원이 꺼질때
         # 방어가능 : 찾는 서버가 없을때, 찾는 파일이 없을때 등등
         # 파이썬인 경우 예외문을 넣는건 자유지만(부하가 많이 걸림)
         # 자바는 반드시 예외문을 걸게 함(안전성을 제일 중시하기 때문)
         # C언어는 예외문 없음
        with open("menu.json", "r", encoding="utf-8") as file:
            # .json : 자바스크립트의 이종간 통신가능(직렬화)한 파일. 파이썬 파일을 자바에 열때 자바가 읽을 수 있도록 변형해 읽을 수있도록 하는거
            # rt : 파일을 열때 읽기 권한으로 텍스트창 열기
            # rb : 컴퓨터 언어로 열기
            return json.load(file)
    except FileNotFoundError:
        print("해당 파일이 존재하지 않습니다.")
    except json.JSONDecodeError:
        print("JSON 디코딩 실패")

# 파일에 저장하기
def save_menu():
    with open("menu.json", "w", encoding="utf-8") as file:
        json.dump(menu, file, ensure_ascii=False, indent=4)
        print("menu.json 파일에 저장완료")

# [6] 종료하기
while True:
    print("메뉴를 선택하세요")
    choice = int(input("[1]전체 메뉴 [2]조회 [3]추가 [4]삭제 [5]수정 [6]로딩 [7]저장 [6]종료 : "))

    if choice == 1:
        print_menu()
    elif choice == 2:
        name = input("찾으시는 메뉴를 입력하세요. ")
        get_menu(name)
    elif choice == 3:
        name2 = input("주문할 메뉴를 입력하세요. ")
        add_menu()
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        menu = load_menu()
    elif choice == 7:
        save_menu()
    elif choice == 0:
        break
    else:
        print("정확한 값을 입력하세요.")



