# NumPy(Numerical Python)는 파이썬에서 수치 계산과 과학적 연산을 위한 핵심 라이브러리
# - 데이터 언어는 '숫자'와 '행렬'이며, 이를 효율적으로 처리하기 위해 넘파이(NumPy) 사용
# - 빅데이터 환경에서 파이썬 기본 리스트로 for문을 돌리는건 매우 느림
# - 넘파이(NumPy)의 백터화 연산을 쓰면 수백만개의 데이터도 순식한에 처리 가능
# - 대규모 다차원 배역 처리, 고속 수학 연산지원
# - 머신러닝, 딥러닝, 데이터 분석에 필수적으로 사용 됨

# NumPy는 파이썬 내장 모듈이 아니므로 별도로 설치 필요
# 일반적으로 np라믐 별칭으로 불림
import numpy as np

# 기본 배열 생성
print("========== a1 ==========")
data1 = [0, 1, 2, 3, 4, 5]
a1 = np.array(data1) # 리스트를 넘파일 배열로 만듦
print(data1)         # 리스트는 콤마로 구분
print(a1)            # 넘파이는 콤마 없이 구분

print("\n========== a2 ==========")
data2 = [0, 1, 2, 3, 4, 5.5]
a2 = np.array(data2)
print(a2)   # 정수와 실수가 섞여 있으면 실수로 통일됨

print("\n========== a3 ==========")
data3 = [0, 1, 2, 3, 4, 5.5, "1111", "2222"]
a3 = np.array(data3)
print(a3)   # 숫자와 문자열이 섞여 있으면 문자열로 통일됨

# 속성 확인
print("\n========== x ==========")
x = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
print(x)
print(x.shape)
# .shape 배열의 형태를 튜플로 반환 1차원은 (열 개수,), 2차원은 (열 개수, 행 개수)
print(x.dtype)
# .dtype 배열 요소의 데이터 타입 반환
# int64   : 64비트(8바이트) 크기의 메모리를 사용하는 정수
# float64 : 64비트(8바이트) 크기의 메모리를 사용하는 실수
# <U4     : 4바이트 크기의 유니코드(Unicode)

# 특정 범위의 배열 생성
print("\n========== a4 ==========")
a4 = np.arange(0, 10, 2) # 0부터 10 미만 사이 2 간격으로 숫자 출력
print(a4)

print("\n========== a5 ==========")
a5 = np.arange(1, 101, 3) # 1부터 100 미만 사이 3 간격으로 숫자 출력
print(a5)

print("\n========== a6 ==========")
a6 = np.arange(0, 50, 5) # 0부터 50 미만 사이 5 간격으로 숫자 출력
print(a6)

# 2차원 배열 생성
print("\n========== a7_1 ==========")
a7_1 = np.arange(12).reshape(4, 3)  # .reshape(행(가로), 열(세로))
print(a7_1)
print(a7_1.shape)

print("\n========== a7_2 ==========")
a7_2 = np.arange(12).reshape(-1, 3) # 열(세로)을 3칸으로 맞추어 행을 자동으로 나열하라
print(a7_2)

print("\n========== a7_3 ==========")
a7_3 = np.arange(12).reshape(4, -1) # 행(가로)을 4줄으로 맞추어 열을 자동으로 나열하라
print(a7_3)

# 동일한 간격으로 데이터 생성
print("\n========== a8 ==========")
a8 = np.linspace(1, 10, 11) # 1부터 10미만 사이의 11개 숫자를 넣는데, 이때 간격이 동일한 숫자로 추출
print(a8)                                  # [ 1. 1.9  2.8  3.7  4.6  5.5  6.4  7.3  8.2  9.1  10.]

# NumPy 기초 실습
print("\n========== arr1 ==========")
# 1. 리스트 [10, 20, 30, 40, 50]을 NumPy 배열로 만들어 arr1에 저장하고, 배열과 type(arr1)을 출력하세요.
arr1 = np.array([10, 20, 30, 40, 50])
print(arr1)
print(type(arr1))

# 2. np.array([True, 1, 2])의 출력 결과와 dtype은 무엇일까요?
print("\n========== arr2 ==========")
arr2 = np.array([False, True, 1, 2])
print(arr2)       # [0 1 1 2]
print(type(arr2))

# 3. 2행 3열 배열 [[1, 2, 3], [4, 5, 6]]을 만들고 shape와 dtype을 출력하세요.
print("\n========== arr3 ==========")
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3.shape)
print(arr3.dtype)

# 4. np.arange()를 사용해 2부터 20까지(20 포함) 짝수 배열을 만드세요.
print("\n========== arr4 ==========")
arr4 = np.arange(2, 21, 2)
print(arr4)

# 5. np.arange()를 사용해 [10 9 8 7 6 5 4 3 2 1]을 만드세요.
print("\n========== arr5 ==========")
arr5 = np.arange(10, 0, -1)
print(arr5)

# 6. np.arange()로 0부터 1 미만까지 0.1 간격의 배열을 만들고, 요소가 몇 개인지 출력 결과로 확인하세요.
print("\n========== arr6 ==========")
arr6 = np.arange(0, 1, 0.1)
print(arr6.shape)
print(len(arr6))

# 특정 숫자로 채워진 배열
print("\n========== a9 ==========")
a9 = np.zeros(10)      # 0으로 10열로 1차원 배열로 체우기
print(a9)

