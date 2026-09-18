
# 메서드 종류
# 인스턴스 메서드 (Instance Method)
# 메서드의 기본값, 객체와 같은 성질을 띄지만 객체는 데이터 무게가 있음
# 객체마다 작동해야하는 스위치 같은거라 각 객체마다 독립적으로 부여받아야 함
# self를 사용

# 정적 메서드 (staticmethod)
# 설계도면에만 남아있는 메서드, 클래스 내부에 있는 맴버와 무관하게 움직인다.
# 객체의 성질을 띄지 않는다. 따라서 인스턴스 메서드와 다르게 하나만 있어도 됨.
# 인스턴스가 외부의 입력값을 저장하고 그에맞는 결과값을 내놓는거라면,
# 정적 메서드는 계산기처럼 입력값만 받기만 하고 결과값을 내놓으면 됨.
# @staticmethod를 사용, self나 cls는 사용 안함

# 클래스 메서드 (classmethod)
# 클래스 전체 설정이나 대체 생성자를 만들 때 사용
# @classmethod와 cls(클래스 자신) 사용

"""
class Car:
    isinstance_count = 0

    def __init__(self, size, model):
        self.size = size
        self.model = model
        Car.isinstance_count += 1
        print(f"자동차 객체 생성 수 : {Car.isinstance_count}")

    def move(self, speed):
        self.speed = speed
        print(f"자동차 {self.size}&{self.model}가 시속 {self.speed}")

    @classmethod # 내부에 정해진 값을 만들긴 하는데
    def print_cnt(cls):
        print(f"자동차 {Car.isinstance_count}대가 만들어졌습니다.")

    @staticmethod
    def check_type(code):
        if (code <= 10):
            print("전기차 입니다.")
        elif (code <= 20):
            print("가솔린차 입니다.")
        elif (code <= 30):
            print("디젤차 입니다.")
        else:
            print("분류 코드가 없습니다.")


car1 = Car("소형", "모닝")
car2 = Car("중형", "쏘나타")
Car.print_cnt()

car1.move(90)
Car.check_type(11)
car2.move(70)
Car.check_type(28)
"""

class Student:
    # 클래스 변수 (모든 학생이 공유하는 정보)
    school_name = "파이썬 고등학교"

    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수 (개별 정보)
        self.age = age

    # 1. 인스턴스 메서드: 객체 고유의 데이터를 다룸 (self 사용)
    def print_info(self):
        print(f"학생 이름: {self.name}, 나이: {self.age}")

    # 2. 클래스 메서드: 클래스 전체 정보를 다루거나 대체 생성자로 사용 (cls 사용)
    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school  # 학교 이름 변경

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # 출생 연도로 나이를 계산해 객체를 만드는 대체 생성자
        current_year = 2026
        age = current_year - birth_year + 1
        return cls(name, age)  # Student(name, age) 객체 생성 후 반환

    # 3. 정적 메서드: 객체/클래스 데이터와 무관한 단순 유틸리티/계산기 기능
    @staticmethod
    def is_adult(age):
        return age >= 20


# --- 실행 및 비교 ---

# 1. 인스턴스 메서드 사용 (객체 생성 필수)
student1 = Student("김철수", 18)
student1.print_info()  # 출력: 학생 이름: 김철수, 나이: 18

# 2. 클래스 메서드 사용 (대체 생성자 및 클래스 정보 변경)
student2 = Student.from_birth_year("이영희", 2005)
student2.print_info()  # 출력: 학생 이름: 이영희, 나이: 22

Student.change_school("코딩 고등학교")
print(Student.school_name)  # 출력: 코딩 고등학교

# 3. 정적 메서드 사용 (객체 생성 없이 클래스명으로 바로 호출하는 계산기)
print(Student.is_adult(22))  # 출력: True
print(Student.is_adult(15))  # 출력: False