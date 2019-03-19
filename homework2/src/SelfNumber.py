'''
코딩 테스트를 준비해야 하는 분들은 이 문제를 풀어보세요.

자연수 n이 있을 때 함수 d는 n의 각 자리 숫자와 n의 합을 구한다.

예를 들어, d(91) = 9 + 1 + 91 = 101 이 된다.

이때 n을 d(n)의 generator라고 한다.

예를 들어, 91은 101의 generator다.

generator가 없는 숫자를 self number라고 하고, 1, 3, 5, 7, 9, 20, 31 등이 여기에 속한다.

1 이상, 5000 미만의 self number의 합을 구하는 프로그램을 만들자.

코딩 전에 다음 순서를 확인하세요.

1. input과 ouput을 충분히 모아보세요. 처음부터 완벽할 필요는 없고, 코딩 도중에 추가하셔도 됩니다.
2. 어떻게 풀어볼지 간단히 생각하고, 곰인형 등을 앞 또는 옆에 두고 친절하게 설명해 보세요.
3. 어떻게 하면 1번에서 모은 input과 output을 항상 순식간에 확인할 수 있을지 고민해 보세요(사실 그냥 자동화된 테스트 코드를 작성하면 됩니다).
4. 구현합니다.
5. 공유합니다.
'''


'''
1. input과 ouput을 충분히 모아보세요. 처음부터 완벽할 필요는 없고, 코딩 도중에 추가하셔도 됩니다.
d(1) = 1 + 1 = 2        1, 3, 5, 7, 9, 11, ...... self number  
d(2) = 2 + 2 = 4
d(3) = 3 + 3 = 6
d(4) = 4 + 4 = 8 
d(5) = 5 + 5 = 10
d(6) = 6 + 6 = 12
d(7) = 7 + 7 = 14
...

2. 어떻게 풀어볼지 간단히 생각하고, 곰인형 등을 앞 또는 옆에 두고 친절하게 설명해 보세요.
1 ~ 5000 미만의 합을 구한 후, 1 ~ 5000 까지의 generator 값을 빼준다.
그러면 self number의 합을 구할 수 있다. 하지만 generator의 값이 5000 이상이 되는 것은 제외한다.
 
'''

# 전체 데이터 합
def sum(first_num, end_num) -> int:
    sum = 0;
    for i, v in enumerate(range(first_num, end_num)):
        # print("index: {}, value: {}".format(i, v))
        sum += v

    return sum

# self number의 합
def self_num_total(first_num, end_num, total_value) -> int :
    #generator 을 구한다.  d(91) = 9 + 1 + 91 = 101 은 generator가 된다. 각각의 자릿수 더하고 숫자값을 더한다.

    sum_self_num = total_value
    for num in range(first_num, end_num):
        sum_of_digit = 0 # 자릿수의 합
        generator = 0
        for digit in str(num):
            sum_of_digit += int(digit)

        generator = sum_of_digit + num
        # print("generator : {}".format(generator))

        if(generator < end_num):
            sum_self_num -= generator

    return sum_self_num


def run():
    #1부터 5000 미만의 합을 구한다.
    first_num = 1
    end_num = 5000

    total_value = sum(first_num, end_num)

    # 1 ~ 5000 미만의 generator 을 구하면서 전체 데이터 값에 빼준다. 그러면 self_num의 총 합이 나온다.
    result = self_num_total(first_num, end_num, total_value)
    print("Sum of self number = {}".format(result))


if __name__ == '__main__':
    run()
