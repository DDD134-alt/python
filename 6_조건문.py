# 제어문 : 프로그램의 흐름을 제어하는데 사용
# - 조건문 : 입력 값에 따라 특정 코드 블록을 선택적으로 실행
# > 3항연상자(중요), switch문(그다음 중요), if문(덜중요)
# - 반복문 : 조건이 충족되는 동안 특정 코드 블록을 반복 실행
# > while문, for문
"""
num +int(input("정수 입력 : "))

# 양수/음수 구분 하기
# if문에는 콜론(:) 뒤에 들여쓰기(4칸)를 한다. 콜론은 if문 박스 안에 두겠다는 뜻
if num >= 0:
    print(f"{num}은 양수 입니다")
else:
    print(f"{num}은 음수 입니다.")

# 홀수/짝수 구하기
if num % 2 == 0:
    print(f"{num}은 짝수 입니다.")
else:
    print(f"{num}은 홀수 입니다.")

# M이면 남성, F면 영성, 그외는 잘못입력
gender = input("M / F : ").upper()

if gender == "M":
    print("당신은 남성 입니다.")
elif gender == "F":
    print("당신은 여성 입니다.")
else:
    print("잘 못 입력 했습니다.")
"""

# 1. 학생의 이름, 국수영 성적을 입력 받기
# 각각의 성적이 0~100 사이가 아니면 성적을 잘 못 입력했습니다 후 종료
# 성적이 정상입력 됐다면, 총점과 평균 출력
# 평슌이 90점 이상이면 이름과 등급 A 출력
# 평슌이 80점 이상이면 이름과 등급 B 출력
# 평슌이 70점 이상이면 이름과 등급 C 출력
# 평슌이 60점 이상이면 이름과 등급 D 출력
# 나머지는 이름과 등급 F 출력

# 내 문제 풀이
"""
name = input("이름 : ")
kor = int(input("국어 : "))
if kor < 0 or kor > 100:
    print("잘 못 입력 하셨습니다.")
else:
    eng = int(input("영어 : "))
if eng < 0 or eng > 100:
    print("잘 못 입력 하셨습니다.")
else:
    mat = int(input("수학 : "))
if mat < 0 or mat > 100:
    print("잘 못 입력 하셨습니다.")
else:
    sum = kor + eng + mat
    avg = sum / 3
    print(f"당신의 총점은 {sum}점 이고, 평균은 {avg:.0f}점 입니다")
if avg >= 90:
    print(f"축하합니다! {name}님의 등급은 A 입니다!")
if 90 > avg >= 80:
    print(f"{name}님의 등급은 B 입니다.")
if 80 > avg >= 70:
    print(f"{name}님의 등급은 C 입니다.")
if 70 > avg >= 60:
    print(f"{name}님의 등급은 D 입니다.")
if avg < 60:
    print(f"{name}님의 등급은 F 입니다.")
"""
# 해답
"""
name = input("이름 : ")
kor = int(input("국어 : "))
eng = int(input("영어 : "))
mat = int(input("수학 : "))
if not (0 <= kor <= 100) or not (0 <= eng <= 100) or not (0 <= mat <= 100):
    print("성적을 잘 못 입력 하셨습니다.")
else:
    # 빈칸으로 두고 싶을때 pass 넣기. 빈칸은 에러가 나기 때문에 일단 넘어가란 뜻
    # 알맞은 성적이 입력되었으면, 총점과 평균 구하기
    total = kor + eng + mat
    avg = total / 3
    # 평균에 따른 등급 판정
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

# 문자열 비교 : 계절을 영문으로 입력받아 계절에 맞는 문구 출력하기
# spring, summer, fall, autumn, winter 입력 받아서 계절에 맞는 문구 출력
# 단 비교의 편의ㅡㄹ 위해 입력 받은 문자열은 대문자로 변환해서 비교하기
"""
season = input("계절을 입력해 주세요! ").upper()
if season == "SPRING":
    text1 = "봄"
    text2 = "씨를 뿌려라."
elif season == "SUMMER":
    text1 = "여름"
    text2 = "물을 대라."
elif season == "FALL" or season == "AUTUMN":
    text1 = "가을"
    text2 = "곡식을 거두어라."
elif season == "WINTER":
    text1 = "겨울"
    text2 = "곡식을 거두어라."
else:
    print("그건 계절이 아니여요...")
print(f"어느덧 {text1}이어라.\n그대여, {text2}")
"""

# 자판기 문제
print("=" * 6 + " 메뉴 " + "=" * 6)
print("1.콜라\t: 1,100원")
print("2.사이다\t: 1,000원")
print("3.커피\t: 700원")
print("4.생수\t: 600원")
print("=" * 17)

menu1 = "콜라"
price1 = 1100
menu2 = "사이다"
price2 = 1000
menu3 = "커피"
price3 = 700
menu4 = "생수"
price4 = 600
while True:
    order = input("주문할 메뉴의 번호를 입력해 주세요. ")
    if order == "1":
        print(f"주문하신 메뉴는 {menu1}입니다. 가격은 {price1}원 입니다.")
        money1 = int(input("금액을 투입해 주세요. "))
        if money1 < price1:
            print(f"금액이 {price1 - money1}원 부족합니다.")
        elif money1 == price1:
            print(f"{money1}원 받았습니다. 감사합니다.")
        else:
            change = money1 - price1
            print(f"{money1}원 받았습니다. 거스름 돈은 {change}원 입니다.")
            break
    elif order == "2":
        print(f"주문하신 메뉴는 {menu2}입니다. 가격은 {price2}원 입니다.")
        money2 = int(input("금액을 투입해 주세요. "))
        if money2 < price2:
            print(f"금액이 {price2 - money2}원 부족합니다.")
        elif money2 == price2:
            print(f"{money2}원 받았습니다. 감사합니다.")
        else:
            change = money2 - price2
            print(f"{money2}원 받았습니다. 거스름 돈은 {change}원 입니다.")
            break
    elif order == "3":
        print(f"주문하신 메뉴는 {menu3}입니다. 가격은 {price3}원 입니다.")
        money3 = int(input("금액을 투입해 주세요. "))
        if money3 < price3:
            print(f"금액이 {price3 - money3}원 부족합니다.")
        elif money3 == price3:
            print(f"{money3}원 받았습니다. 감사합니다.")
        else:
            change3 = money3 - price3
            print(f"{money3}원 받았습니다. 거스름 돈은 {change3}원 입니다.")
            break
    elif order == "4":
        print(f"주문하신 메뉴는 {menu4}입니다. 가격은 {price4}원 입니다.")
        money4 = int(input("금액을 투입해 주세요. "))
        if money4 < price4:
            print(f"금액이 {price4 - money4}원 부족합니다.")
        elif money4 == price4:
            print(f"{money4}원 받았습니다. 감사합니다.")
        else:
            change4 = money4 - price4
            print(f"{money4}원 받았습니다. 거스름 돈은 {change4}원 입니다.")
            break
    else:
        print("존재하지 않는 메뉴 입니다. 다시 메뉴를 확인해 주세요.")
        print()



# 주/야간 근무시간을 입력받아 급여 계산하기
"""
work_type = int(input("[1]주간근무, [2]야간근무를 입력. "))
work_time = int(input("근무 시간 입력. "))
HOUR_PAY = 10320

if work_type == 1:
    pay = work_type * HOUR_PAY          #주간급여
else:
    pay = work_type * HOUR_PAY * 1.5    #야간급여

print(f"{work_time}시간 동안 근무간 {work_type == 1 and "주간" or "야간"} 급여는 {pay:,.0f}원 입니다.")
"""
