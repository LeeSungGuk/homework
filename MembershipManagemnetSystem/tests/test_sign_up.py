import jwt
import time
import pytest

from datetime import datetime, timedelta
from jwt import InvalidSignatureError


# 회원가입 토큰 발급
def sign_up(email: str, pw: str) -> str:
    input_data = {
        "email": email,
        "pw": pw
    }
    key = 'secret'

    # 테스트용
    # jwt_data = jwt.encode(input_data, key, algorithm='HS256')

    now = datetime.now()
    exp = timedelta(seconds=2)

    payload = {
        'iss': email,
        'exp': now + exp
    }

    jwt_token = jwt.encode(payload, key, algorithm='HS256')

    return jwt_token


# 토큰생성 (만료 정보만)
def make_jwt_token(email: str) -> str:
    # 토큰 정보 입력
    # now: 현재 시간, exp: 만료 시간 정보
    now = datetime.now()
    exp = timedelta(minutes=60)
    print("now: {}, exp: {}".format(now, exp))

    return jwt.encode({'exp': now + exp}, 'scret')


# 토큰 만료 체크
def exp_token_exception():
    s = make_jwt_token("jin3137@gmail.com")
    time.sleep(3)

    try:
        jwt.decode(s, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise InvalidSignatureError("InvalidSignatureError")


def test_exp_token():
    # exception checking
    with pytest.raises(InvalidSignatureError, match='Signature verification failed'):
        exp_token_exception()


def test_sign_up():
    print("jwt: {}".format(sign_up("jin3137", "dltjdrnr3137", )))









