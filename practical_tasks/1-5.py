def get_digits(user_string: str) -> tuple:
    if user_string.isdigit():
        return tuple(map(int, user_string))
    else:
        return "ERROR: input only digits without spaces"


user_string = input("input digits without spaces")
print(get_digits(user_string))
