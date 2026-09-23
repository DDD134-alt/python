
# 동적 바인딩 (Dynamic Binding)
# 부모와 자식 여러명이 동시에 있을때, 자동으로 맨 아래 자식을 따르는 것
# 파이썬은 이런 동적바이딩 성질을 띄고 있기 때문에 자동으로 오버라이딩(메서드 재정의)이 작동함

# 파이썬에 메서드 오버로딩이 없는 이유
# 파이썬은 변수의 타입을 미리 지정하지 않는 '동적 타이핑(Dynamic Typing)' 언어이기 때문.
# (동적 바인딩 때문이 아니며, 오버로딩 대신 default 매개변수나 *args를 사용함)

# 연산자 오버로딩 (Operator Overloading)
# 정수+정수가 다른 곳애서는 문자+문자로 갈때 +의 역할이 연산에서 객체 붙이기로 바뀌는것. 그게 오버로딩
# 같은 연산자 기호(+, -, * 등)가 대상(객체)에 따라 다르게 동작하도록 재정의하는 것.
# 예: 1 + 2 = 3 (숫자 더하기)
#     'a' + 'b' = 'ab' (문자열 이어붙이기)
#     p1 + p2 = Point(x, y) (사용자 정의 객체 합치기)

# 언어별 차이
# - 파이썬 : 일반 메서드 오버로딩이 안되지만 연산자 오버로딩(__add__ 등등)은 됨
# - C++, Java: 일반 메서드 오버로딩, 연산자 오버로딩 다 됨


class Vector2D: # 좌표 이동 클래스
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector2D(1, 2) # 같은 자리 숫자끼리 더할 수 있음
v2 = Vector2D(3, 4) # 이는 좌표 이동과 같음
v3 = v1 + v2
print(v3.x, v3.y)

v4 = 10
v5 = 20
print(v4 + v5) # 한자리 숫자만 있는건 또 평법하게 연산해줌

print(v1 == v2)
