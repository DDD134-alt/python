
# 파일 열기
"""
with open("./스타벅스일일매출.txt", "r", encoding="utf-8") as file:
    for e in file:
        print(e, end="")
    print()
# with open("1", "2", encoding="3") as file:

# 1 - 상대경로(./), 절대경로(../)
# 상대경로 (Relative Path) : 내가 있는 위치에서 상대가 어느 위치에 있는지 알려주는 것
# 절대경로 (Absolute Path) : 물리적인 위치에서 처음부터 다 적어주는 위치

# 2 - 앞글자: 옵션
# r (Read)   : 기존 파일 읽기. 파일이 없으면 애러발생
# w (Write)  : 새로 쓰기. 기존내용 싹 지우고 덮어쓰기
# a (Append) : 추가. 기존 내용 뒤에 이어쓰기. 파일이 없으면 새 파일 생성

# 2 - 뒷글자: 보조모드
# t (Text)   : 기본값(따로 쓰지 않아도 t가 붙은것과 같음), 생략가능, 글자(.txt, .csv) 파일을 읽을때 사용. 사람이 읽는 글
# b (Binary) : 이미지(.png, .jpg), 음악(.mp3), 엑셀(.xlsx) 등 글자가 아닌 데이터 파일을 읽을때 사용.
#              컴퓨터가 읽는 글(이진법). 택스트보다 가볍다.
# + (Plus)   : 읽고 쓰기 겸용 ("r+" 읽기/쓰기 겸용, "w+" 새로 쓰기/읽기 겸용)

# encoding="utf-8"
# 열때 한글이 깨지지 않도록
"""
"""
# 스타벅스 판매량 구하기
file_name = "./스타벅스일일매출.txt"
dates = []
espresso = []
americano = []
cafelatte = []
cappuccino = []

with open(file_name, "r", encoding="utf-8") as file:
    header = file.readline().split()     # 줄 바꿈 기준으로 한줄을 읽어 들임

    for e in file:                           # 파일 끝에 붙어있는 컴퓨터 언어까지 돌아줌
        data_list = e.split()                # e : 한 줄
        dates.append(data_list[0])
        espresso.append(int(data_list[1]))   # 10,... 입력
        americano.append(int(data_list[2]))  # 50,... 입력
        cafelatte.append(int(data_list[3]))  # 45,... 입력
        cappuccino.append(int(data_list[4])) # 20,... 입력

# 제목 / 전체 판매량 / 일 평균 판매량
print("|   제목   | 전체 판매량 | 일 평균 판매량 |")
print(f"{header[1]:^10}{sum(espresso):^9}{sum(espresso) / len(espresso):^17.2f}")
print(f"{header[2]:^10}{sum(americano):^9}{sum(americano) / len(americano):^17.2f}")
print(f"{header[3]:^10} {sum(cafelatte):^9}{sum(cafelatte) / len(cafelatte):^17.2f}")
print(f"{header[4]:^10} {sum(cappuccino):^9}{sum(cappuccino) / len(cappuccino):^17.2f}")

# 1. 각 메뉴별 전체 판매량
def total_sales_func():
    print("-" * 20)
    print("전체 판매량")
    print(f"{header[1]}\t: {sum(espresso)}잔")
    print(f"{header[2]}\t: {sum(americano)}잔")
    print(f"{header[3]}\t\t: {sum(cafelatte)}잔")
    print(f"{header[4]}\t\t: {sum(cappuccino)}잔")
    print("-" * 20)


# 2. 각 메뉴별 일 평균 판매량
def avg_sales_func():
    days = len(dates)  # 리스트에 포함된 날짜의 갯수
    print("-" * 20)
    print("일 평균 판매량")
    print(f"{header[1]}\t: {sum(espresso) / days:.2f}잔")
    print(f"{header[2]}\t: {sum(americano) / days:.2f}잔")
    print(f"{header[3]}\t\t: {sum(cafelatte) / days:.2f}잔")
    print(f"{header[4]}\t\t: {sum(cappuccino) / days:.2f}잔")
    print("-" * 20)


# 3. 판매량이 가장 높은 메뉴 구하기
def most_sold_menu_func():
    total_list = [sum(espresso), sum(americano), sum(cafelatte), sum(cappuccino)]
    max_val = max(total_list)           # 최고 판매량 수치를 찾음
    max_ind = total_list.index(max_val) # 그 최고 수치가 몇 번째 칸(메뉴)에 있는지 위치를 찾음
    print("-" * 35)
    print(f"가장 많이 팔린 메뉴 [{header[max_ind + 1]}] : {max_val}잔")
    print("-" * 35)

# 4. 판매량이 가장 적은 메뉴 구하기
def least_sold_menu_func():
    total_list = [sum(espresso), sum(americano), sum(cafelatte), sum(cappuccino)]
    min_val = min(total_list)           # 최저 판매량 수치를 찾음
    min_ind = total_list.index(min_val) # 그 최저 수치가 몇 번째 칸(메뉴)에 있는지 위치를 찾음
    print("-" * 35)
    print(f"가장 적게 팔린 메뉴 [{header[min_ind + 1]}] : {min_val}잔")
    print("-" * 35)

# 5. 판매량이 가장 많은 날짜 구하기
def best_solds_day_func():
    total_per_day = []
    for i in range(len(dates)):
        total = espresso[i] + americano[i] + cafelatte[i] + cappuccino[i]
        total_per_day.append(total)
    max_sal = max(total_per_day)           # 최고 판매량 일자를 찾음
    max_ind = total_per_day.index(max_sal) # 그 최고 일자가 몇 번째 칸(메뉴)에 있는지 위치를 찾음
    print("-" * 25)
    print(f"최고 판매일 : {dates[max_ind]} / {max_sal}잔")
    print("-" * 25)

# 6. 반복문으로 구성된 메뉴 만들기
print('''
    [1] 메뉴별 전체 판매량
    [2] 메뉴별 일일 평균 판매량
    [3] 최고 판매량 메뉴
    [4] 최저 판매량 메뉴
    [5] 제일 많이 판매된 날
    [0] 종료하기
    ''')
while True:
    choice = int(input("조회하고 싶은 메뉴의 번호를 입력해 주세요. "))
    if choice == 1:
        total_sales_func()
    elif choice == 2:
        avg_sales_func()
    elif choice == 3:
        most_sold_menu_func()
    elif choice == 4:
        least_sold_menu_func()
    elif choice == 5:
        best_solds_day_func()
    elif choice == 0:
        print("종료합니다.")
        break
    else:
        print("없는 메뉴를 주시다니, 더 살아 무엇하리!")
        break
"""


