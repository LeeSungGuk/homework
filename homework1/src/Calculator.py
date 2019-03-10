import re


# 더하기
def add(curr_val, next_val):
    return curr_val + next_val


# 빼기
def sub(curr_val, next_val):
    return curr_val - next_val


# 곱하기
def mul(curr_val, next_val):
    return curr_val * next_val


# 나누기
def div(curr_val, next_val):
    return curr_val / next_val


# 내장 함수 사용
def inner_fnc(data_str):
    return eval(data_str)


# curr_val: 현재 도출된 값, oper_val: +. - * , / , next_val: 다음 값
def value(curr_val, oper_val, next_val):
    if oper_val is None:
        curr_val = next_val
    elif oper_val == "+":
        return add(curr_val, next_val)
    elif oper_val == "-":
        return sub(curr_val, next_val)
    elif oper_val == "*":
        return mul(curr_val, next_val)
    elif oper_val == "/":
        return div(curr_val, next_val)

    return curr_val


def cal(input_list):

    # 문자열을 순차적으로 검색한다.
    resut_val = 0
    oper_val = None
    for s in input_list:
        next_val = 0
        p = re.compile("[0-9/+\-\*\/\%\\s]")
        maching_data = p.match(s)
        m_str = maching_data.string

        # 문자와 특수문자 입력시 발생
        if m_str is None:
            print("입력된 데이터가 잘못되었습니다. 다시입력 바랍니다.")
            break

        if m_str == " ":
            continue

        if m_str in ("+", "-", "*", "/", "%"):
            # 계산할 + , - , * .. 할당
            oper_val = m_str
        else:
            next_val = float(m_str)
            resut_val = value(resut_val, oper_val, next_val)

    return resut_val


def run():
    print("hello 계산기")

    while True:
        print("숫자를 입력하세요 문자는 스페이스로 띄어 주세요")
        input_data = input()
        input_list = list()

        try:
            input_list = input_data.split(" ")

            # 입력값이 충분하지 않을 때
            if len(input_list) < 2:
                print("계산할 값이 모자랍니다. 다시 입력해주세요.")
                continue

        except Exception as e:
            print("e", e)

        # 입력값 계산
        result_val = cal(input_list)

        print("답: ", result_val)
        #print("내장 함수 사용:", eval(x))


if __name__ == '__main__':
    run()


