from src.db import DbConnect

# 처음 테이블 생성 시 한번만 호출
def create_table_user():

    cur = DbConnect().connect()
    # 중복체크


    c = cur.cursor()
    # 테이블 생성
    c.execute('''
                CREATE TABLE users
                    (user_id text, pw text, name text,
                     token text, membership_level text, payment text, reg_date text);
                ''')




def create_insert_user():
    cur = DbConnect().connect()
    c = cur.cursor()
    ret = c.execute("insert into users values ('jin3137@gmail.com', '123', '이성국', '123', '1', 'Y', '2019-04-08' );")

    fetch_one = c.execute("select * from users").fetchone()

    cur.commit()

    cur.close()

    return fetch_one