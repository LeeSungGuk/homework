import pytest


# 연속된 데이터 체크
def jully_jumpers_check(data: list):
    for i in range(len(data) - 1):
        jully_number = abs(list_연속숫자_뺄셈(data[i], data[i+1]))
        if jully_number > 1 or jully_number < 0:
            return "not jolly"
    return "jolly"

# 앞뒤 사이 값
def list_연속숫자_뺄셈(val, next_val):
    return val - next_val


# 입력된 배열 앞뒤 데이터 사이 값
def 반복문_설정(data: list):
    val = list()
    for i in range(len(data)-1):
        val.append(abs(list_연속숫자_뺄셈(data[i], data[i+1])))
    return val


def test_return_list():
    #1 4 2 3 을 넣었을때 3 , 2 , 1 앞과 뒤에 숫자를 뺀 값을 먼저 구한다.
    data = [1, 4, 2, 3]
    # data = [4, 1, 4, 2, 3]
    val = 반복문_설정(data)
    # assert val == [3, 3, 2, 1]
    assert [3, 2, 1] == 반복문_설정([1, 4, 2, 3])
    assert [1, 2, 3] == 반복문_설정([1, 2, 4, 1])


# 리턴 졸리 데이터
def jolly_jumpers(data: list):
    val = 반복문_설정(data)
    jolly_str = jully_jumpers_check(val)
    return jolly_str


# 연속 데이터 체크
def test_jolly_number():
    # assert "jolly" == jully_jumpers([2,1])
    assert "jolly" == jully_jumpers_check([3, 2])
    assert "jolly" == jully_jumpers_check([2, 3])
    assert "jolly" == jully_jumpers_check([3, 3, 2, 1])
    assert "not jolly" == jully_jumpers_check([3, 4, 2, 1])
    assert "not jolly" == jully_jumpers_check([4, 4, 2, 1])
    assert "jolly" == jully_jumpers_check([4, 4, 3, 2])
    assert "jolly" == jully_jumpers_check([2, 3, 4, 4])


# 최종 테스트 입력된 배열 값이 졸리인지 아닌지 체크한다.
def test_jolly_jumpers():
    assert "jolly" == jolly_jumpers([1, 4, 2, 3])
    assert "jolly" == jolly_jumpers([1, 2, 3, 1])
    assert "not jolly" == jolly_jumpers([1, 2, 3, -1])
    assert "jolly" == jolly_jumpers([4, 1, 4, 2, 3])
    assert "not jolly" == jolly_jumpers([5, 1, 4, 2, -1, 6])