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


d(10) = 1 + 0 + 10 = 11
d(11) = 1 + 1 + 11 = 13
d(12) = 1 + 2 + 12 = 15



...


d(20) = 2 + 0 + 20 = 22
d(21) = 2 + 1 + 21 = 24
...


...

2. 
답변: 어떻게 풀어볼지 간단히 생각하고, 곰인형 등을 앞 또는 옆에 두고 친절하게 설명해 보세요.
1 ~ 5000 미만의 합을 구한 후, 1 ~ 5000 까지의 generator 값을 빼준다.
그러면 self number의 합을 구할 수 있다. 하지만 generator의 값이 5000 이상이 되는 것은 제외한다.

문제점: generator에 중복되는 숫자가 존재한다.

두번째 답변:
그래서 숫자를 더 나열하면서 생각해보니 패턴이 존재 한다. 
10 = 1 (10으로 나누는 몫) + 0 (10으로 나누고 나머지) + 10 (자기자신)  = 11
11 = 1 (10으로 나누는 몫) + 1 (10으로 나누고 나머지) + 11 (자기자신)  = 12


python string을 for 문으로 10 1 , 2 로 읽을 수 있다.
 
'''



def number_set(f, e) -> set:
    return set([v for v in range(f, e)])


def sum_of_numbers(f, e) -> set:
    return sum(number_set(f, e))


def sum_of_digits(f, e) -> int:
    list_generator = []
    for num in range(f, e):
        generator = ((num // 10) + (num % 10) + num)

        if (generator < e):
            list_generator.append(generator)

    # 중복제거
    set_list = set(list_generator)
    # print("set_gene_list: ", list(set_list))

    return sum(set_list)


def digits_set(f, e) -> set:
    list_generator = []
    for num in range(f, e):
        generator = ((num // 10) + (num % 10) + num)
        if (generator < e):
            list_generator.append(generator)

    # 중복제거
    set_list = set(list_generator)
    return set_list


# self number의 합
def self_num_total(first_num, end_num) -> int :
    total_num = sum_of_numbers(first_num, end_num)
    total_generator = sum_of_digits(first_num, end_num)

    # 전체 합 - generator 합 = self number 합
    sum_of_self_num = total_num - total_generator

    return sum_of_self_num


#차집합 구하기
def self_num(f, e):
    self_num_set : set = number_set(f, e) - digits_set(f, e)
    return sum(self_num_set)


def run():
    #1부터 5000 미만의 합을 구한다.
    first_num = 1
    end_num = 5000

    # 1 ~ 5000 미만의 generator 을 구하면서 전체 데이터 값에 빼준다. 그러면 self_num의 총 합이 나온다.
    result = self_num_total(first_num, end_num)
    result1 = self_num(first_num, end_num)
    print("Sum of self number = {}".format(result))
    print("차집합 이용 = {}".format(result1))


if __name__ == '__main__':
    run()
