# 람다 : 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현
# 람다 함수를 이용해 익명의 함수를 만들 수 있음
# 람다 함수의 장점은 코드의 간결함, 메모리 절약


# 람다 사용 안 할때 1
def add(a, b):
    return a + b
print(add(14, 16))

# 람다 사용 할때 1
print(f"{(lambda a, b: a + b)(10, 20)}")


# 람다 사용 안 할때 2
def power(n):
    return n * n
print(power(5))

# 람다 사용 할때 2
out = list(map(lambda x: x * x, [1, 2, 3, 4, 5]))
print(out)
