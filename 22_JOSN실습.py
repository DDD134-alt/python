# 1단계. 데이터 구성
# - 도서 정보를 담는 딕셔너리를 최소 5개 만들어 리스트로 구성하세요.
# - 각 도서는 다음 필드를 포함해야 합니다.
#     - `title` (문자열)
#     - `author` (문자열)
#     - `publisher` (문자열)
#     - `year` (정수)
#     - `price` (정수)
#     - `genre` (문자열 2개로 구성된 리스트)

import json  # 필수! json 모듈 불러오기

books = [
    {
    "title": "도시 인문학 수업",
    "author": "도시연구소",
    "publisher": "믹스커피",
    "year": 2026,
    "price": 22500,
    "genre": "인문교양"
    },
    {
    "title": "투명한 나선",
    "author": "히가시노 게이고",
    "publisher": "북다",
    "year": 2026,
    "price": 13860,
    "genre": "일본소설"
    },
    {
        "title": "독하게 돈 공부",
        "author": "박소연",
        "publisher": "메이븐",
        "year": 2026,
        "price": 14490,
        "genre": "재테크전략"
    },
    {
    "title": "어떻게 살아낼 것인가",
    "author": "짐 콜린스",
    "publisher": "필름",
    "year": 2026,
    "price": 18900,
    "genre": "자기관리"
    },
    {
    "title": "오뒷세이아",
    "author": "호메로스",
    "publisher": "을유문화사",
    "year": 2026,
    "price": 15750,
    "genre": "인문교양"
    }
]


# 2단계. 직렬화
# - 위 리스트를 `json.dumps()`를 사용해 JSON 문자열로 변환하고 출력하세요.
# - 한글이 깨지지 않도록 옵션을 설정하고, 보기 좋게 들여쓰기 하세요.

json_str = json.dumps(books, ensure_ascii=False, indent=4)
print(json_str)


# 3단계. 역직렬화
# - 2단계에서 만든 JSON 문자열을 다시 Python 객체로 변환하세요.
# - `for`문을 사용해 각 도서 정보를 한 줄씩 출력하세요.

obj = json.loads(json_str)
for e in obj:
    print(e)


# 4단계. 데이터 가공 (응용)
# - 역직렬화한 데이터에서 가격이 15,000원 이상인 책만 필터링하세요.
# - 필터링한 결과를 "제목 - 가격원" 형식으로 출력하세요. (예: `클린 코드 - 33,000원`)

for e in obj:
    if e["price"] >= 15000:
        print(f"{e['title']} - {e['price']:,}원")


# 5단계. 파일 저장 및 읽기
# - 전체 도서 리스트를 `books.json` 파일로 저장하세요.
# - 저장한 파일을 다시 읽어서 출력하세요.

with open('books.json', 'w', encoding='utf-8') as json_file:
    json.dump(books, json_file, ensure_ascii=False, indent=4)
print("books.json 파일 저장 완료!")

with open('books.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)


# 6단계. 심화 (선택)
# - `books.json`을 읽은 후, 사용자로부터 저자 이름을 입력받아 해당 저자의 책만 출력하는 기능을 추가하세요.

# books.json 파일 읽어오기
with open('books.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# 사용자 입력 및 검색 루프
while True:
    book_aut = input("찾고자 하는 책의 저자를 입력하세요 (종료: q) : ").strip()

    # 종료 조건
    if book_aut.lower() == 'q':
        print("프로그램을 종료합니다.")
        break

    found = False  # 검색 결과가 있는지 확인하는 플래그(Flag) 변수

    # data 리스트를 순회하며 입력한 저자와 일치하는 책 찾기
    for e in data:
        if e["author"] == book_aut:
            print(f"- 제목: {e['title']} / 출판사: {e['publisher']} / 가격: {e['price']:,}원")
            found = True

    # 검색 결과가 없을 때
    if not found:
        print(f"'{book_aut}' 저자의 책을 찾을 수 없습니다.\n")
    else:
        print()  # 줄바꿈용