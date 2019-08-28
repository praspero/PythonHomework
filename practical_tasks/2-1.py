import string
from typing import Optional, Set


def test_1_1(*args) -> Set[str]:
    if not args:
        return
    result = set(args[0])
    for item in args[1:]:
        result.intersection_update(item)
    return result


def test_1_2(*args) -> Optional[Set[str]]:
    return set().union(*args)


def test_1_3(*args) -> Optional[Set[str]]:
    if not args:
        return
    sets = [set(item) for item in args]
    result = {}
    for item in sets:
        for char in item:
            result[char] = result.get(char, 0) + 1
    return {key for key in result if result[key] > 1}


def test_1_4(*args) -> Set[str]:
    return set(string.ascii_lowercase).difference(*args)


print(test_1_1("hello", "world", "python"))
print(test_1_2("hello", "world", "python"))
print(test_1_3("hello", "world", "python"))
print(test_1_4("hello", "world", "python"))

