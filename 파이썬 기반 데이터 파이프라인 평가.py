# 답지
# 1. order.txt 파일 읽기
print("=== 1. 파일 읽기 ===\n")
try:
    with open('order.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            print(line)
except FileNotFoundError:
    print("order.txt 파일을 찾을 수 없습니다.")

print()

# 2. 텍스트 클렌징 적용
# - 첫 번째 줄(헤더) 건너뛰기
# - 각 항목 앞뒤 공백 제거
# - 가격에서 "원" 제거
# - 수량과 가격은 정수형(int)으로 변환
print("=== 2. 텍스트 클렌징 ===\n")
with open('order.txt', 'r', encoding='utf-8') as file:
    header = file.readline()  # 헤더(상품, 수량, 가격) 읽어서 넘기기

    for line in file:
        line = line.strip()
        if not line:
            continue

        # 쉼표(,) 기준 분할 및 각 항목 앞뒤 공백 제거
        parts = line.split(',')
        menu = parts[0].strip()

        # "원" 및 공백 제거 후 정수 변환
        amount = int(parts[1].strip())
        price = int(parts[2].replace('원', '').strip())

        print(f"상품: {menu} | 수량: {amount}개 | 가격: {price:,}원")

print()

# 3. 이상치 제거
# - 가격이 0보다 작거나 10,000보다 큰 경우 제외
# - 수량(개수)이 0보다 작은 경우 제외
print("=== 3. 이상치 제거 후 출력 ===\n")
with open('order.txt', 'r', encoding='utf-8') as file:
    header = file.readline()

    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(',')
        menu = parts[0].strip()
        amount = int(parts[1].strip())
        price = int(parts[2].replace('원', '').strip())

        # 이상치 조건 검사 (조건에 맞지 않으면 건너뜀)
        if price < 0 or price > 10000 or amount < 0:
            continue

        print(f"상품: {menu} | 수량: {amount}개 | 가격: {price:,}원")

print()

# 4. 총매출(전매출) 출력하기
# - (수량 * 가격)의 총합 계산
print("=== 4. 총매출 계산 ===\n")
total_sales = 0

with open('order.txt', 'r', encoding='utf-8') as file:
    header = file.readline()

    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(',')
        menu = parts[0].strip()
        amount = int(parts[1].strip())
        price = int(parts[2].replace('원', '').strip())

        # 단가 * 수량을 누적
        total_sales += amount * price

print(f"총매출: {total_sales:,}원")