# AI가 말아주는 코드~
file_name = "./스타벅스일일매출.txt"
dates = []

# 메뉴 데이터를 담을 딕셔너리 생성
sales_data = {}

with open(file_name, "r", encoding="utf-8") as file:
    # 헤더 읽기 (['날짜', '에스프레소', '아메리카노', '카페라떼', '카푸치노'])
    header = file.readline().split()

    # 헤더의 메뉴 이름들로 딕셔너리 키 초기화
    # header[1:] -> ['에스프레소', '아메리카노', '카페라떼', '카푸치노']
    for menu_name in header[1:]:
        sales_data[menu_name] = []

    # 파일 본문 데이터 읽기
    for line in file:
        data_list = line.split()
        dates.append(data_list[0])  # 날짜 저장

        # 각 메뉴별 판매량을 딕셔너리 리스트에 추가
        for idx, menu_name in enumerate(header[1:]):
            sales_data[menu_name].append(int(data_list[idx + 1]))


# 1. 각 메뉴별 전체 판매량
def total_sales_func():
    print("-" * 20)
    print("전체 판매량")
    # menu: 메뉴 이름 (Key), counts: 판매량 리스트 (Value)
    for menu, counts in sales_data.items():
        print(f"{menu}\t: {sum(counts)}잔")
    print("-" * 20)


# 2. 각 메뉴별 일 평균 판매량
def avg_sales_func():
    days = len(dates)
    print("-" * 20)
    print("일 평균 판매량")
    for menu, counts in sales_data.items():
        avg = sum(counts) / days
        print(f"{menu}\t: {avg:.2f}잔")
    print("-" * 20)


# 3. 판매량이 가장 높은 메뉴 구하기
def most_sold_menu_func():
    # max() 함수에 key 기준을 sum으로 지정하여 가장 합계가 큰 메뉴를 바로 찾음
    best_menu = max(sales_data, key=lambda m: sum(sales_data[m]))
    best_val = sum(sales_data[best_menu])

    print("-" * 35)
    print(f"가장 많이 팔린 메뉴 [{best_menu}] : {best_val}잔")
    print("-" * 35)


# 4. 판매량이 가장 적은 메뉴 구하기
def least_sold_menu_func():
    # min() 함수에 key 기준을 sum으로 지정
    worst_menu = min(sales_data, key=lambda m: sum(sales_data[m]))
    worst_val = sum(sales_data[worst_menu])

    print("-" * 35)
    print(f"가장 적게 팔린 메뉴 [{worst_menu}] : {worst_val}잔")
    print("-" * 35)


# 5. 판매량이 가장 많은 날짜 구하기
def best_solds_day_func():
    total_per_day = []

    # 날짜 수(행)만큼 반복하면서 하루 동안 팔린 모든 음료 합계 구하기
    for i in range(len(dates)):
        day_total = sum(counts[i] for counts in sales_data.values())
        total_per_day.append(day_total)

    max_val = max(total_per_day)
    max_idx = total_per_day.index(max_val)

    print("-" * 25)
    print(f"최고 판매일 : {dates[max_idx]} / {max_val}잔")
    print("-" * 25)