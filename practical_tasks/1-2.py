def palindrome_check(user_string: str) -> bool:
    new_string = ""
    for s in user_string:
        if s.isalpha():
            new_string = new_string + s
    new_string = new_string.lower()
    for index in range(0, len(new_string)//2):
        if new_string[index] != new_string[-(index+1)]:
            return False
    return True


user_string = input()
print(palindrome_check(user_string))
