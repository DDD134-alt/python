import pymysql

def get_connection():
    conn = pymysql.connect(
        host="127.0.0.1", user="root", port=3306, password="1234", database="mysqlDB", charset="utf8"
    )
    return conn

def create_board_table(conn):
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS boardTable")

    # 게시판 테이블
    cur.execute("""
        CREATE TABLE boardTable (
        board_no BIGINT PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(100) NOT NULL,
        contents TEXT NOT NULL,
        board_writer CHAR(10) NOT NULL,
        reg_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (board_writer) REFERENCES userTable(id) ON DELETE CASCADE
        )
    """)
    conn.commit()
    print("boardTable 테이블 생성완료")

def create_comment_table(conn):
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS commentTable")

    # 댓글 테이블
    cur.execute("""
        CREATE TABLE commentTable (
        comment_no BIGINT PRIMARY KEY AUTO_INCREMENT,
        board_no BIGINT NOT NULL,
        comment_writer CHAR(10) NOT NULL,
        comment VARCHAR(500) NOT NULL,
        reg_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (board_no) REFERENCES boardTable(board_no) ON DELETE CASCADE,
        FOREIGN KEY (comment_writer) REFERENCES userTable(id) ON DELETE CASCADE
        )
    """)
    conn.commit()
    print("commentTable 테이블 생성완료")

# def creat():
#     conn = get_connection()
#     create_board_table(conn)
#     create_comment_table(conn)
# if __name__ == "__main__":
#     creat()


# 회원가입 강행하기
def join_user(conn, id):
    cur = conn.cursor()
    agree = input("계속 진행할까요?(Y/N): ").upper()
    if agree == "Y":
        print(f"아래 정보를 입력해 주세요.")
        pwd = input("비밀번호 : ").strip()
        name = input("이름 : ")
        email = input("이메일 : ")
        addr = input("주소 : ")
        cur.execute("INSERT INTO userTable (id, pwd, name, email, addr) VALUES (%s, %s, %s, %s, %s)",
                    (id, pwd, name, email, addr))
        conn.commit()
        print(f"가입 성공! '{id}'님 가입을 축하드립니다.")
        print(f"자동 로그인 되었습니다.")
    elif agree == "N":
        print("")
        continue
    else:
        print(f"문자를 똑바로 입력해 주세요.")


# 로그인 하기
def login(conn):
    cur = conn.cursor()
    while True:
        id = input("아이디를 입력하세요. ").strip()
        cur.execute("SELECT id, pwd FROM userTable WHERE id=%s", (id,))
        user = cur.fetchone() # 입력한 아이디의 아이디, 비번 정보를 user 튜플에 행으로 담기
        if user is None:
            print(f"아이디가 존재하지 않습니다.\n[{id}]으로 회원 가입을 진행하려합니다.")
            join_user(conn, id) # 회원가입 진행
            return id
        else:
            pwd = input("비밀번호를 입력하세요. ")
            if user[1] == pwd:
                print(f"로그인 성공! {user[0]}님 어서오세요!")
                return user[0]
            else:
                print("비밀번호가 틀렸습니다.")


# 게시글 작성하기
def write_post(conn, id):
    cur = conn.cursor()
    print("게시글 작성하기")
    title = input("제목 : ")
    contents = input("내용 : ")
    cur.execute(
        "INSERT INTO boardTable (title, contents, board_writer) VALUES (%s, %s, %s)",
                (title, contents, id))
    conn.commit()
    print(f"{id}님의 게시글이 작성되었습니다.")


