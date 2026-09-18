# 상속 (Inheritance)
# 부모 클래스에서 만든 변수와 메서드를 자식이 완벽하게 똑같이 물려받아 사용하는 것
# 단, 부모와 자식은 항상 동등하거나 자식이 더 우세함(자식이 더 많은 기능을 가질 수 있음)

# 오버라이딩 (Method Overriding / 메서드 재정의)
# 개선된 상속 값, 부모에게 물려받은 상속을 자식의 입맛에 맞게 업그래이드 하는 것
# 실행할때 동적 바인딩(Dynamic Binding)에 의해 자식의 오버라이딩된 메서드가 최우선으로 싱행됨

# 부모가 물려준걸 자식이 그대로 받으면 상속, 개선하면 오버라이딩

# 오버로딩 (Method Overloading / 메서드 중복 정의)
# 하나의 이름으로 각각 기능이 다른, 여러 재료(매개변수)를 받아 중복 정의하는 것
# 파이썬에는 없는 기능이지만 다른 함수로 유사 구현 가능

# 멤버 (Member)
# 클래스를 구성하는 전체 요소
# 멤버 변수 (속성 / State) : 상태 (이름, 나이, 색상 같은거)
# 멤버 매서드 (행위 / Behavior) : 행위를 일으키는 스위치 (달리기, 멈추기 같은거)

class ProtoTV: # 상속을 주기 위한 부모 클래스
    # 전원, 체널, 볼륨을 매개변수로 하는 생성자 생성
    def __init__(self, on, channel, volume):
        self.is_on = on
        self.channel = channel
        self.volume = volume

    # 전원을 켜고 끄는 메서드
    def set_on(self, on):
        self.is_on = on

    # 체널 설정 메서드 (1 ~ 1000)
    def set_channel(self, channel):
        if 1 <= cnl <= 1000:
            self.channel = cnl
            print(f"채널을 {cnl}번으로 변경하였습니다.")
        else:
            print("채널 설정 범위에 벗어났습니다.")

    # 볼륨 설정 메서드 (0 ~ 100)
    def set_volume(self, volume):
        if 1 <= vol <= 100:
            self.volume = vol
            print(f"볼륨을 {vol}으로 변경하였습니다.")
        else:
            print("볼륨 설정 범위에 벗어났습니다.")


class ProductTV(ProtoTV):       # 클래스 ProtoTV의 상속을 받는 자식
    def set_chanel(self, cnl):  # 채녈 제한을 2000까지 늘려 오버라이딩 하기
        if 0 < cnl <= 2000:
            self.channel = cnl
            print(f"채널을 {cnl}번으로 변경하였습니다.")
        else:
            print("채널 설정 범위에 벗어났습니다.")

    # 정보를 출력하는 메서드 만들기
    def print_tv(self):
        print(f"전원 : {'ON' if self.is_on else 'OFF'}")
        print(f"채널 : {self.channel}")
        print(f"볼륨 : {self.volume}")

productTV = ProductTV(False, 10, 10)
productTV.set_on(True)
productTV.set_volume(45)
productTV.set_channel(1200)
productTV.print_tv()
