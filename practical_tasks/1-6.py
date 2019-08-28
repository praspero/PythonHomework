def get_biggest_word(user_input: str) -> str:
    if not user_input:
        return "Error: Your string is empty"
    user_input = user_input.split()
    biggest_length = 0
    for word in user_input:
        if len(word) > biggest_length:
            biggest_word = word
            biggest_length = len(word)
    return biggest_word


user_input = input("Input string:")
print(get_biggest_word(user_input))
