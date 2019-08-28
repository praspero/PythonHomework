def foo(user_list: list) -> list:
    product = 1
    new_list = []
    for digit in user_list:
        product *= digit
    for digit in user_list:
        new_list.append(product // digit)
    return new_list


user_list = list(map(int, input('Input digits ').split()))
print(foo(user_list))
