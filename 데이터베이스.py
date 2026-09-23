# 파이썬에서 MySQL 데이터베이스를 제어하기 위한 라이브러리 불러오기
import pymysql

# 1. DB 연결 (MySQL 서버 접속)
def get_connection():
    conn = pymysql.connect(
        # host: 접속할 서버 IP 주소 ('127.0.0.1'은 내 컴퓨터를 의미)
        host="127.0.0.1",
        # user: 접속할 MySQL 계정 이름 (기본 관리자 계정: 'root')
        user="root",
        # port: MySQL 접속 포트 번호 (기본값: 3306)
        port=3306,
        # password: 해당 계정의 비밀번호
        password="1234",
        # db: 접속할 데이터베이스(스키마) 이름
        database="mysqlDB",
        # charset: 한글 깨짐을 방지하기 위한 문자 인코딩 설정
        charset="utf8"
    )
    return conn

# 2. 테이블 생성 함수
def create_user_table(conn):
    # SQL을 실행할 일꾼(커서)을 생성
    cur = conn.cursor()

    # 2-1. 기존 테이블 삭제 및 생성
    # 기존 폴더에 userTable 테이블이 있다면 지우기
    cur.execute("DROP TABLE IF EXISTS userTable")
    # 새 테이블 생성
    cur.execute("""
        CREATE TABLE userTable (
            id      CHAR(10) PRIMARY KEY,
            pwd     CHAR(15),
            name    CHAR(20),
            email   CHAR(20),
            addr    CHAR(50)
        )
    """)
    # commit: 데이터 변경사항(CREATE, INSERT 등)을 DB에 최종 저장 확정
    conn.commit()

# 3. 초기 데이터 삽입
def insert_user(conn):
    cur = conn.cursor()
    users = [
        ('ayj1234', '12345678', '안유진', 'ayj@gmail.com', '서울시 강남구'),
        ('jwy1234', '12345678', '장원영', 'jwy@gmail.com', '서울시 강남구'),
        ('fall1234', '12345678', '가을', 'fall@gmail.com', '서울시 강남구'),
        ('ys1234', '12345678', '이서', 'ws@gmail.com', '서울시 강남구'),
        ('lay1234', '12345678', '레이', 'lay@gmail.com', '서울시 강남구')
    ]
    # 반복문을 통해 회원 정보를 하나씩 DB에 삽입 (함수 내부 들여쓰기 적용)
    for user in users:
        cur.execute("INSERT INTO userTable VALUES(%s, %s, %s, %s, %s)", user)
    # 데이터 생성 상태 확정, 변경사항 적용
    conn.commit()

def main():
    conn = get_connection()
    create_user_table(conn)
    conn = get_connection()
    insert_user(conn)

if __name__ == "__main__":
    main()

"""
# 테이블 데이터 추가하기
def new_user_insert(conn):
    # 사용자로부터 직접 입력받은 정보를 DB에 추가합니다.
    cur = conn.cursor()
    id = input("\n아이디 (종료시 exit 입력) : ").strip()
    if id == 'exit':
        return "exit"
    pwd = input("비밀번호 : ")
    name = input("이름 : ")
    email = input("이메일 : ")
    addr = input("주소 : ")
    try:
        # execute() 괄호 안에 바인딩 튜플 값 (id, pwd, name, email, addr) 전달
        cur.execute("INSERT INTO userTable VALUES(%s, %s, %s, %s, %s)", (id, pwd, name, email, addr))
        # 저장하기
        conn.commit()
        print(f"'{name}' 회원이 성공적으로 등록되었습니다.")
    # 아이디 중복 오류가 발생할 때 튕기지 않고 오류 내용을 알려주도록 보호하는 예외 처리 구문
    except Exception as e:
        print(f"오류발생 : {e}")

# 5. 메인 실행 함수
def main():
    # DB 연결 통로를 생성
    conn = get_connection()

    # 아래 두 구문은 새로운 개정 등록을 초기화 하므로 막아둠
    # 기존 테이블 삭제 후 새로 생성
    # create_user_table(conn)
    # 기초 데이터 5명 입력을 실행
    # insert_user(conn)

    print("기초 테이블 초기화 및 초기 데이터 삽입 완료!")

    # 사용자 등록 반복 루프
    while True:
        rst = new_user_insert(conn)
        if rst == "exit":
            print("\n회원 등록 프로그램을 종료합니다.")
            break
    # 모든 작업 완료 후 DB 연결 종료
    # close: 사용이 끝난 DB 연결 통로를 닫아 메모리 자원 해제
    conn.close()
"""


"""
# 회원 수정
def update_user(conn):
    cur = conn.cursor()               # DB 연결(conn)을 위한 일꾼(커서 cur) 생성
    id = input("\n아이디 : ").strip()  # id 입력 .strip() 앞뒤 공백 지우기
    name = input("이름 : ")            # 수정할 이름 입력
    email = input("이메일 : ")          # 수정할 이메일 입력
    addr = input("주소 : ")            # 수정할 주소 입력
    # cur.execute : SQL로 Python 구문을 옮길 커서는 이대로 실행해라
    # '' : SQL문 틀
    # 쉼표 뒤에 목록 : 튜플, 입력 받은 값이 어떤 위치로 들어가는지의 목록표. 따라서 input 변수 이름을 기입해야 함
    cur.execute("UPDATE userTable SET name=%s, email=%s, addr=%s WHERE id=%s", (name, email, addr, id))
    if cur.rowcount > 0:
        print(f"'{id}'님 회원 정보가 수정되었습니다.")
    else:
        print("어라, 이상하다. 없는 ID인데요...")
    conn.commit() # 변경된 내용을 DB에 최종 반영(저장)

# 회원 삭제
def delete_user(conn):
    cur = conn.cursor()
    id = input("\n아이디 : ").strip()
    cur.execute("DELETE FROM userTable WHERE id=%s", id)

# 회원 조회
def search_user(conn):


# 회원 전체 조회
def all_search_user(conn):



def print_menu():
    print("\ntk")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

def main():
    conn = get_connection()  # DB 연결
    create_user_table(conn)  # 데이블 생성
    conn = get_connection()  # DB 연결
    insert_user(conn)        # 초기 회원 정보 삼입

    while True:
        conn = get_connection()
        print_menu()
        choice = input("")

        if choice == "1":
            insert_user(conn)
        elif choice == "2":
            update_user(conn)
        elif choice == "3":
            delete_user(conn)
        elif choice == "4":
            search_user(conn)
        elif choice == "5":
            all_search_user(conn)
        elif choice == "0":
            print("")
            conn.close()
            break
        else:
            print("")
"""