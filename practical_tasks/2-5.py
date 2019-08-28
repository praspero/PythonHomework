def call_once(func):
    cache, is_called = None, False

    def wrapper(*args, **kwargs):
        nonlocal cache, is_called
        if not is_called:
            cache = func(*args, **kwargs)
            is_called = True
        return cache
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return int(a) + int(b)


print(sum_of_numbers(13, 52))
print(sum_of_numbers(13, 4456, 458))