print("\n========== a10 ==========")
a10 = np.zeros((3, 4)) # 0으로 3행 4열로 2차원 배열 체우기
print(a10)

print("\n========== a11 ==========")
a11 = np.ones(10)      # 1로 10열로 1차원 배열로 체우기
print(a11)

print("\n========== a12 ==========")
a12 = np.eye(4)
print(a12)

# 배열의 데이터 타입 변환
print("\n========== a13 ==========")
a13 = np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
print(a13)
print(a13.dtype)

print("\n========== num_a13 ==========")
num_a13 = a13.astype(float)
print(num_a13)
print(num_a13.dtype)

print("\n========== a14 ==========")
a14 = np.array(['1', '3', '5', '7', '9'])
print(a14)
print(a14.dtype)

print("\n========== num_a14 ==========")
num_a14 = a14.astype(int)
print(num_a14)
print(num_a14.dtype)

# 난수 배열의 생성
# rand : 0 ~ 1 미만의 실수로 난수 배열을 생성
print("\n========== a15 ==========")
a15 = np.random.rand(2, 3)
print(a15)

print("\n========== a16 ==========")
a16 = np.random.rand(2, 3)
print(a16)

# randint() : 지정된 범위에 해당하는 정수로 난수 배열을 생성
print("\n========== a17 ==========")
a17 = np.random.randint(10, size=(5, 4)) # 0 ~ 9 사이의 난수를 5행 4열로 생성
print(a17)


# 실습 문제 2
# 1. 0으로 채워진 요소 5개짜리 1차원 배열을 만들고, 배열과 dtype을 출력하세요.
print("\n========== a18 ==========")
a18 = np.zeros(5)
print(a18)
print(a18.dtype)

# 2. 0으로 채워진 3행 5열 배열을 만들고 shape를 출력하세요.
print("\n========== a19 ==========")
a19 = np.zeros((3, 5)) # 두 개의 매게변수를 하나의 매게 변수로 전달해야 하기 때문에 괄호 안에 괄호를 써서 작성함
print(a19)
print(a19.shape)

# 3. 1로 채워진 2행 4열 배열을 만든 뒤, astype()을 사용해 정수형으로 변환하여 출력하세요.
print("\n========== a20 ==========")
a20 = np.ones((2, 4)).astype(int)
print(a20)
print(a20.dtype)

# 4. np.eye()로 5 × 5 배열을 만들어 출력하고, 이런 형태의 행렬을 무엇이라고 부르는지, dtype은 무엇인지 확인하세요.
print("\n========== a21 ==========")
a21 = np.eye(5)
print(a21)
print(a21.dtype)

# 5. 배열 np.array(['10', '20', '30', '40'])의 dtype을 출력한 뒤, 정수형으로 변환하고 변환 후의 dtype도 출력하세요.
print("\n========== a22 ==========")
a22 = np.array(['10', '20', '30', '40'])
print(a22.dtype)

print("\n========== num_a22 ==========")
num_a22 = a22.astype(int)
print(num_a22.dtype)

# 6. 0 ~ 1 미만의 실수 난수로 4행 3열 배열을 만들고 shape를 출력하세요.
print("\n========== a23 ==========")
a23 = np.random.rand(4, 3)
print(a23)

# 7. np.random.randint()를 사용해 주사위를 10번 던진 결과(1 ~ 6)를 1차원 배열로 만드세요.
print("\n========== a24 ==========")
a24 = np.random.randint(7, size=(5))
print(a24)

# 8. 0 ~ 99 사이의 정수 난수 12개를 1차원 배열로 만든 뒤, 다음을 순서대로 수행하세요.
print("\n========== a25 ==========")
a25 = np.random.randint(100, size=(12))
print(a25)


# 연산과 함수
a24 = [1, 2, 3]
a25 = [4, 5, 6]
print(a24 + a25)

a24_1 = np.array([1, 2, 3])
a25_1 = np.array([4, 5, 6])
print(a24_1 + a25_1)
print(a24_1 * a25_1)
print(a24_1 / a25_1)


a26 = np.array([10, 20, 30, 40, 50])
print(a26 > 20)

# 동계 연산
a27 = np.arange(10)
print(f"합계 : {a27.sum()}, 평균 : {a27.mean()}")
print(f"표준편차 : {a27.std()}, 분산 : {a27.var()}")
print(f"최솟값 : {a27.min()}, 최대값 : {a27.max()}")

aa = np.random.randint(2, size=(10, 10))
print(aa)
print(f"앞면이 나올 확률 : {aa.sum()}%")
print(f"뒷면이 나올 확률 : {100 - aa.sum()}%")

aa2 = np.arange(1, 11, 1)
aa3 = np.array([5])
print(aa2 + aa3)

aa4 = np.arange(1, 4, 1)
aa5 = np.arange(4, 7, 1)
aa6 = np.arange(7, 10, 1)
print(aa4)
print(aa5)
print(aa6)

aa7 = np.arange(20)
print(f"합계 : {aa7.sum()}, 평균 : {aa7.mean()}")
print(f"최솟값 : {aa7.min()}, 최대값 : {aa7.max()}")

aa8 = np.random.randint(101, size=(10))
print(aa8)
result = aa8[aa8 >= 50]
print(result)

