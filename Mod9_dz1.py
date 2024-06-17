def is_odd(x):
    return x % 2


def square_num(x):
    return x * x


my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = map(square_num, filter(is_odd, my_list))

print(list(result))