# 게시글 조회하기
def list_posts(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT B.board_no, B.title, U.name, B.reg_date
        FROM userTable U
        JOIN boardTable B
             ON U.id = B.board_writer
        ORDER BY B.board_no DESC""")
    posts = cur.fetchall() # 전체 게시글 목록의 행을 튜플로 담아 리스트에 담기

    print(f"|{'글번호'}| {'제목':<10} [{'작성자'}] {'작성일'}")
    print("-" * 40)

    if not posts:
        print("게시글이 없습니다.")
        return False

    for post in posts:
        board_no, title, writer_name, reg_date = post
        # reg_date를 문자열로 포맷팅해서 보기 좋게 출력
        date_str = reg_date.strftime("%m.%d %H:%M") if reg_date else ""
        print(f"|{board_no:^5}| {title:<10} [{writer_name}] {date_str}")

    print("-" * 40)
    return True


# 게시글 댓글 조회하기
def view_post(conn):
    cur = conn.cursor()
    try:
        list_no = int(input("조회할 게시물 번호 입력: "))
    except ValueError:
        print("숫자로 입력해 주세요.")
        return

    cur.execute(
        """
        SELECT B.board_no, B.title, B.contents, U.name, B.reg_date
        FROM boardTable B
                 JOIN userTable U ON B.board_writer = U.id
        WHERE B.board_no = %s
        """,
        (list_no,),
    )
    post_detail = cur.fetchone()  # 게시글은 1개이므로 fetchone() 사용

    if post_detail is None:
        print("존재하지 않는 게시글 번호입니다.")
        return

    # 본문 데이터 언패킹
    board_no, title, contents, writer_name, reg_date = post_detail

    print(f"[{board_no}번] 제목: {title}")
    print(f"작성자: {writer_name} | 작성일: {reg_date}")
    print("-----------------------------------------------------------")
    print(f"내용:\n{contents}")
    print("===========================================================")

    cur.execute(
        """
        SELECT U.name, C.comment, C.reg_date
        FROM commentTable C
                 JOIN userTable U ON C.comment_writer = U.id
        WHERE C.board_no = %s
        ORDER BY C.comment_no ASC
        """,
        (list_no,),
    )

    comments = cur.fetchall()  # 댓글은 여러 개일 수 있으므로 fetchall() 사용

    print("[댓글 목록]")
    if not comments:
        print("등록된 댓글이 없습니다.")
    else:
        for com in comments:
            com_writer, com_text, com_date = com
            date_str = com_date.strftime("%m.%d %H:%M") if com_date else ""
            print(f"- {com_writer} : {com_text} ({date_str})")


# 댓글 작성하기
def write_comment(conn, id):
    cur = conn.cursor()
    board_no = int(input("댓글을 달 게시글 번호: "))
    comment = input("댓글 내용: ")
    cur.execute(
        "INSERT INTO commentTable (board_no, comment_writer, comment) VALUES (%s, %s, %s)",
        (board_no, id, comment),)
    conn.commit()
    print(f"[{id}]님의 댓글이 등록되었습니다.")


# 게시글 삭제하기
def delete_post(conn, id):
    cur = conn.cursor()
    del_post = input("삭제할 게시글 번호: ")
    # 본인이 쓴 글인지 확인하거나, id 조건 체크 후 삭제
    cur.execute(
        "DELETE FROM boardTable WHERE board_no = %s AND board_writer = %s",
        (del_post, id),
    )
    conn.commit()
    print(f"{id}님의 게시글이 삭제되었습니다.")


# 회원 탈퇴
def delete_user(conn, id):
    cur = conn.cursor()
    cur.execute("DELETE FROM userTable WHERE id = %s", (id,))
    conn.commit()
    print(f"바이바이! {id}님!")


# 메뉴 출력하기
def menu():
    print("[1]게시글 쓰기 | [2]게시글 보기 | [3]댓글 달기 | [4]게시글 지우기 | [5]회원탈퇴 | [0]종료")



def main():
    conn = get_connection()
    print("환영합니다!")
    user_id = login(conn)

    while True:
        menu()
        choice = input("번호를 입력해주세요. ").strip()

        if choice == "1":
            write_post(conn, user_id)
        elif choice == "2":
            if list_posts(conn):
                view_post(conn)
        elif choice == "3":
            write_comment(conn, user_id)
        elif choice == "4":
            delete_post(conn, user_id)
        elif choice == "5":
            delete_user(conn, user_id)
            conn.close()
            break
        elif choice == "0":
            print("프로그램을 종료 합니다.")
            conn.close()
            break
        else:
            print("정확한 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()