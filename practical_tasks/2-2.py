def generate_squares(number: int) -> dict:
    return {integer: integer ** 2 for integer in range(number + 1) if integer != 0}


number = int(input('Input integer '))
print(generate_squares(number))
