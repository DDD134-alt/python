# 에어컨 만들기
# 전원 : ON / OFF
# 현재 온도 표시 기능 (기본값은 20도)
# 온도 설정 기능 (1도씩 설정 가능)
# 바람 세기 설정 : 1단계, 2단계, 3단계
# 생성자, getter, setter, 설정 정보 보여 주기

# 수업내용
class AirCon: # 공장 초기화 값
    def __init__(self, power, temp, step):
        self.power = power     # 전원
        self.temp = temp       # 설정온도
        self.wind_step = step  # 바람세기
        self.curr_temp = 5     # 현재온도. 이거 말고도 현제 날짜와 온도값을 받을 수도 있다

    def set_on(self, is_on):
        self.power = is_on

    def temp(self, temp):
        self.temp = temp

    def wind(self, wind_step):
        self.wind_step = step

    def view_info(self):
        wind_str = "", "1단계", "2단계", "3단계"
        print(f"전원 : {self.power and 'ON' or 'OFF'}")
        print(f"현재 온도 : {self.curr_temp}")
        print(f"설정 온도 : {self.temp}")
        print(f"바람 세기 : {wind_str[self.wind_step]}")


my_air_con = AirCon(False, 22, 1)
my_air_con.set_power(True)
my_air_con.set_wind_step(3)
my_air_con.set_temp(24)
my_air_con.view_info()

# 에아가 말아준 코딩~
class Customer:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.point = 0  # 초기 포인트는 0점
        self.history = []  # 방문 이력을 담을 리스트

    # 방문 및 시술 시 포인트 적립 (5%)
    def add_visit(self, service, price):
        self.history.append(service)  # 방문 이력 추가
        earned = int(price * 0.05)  # 결제 금액의 5% 포인트 계산
        self.point += earned
        print(
            f"{self.name}님, {service} 완료! {earned}포인트 적립 완료! [잔액 : {self.point}포인트]"
        )

    # 포인트 사용
    def use_point(self, amount, price):
        # 1. 포인트를 충분히 가지고 있는 경우
        if self.point >= amount:
            self.point -= amount
            pay_price = price - amount
            print(
                f"{amount}포인트 사용! [남은 포인트 : {self.point}포인트] / 최종 결제 금액: {pay_price}원"
            )

        # 2. 보유 포인트보다 더 많이 사용하려고 할 때 (전액 사용 처리)
        else:
            used_point = self.point  # 가진 포인트 전부 사용
            pay_price = price - used_point
            self.point = 0  # 포인트는 0이 됨
            print(
                f"보유 포인트({used_point}점) 전액 사용! 남은 실제 결제 금액은 {pay_price}원 입니다."
            )


# --- [객체 생성 및 사용 예시] ---

# 1. Customer 클래스를 통해 실제 고객 객체(hair_customer) 생성
hair_customer = Customer("김민서", "010-1234-5678")

# 2. 커트 시술 후 포인트 적립 (add_visit 메서드 호출)
# 20,000원의 5%인 1,000포인트 적립됨
hair_customer.add_visit("여성 커트", 20000)

# 3. 염색 시술 후 포인트 적립
# 80,000원의 5%인 4,000포인트 추가 적립 (총 5,000포인트)
hair_customer.add_visit("전체 염색", 80000)

# 4. 다음 방문 때 3,000포인트 사용하여 펌 결제
hair_customer.use_point(3000, 60000)

# 5. 고객의 전체 방문 이력 확인
print(f"{hair_customer.name}님의 전체 시술 이력:", hair_customer.history)
