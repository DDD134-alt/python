# 튜플 : 변경할 수 없는 자료
# 괄호(())를 사용하여 정의, 요소는 쉼표(,)로 구분

sl = [1, 2, 3]
tp1 = (1, 2, 3)
tp2 = 1, 2, 3
ts1 = 1
ts2 = "1"
ts3 = 1,

print(type(sl))     # 리스트
print(type(tp1))    # 튜플
print(type(tp2))    # 소괄호로 감싸지 않아도 튜플
print(type(ts1))    # 숫자
print(type(ts2))    # 글자
print(type(ts3))    # 소괄호로 감싸지 않아도 콤마가 있으면 튜플

member = ("안유진", 23, "대전시", True) # 패킹(여러가지를 하나로 묶는 것, 리스트와 다르게 패킹은 내용물을 변경하지 않는 성질이 있음)
name, age, addr, is_adult, phone = member  # 언패킹

member.append("1004")
print(member)

def get_name_card(name, phone):
    position = f"{name} 수석연구원"
    addr = "서울시 강남구"
    phone = f"082+{phone}"
    return position, addr, phone
result = get_name_card("곰돌이", "1234-5678")
print(result)
