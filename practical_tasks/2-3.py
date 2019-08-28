def count_letters(input_string: str) -> dict:
    dictionary = {}
    for letter in input_string:
        if letter.isalpha():
            dictionary[letter] = dictionary.get(letter, 0) + 1
    return dictionary


input_string = input('Input string ')
print(count_letters(input_string))
