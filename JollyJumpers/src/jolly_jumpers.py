

def jully_jumpers_check(data: list):
    for i in range(len(data) - 1):
        jully_number = abs(subtraction_of_data(data[i], data[i+1]))
        if jully_number > 1 or jully_number < 0:
            return "not jolly"
    return "jolly"


def subtraction_of_list_data(data: list):
    val = list()
    for i in range(len(data)-1):
        val.append(abs(subtraction_of_data(data[i], data[i+1])))
    return val


def subtraction_of_data(val, next_val):
    return val - next_val


def jolly_jumpers(data: list):
    val = subtraction_of_list_data(data)
    jolly_str = jully_jumpers_check(val)
    return jolly_str


if __name__ == '__main__':
    pass
