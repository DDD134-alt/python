# 추상화(Abstraction)
# 실체가 없는 부모가 자녀에게 상속을 주는것
# 무엇을 해야 하는지 설계 명세서(공통 규격/틀/규칙)만 정하고 실제 내부 구현은 하지 않는 것

# 클래스(Class)
# 추상 클래스(Abstract Class)에서 준 설계 명세서를 토대로 구조, 배치등 구체적인 설계도를 구현하는 것

# 메서드 (Method) = def문
# 외부에서 값이 들어오면 그 값에 대응하는 출력값을 내놓는 서비스
# 하지만 값이 들어온 후 출력되는 동안의 과정을 구태여 드러내지 않고 묻어두는 것도 추상화.

# 높은 응집도 (High Cohesion) : 하나의 클래스/메서드는 자신에게 맡겨진 하나의 역할을 완벽히 수행할줄 알아야 함
# 낮은 결합도 (Loose Coupling) : 클래스 간의 의존성을 줄여, 한쪽 코드를 수정해도 다른 쪽 코드가 영향을 덜 받도록 해야 함
# 결론, 내부에는 응집도가 높아야 하지만 외부와 외부끼리의 결합도는 느슨해야 한다. 그것이 좋은 코딩

from abc import *

class NetworkAdapter(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        pass

class LAN(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company} LAN에 연결했습니다.")

class WIFI(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company} WI-FI에 연결했습니다.")

class LTE(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company} LTE에 연결했습니다.")

net = input("연결할 네트워크를 선택 [1]LAN, [2]WI-FI, [3]LTE ")
if net == "1":
    adapter = LAN("KT Megapass")
    adapter.connect()
elif net == "2":
    adapter = WIFI("SK Telecom")
    adapter.connect()
elif net == "3":
    adapter = LTE("LG U+")
    adapter.connect()
else: print("연결할 네트워크가 없습니다.")

# 멀티태스킹 OS
# 멀티스래딩 어플리케이션을 만들때 필요