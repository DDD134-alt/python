# - 메뉴는 [1]예매하기, [2]종료하기
# - 사용자로부터 좌석번호(index)를 입력받아 예매하는 시스템이다. (좌석은 10개이다.)
# - [V] [V] [V] [  ] [  ] [  ] [  ] [  ] [  ] [  ]
# - 예매가 완료되면 해당 좌석 값을 1로 변경한다.
# - 이미 예매가 완료된 좌석은 재구매할 수 없다.
# - 한 좌석당 예매 가격은 12000원이다.
# - 프로그램 종료 후, 해당 영화관의 총 매출액을 출력한다.

# 좌석 개수 리스트 만들기

seat = [0] * 10 # 전역 리스트, 0으로 초기화된 값 10개 만들기
price = 12000

# 좌석 출력 함수
def print_seat():
    for e in seat:
        if e == 0:
            print("[ ]", end=" ")
        else:
            print("[V]", end=" ")

# 좌석 선택 함수
def select_seat():
    print_seat()
    seat_num = int(input("좌석번호 입력")) - 1
    if seat[seat_num] == 0:
        seat[seat_num] = 1
        print_seat()
    else:
        print("이미 예약 된 자석 입니다.")

def cancel_seat():
    print_seat()
    seat_num = int(input("좌석번호 입력")) - 1
    if seat[seat_num] == 1:
        seat[seat_num] = 0
        print_seat()
    else:
        print("예약된 자석이 아닙니다")

def total_account():
    cnt = 0
    for e in seat:
        if e == 1:
            cnt += 1
    return price * cnt

while True:
    print("[1]예매하기")
    print("[2]취소하기")
    print("[0]종료하기")
    sel = int(input("메뉴선댁. "))
    if sel == 1:
        select_seat()
    elif sel == 2:
        cancel_seat()
    elif sel == 0:
        print(f"총 매출 : {total_account():,}원")
    else:
        print("다시 입력.")



# 입력으로 들어오는 수의 평균을 구해서 반환 후 출력 하기
"""
def avg_num(num):
    return sum(num) / len(num)
num = list(map(int, input("숫자를 입력하면 평균값을 구해드립니다! ").split()))
print(f"{avg_num(num):.0f}")
"""
"""
number = list(map(int, input("숫자입력. ").split()))
def a():
    if len(number) <= 2:
        print(number[1])
    else:
        return "-1"
"""

# 두번째 수 찾기
# 리스트에 찾는 숫자가 2번 이상 나올때 두번째로 나오는 수의 위치 값을 출력.
# 찾는 숫자가 2번 이상 안 나오면 -1로 출력
"""
def second_num(ls, n):
    cnt = 0
    for i in range(len(ls)):
        if ls[i] == n:
            if cnt > 0 : return i+1
            else: cnt += 1
    return -1

ls = list(map(int, input("리스트 입력 : ").split()))
n = int(input("찾는 숫자 : "))
print(second_num(ls, n))
"""

# 세자리수 정수 입력 받아 가장 큰수 출력하기
"""
def mex_num(num):
     if 100 <= num < 1000:
         return max(num)

num = list(map(int, input("리스트 입력 : ").split()))
mex_num(num)
"""