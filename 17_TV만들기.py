class Television: # 클래스 이름은 대문자로 시작
    def __init__(self, name, on, channel, volume):
    # __init__ : 생성자, 설계도면이 객체를 만들때 호출되는거, 내부에 있는 초기값을 구현(공장 초기화 값)
    # 파이썬은 생상자가 하나라 하나만 만들기 가능, 하나에 두가지 이상 버전은 못 만듦
        # self : 설계도로 만들어지는 객체마다 들어가는 문법이라 자기 자신(self)이라 명명
        self.name = name
        self.is_on = on
        self.channel = channel
        self.volume = volume

    def set_on(self, on):
        self.is_on = on

    def set_channel(self, cnl):
        self.channel = cnl

    def set_volume(self, vol):
        if 0 <= vol <= 100:
            self.volume = vol
        else:
            print("볼륨값 입력 범위를 초과했습니다.")

    def get_on(self):
        return self.is_on

    def get_channel(self):
        return self.channel

    def get_volume(self):
        return self.volume

    def view_tv(self):
        power = ("OFF","ON")
        print(f"이름 : {self.name}")
        print(f"전원 : {power[self.is_on]}")
        print(f"채널 : {self.channel}")
        print(f"볼륨 : {self.volume}")

lg_tv = Television("LG", False, 10, 10)
samsung_tv = Television("SAMSUNG", False, 20, 20)
samsung_tv.view_tv()
lg_tv.view_tv()

# 객체지향 문법 : 느슨한 결합관계, 의존 관계를 낮추기 위해. 이게 추상화 단계.