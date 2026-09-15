# 자료형(Data Type)은 데이터를 저장한는 방식과 연산할 수 있는 방법을 정의하는 데이터 형태를 의미
# Python에는 변수를 선언할때 자료형을 명시하지 않아도 되며, 값이 할당될 때 자동으로 자료형이 결정
text = True # "", 100, 3.14, True, None, False
print(type(text))

# 문자열 : 문자가 연속으로 존재하는 것, 파이썬은 문자와 문자열을 구분하지 않은. "", '', """ """, ''' '''
text1 = "안녕하세요, 파이썬 입니다."
print(text1)
print(text1[0])     # 해당 인덱스의 내용 추출
print(text1[7:10])  # 슬라이싱
print(text1 + "!!!!!!!")
print(text1 * 3)

# 숫자형(Number) : 정수, 실수, 복수형이 있음 셋 다 사칙연산 가능
num1 = 10
num2 = 4
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2) # 몫 구하기
print(num1 % num2)  # 나머지
print(num1 ** num2) # num1의 num2제곱

# 불리언(Boolean) : 참과 거짓 두가지의 값만 가짐
age = int(input("나이 : "))
is_adult = False
if age > 18:
    is_adult = True
else:
    is_adult = False

print(bool(1))      # True
print(bool(0))      # False 0은 거짓, 0을 제외한 모든 숫자는 참
print(bool(-1))     # True
print(bool(""))     # False 문자열은 내용이 없으면 거짓, 내용이 있으면 모두 참
print(bool(" "))    # True
print(bool(None))   # False None은 아직 내용이 정해지지 않아서 거짓

# 형변환 : 데이터를 다른 자료형으로 변환 할 때 사용
print("100" + str(200))
print(int("100") + 200)

age = int(input("나이를 입력하게나."))
print(f"{'성인 이로구나!' if age > 18 else '머리에 피도 안 말라구나!'}")

sentence = "Python programming is fun!"
print(sentence[0:6])
