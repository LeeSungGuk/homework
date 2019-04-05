import jwt


def sign_up(email: str, pw: str):
    input_data = {
        "email" : email,
        "pw" : pw
    }

    key = 'secret'

    jwt_data = jwt.encode(input_data, key, algorithm='HS256')

    return jwt_data






def test_sign_up():
    print("jwt: {}".format(sign_up("jin3137", "dltjdrnr3137", )))




