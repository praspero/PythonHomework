def split_by_index(user_string: str, indexes_list: list) -> list:
    new_list = []
    left_boundary = 0
    length_of_string = len(user_string)
    for index, number in enumerate(indexes_list):
        if number >= length_of_string:
            return "Invalid indexes"
        right_boundary = number
        new_list.append(user_string[left_boundary:right_boundary])
        left_boundary = number
    new_list.append((user_string[left_boundary:]))
    return new_list


user_string = input("Input string")
indexes_list = list(map(int, input('Input indexes ').split()))
print(split_by_index(user_string, indexes_list))
