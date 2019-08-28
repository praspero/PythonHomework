def quotas_replace(user_string: str) -> str:
    for index, symbol in enumerate(user_string):
        if symbol == "\'":
            user_string = user_string[:index] + "\"" + user_string[index+1:]
            continue
        if symbol == "\"":
            user_string = user_string[:index] + "\'" + user_string[index+1:]

    return user_string


user_string = input("Input a string:")
print(quotas_replace(user_string))



