from typing import Optional


def get_pairs(user_list: list) -> Optional[list]:
    new_list = []
    if len(user_list) <= 1:
        return
    previous_item = user_list[0]
    for item in user_list[1:]:
        new_list.append((previous_item, item))
        previous_item = item
    return new_list


user_list = list(input('Input list ').split())
print(get_pairs(user_list))
