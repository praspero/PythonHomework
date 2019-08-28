def string_split(user_string: str, split_char: str) -> list:
    left_boundary = 0
    new_list = []
    for right_boundary, c in enumerate(user_string):
        if c == split_char:
            new_list.append(user_string[left_boundary:right_boundary])
            left_boundary = right_boundary + 1
    new_list.append(user_string[left_boundary:])
    return new_list


user_string = input("Input a string")
split_char = input("Input a char for split")
print(string_split(user_string, split_char))
