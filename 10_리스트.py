# 리스트 : 연속적으로 저장되는 형태의 자료형
# - 크기 지정이 필요 없음
# - 같은 데이터형일 필요 없음
# []대괄호로 감싸서 표현, 0개 이상의 원소가 저장될 수 있음(값 없는 빈 리스크도 만들 수 있다는 뜻)
# - 읽고 쓰기 가능!

# 과목 수를 알 수 없는 성적을 입력받아, 총접과 평균 구하기
"""
score = list(map(int, input("성적입력 : ").split()))
print(f"총점 : {sum(score)}, 평균 : {sum(score) / len(score)}")
"""

# 필요한 리스트 뽑기
"""
mixed = ["연유자", 45, True, [200, 300, 400], ["피해자", "피의자"], {"주소": "경기도"}]
print(mixed)

# 연유자 이름 출력
print(mixed[0])

# 200,300,400 출력
print(mixed[3])
# 숫자는 '3'이나 '0'으로 따로 뽑아낼 수 없음

# "연유자", 45, True 출력
print(mixed[0:2])

# 피해자 출력
print(mixed[4][1])

# 경기도 출력 - 딕셔너리이기 때문에
print(mixed[5]["주소"])

# 피의자의 '의' 출력
print(mixed[4][1][1])
"""

# 딧셔너리 출력
"""
members = [
    {
        "name": "정경수1",
        "addr": "경기도 수원시1"
    },
    {
        "name": "정경수2",
        "addr": "경기도 수원시2"
    },
    {
        "name": "정경수3",
        "addr": "경기도 수원시3"

    },
    {
        "name": "정경수4",
        "addr": "경기도 수원시4"

    },
    {
        "name": "정경수5",
        "addr": "경기도 수원시5"

    }
]

# 정경수1 출력
print(members[0]["name"])
"""

# 요소 추가하기
list_a = [1, 2, 3]

# append : 자동으로 맨 뒤에 추가
list_a.append(4)    # 출력: [1, 2, 3, 4] (맨 뒤에 4 추가)
list_a.append(5)    # 출력: [1, 2, 3, 4, 5] (맨 뒤에 5 추가)

# insert(인덱스 위치, 넣을 값) : 특정 위치(인덱스)에 값을 끼워 넣음.
# 지정한 위치 뒤의 값들을 모두 한 칸씩 밀어내야 해서 데이터가 많으면 비효율적임(시간 복잡도 O(n)).
list_a.insert(1, 1000)  # 출력: [1, 1000, 2, 3, 4, 5] (1 뒤에 1000 추가)
print(list_a)

# 리스트 제거하기
# pop : 인덱스가 없으면 맨 마지막값 제거, 있으면 지정한 인덱스의 값을 지우면서 그 값을 반환(출력) 함.
print(list_a.pop(0))    # 출력: 1
print(list_a)           # 출력: [1000, 2, 3, 4, 5] (1이 제거됨)

# remove : 지우려는 '값'을 직접 지정하여 제거. 아무것도 반환하지 않음(None).
print(list_a.remove(1000))  # 출력: None (삭제 성공 시 pop과 달리 반환값을 출력하지 않음)
print(list_a)               # 출력: None (삭제 성공 시 반환값 없음)

# del : 파이썬 키워드로 지정한 인덱스의 요소를 완전히 삭제함.
del list_a[1]
print(list_a)   # 출력: [2, 4, 5] (1번 인덱스였던 3이 제거됨)

# clear : 리스트 안의 모든 요소를 비워서 빈 리스트로 만듬.
list_a.clear()
print(list_a)   # 출력: [] (모든 요소가 삭제됨)

# 중복제거
my_list = ["A", "B", "C", "D", "E"]
new_list = []
for v in my_list:
    if v not in new_list:
        new_list.append(v)
print(new_list)

test_list = {"B", "A", "D", "B", "C", "D", "E"}
print(test_list)

# 10개의 임의의 숫자를 입력받아 홀수, 짝수를 각 리스트에 나누어 담아 출력하기
number = map(int, input("숫자를 입력해 주세요. ").split())
even = []
odd = []
for e in number:
    if e % 2 == 0:
        even.append(e)
    else:
        odd.append(e)
print(f"짝수 : {even}\n홀수 : {odd}")

# 더 줄이기
number = map(int, input("숫자를 입력해 주세요. ").split())
even = list(filter(lambda x: x % 2 == 0, number)) # lambda : 1회용 함수
odd = list(filter(lambda x: x % 2 == 1, number))
print(f"짝수 : {even}\n홀수 : {odd}")
