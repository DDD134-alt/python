# 에어컨 만들기
# 전원 : ON / OFF
# 현재 온도 표시 기능 (기본값은 20도)
# 온도 설정 기능 (1도씩 설정 가능)
# 바람 세기 설정 : 1단계, 2단계, 3단계
# 생성자, getter, setter, 설정 정보 보여 주기

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