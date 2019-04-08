from src.db.user_db import create_table_user, create_insert_user

'''
def test_create_user():
    # email, pw, token
    email = "jin3137@gmail.com"
    pw = "1"
    token = "123"

    # 데이터 저장 튜플에 값을 넣는다. ex) [(), (), ()]
    ret_date = create_table_user()
    print("ret_date: {}".format(ret_date))


    assert ret_date is None
'''


def test_create_insert_user():
    r = create_insert_user()
    assert len(r) > 0