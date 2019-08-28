def combine_dicts(*args):
    new_dict = {}
    for dictionary in args:
        for key in dictionary:
            new_dict[key] = new_dict.get(key, 0) + dictionary.get(key)
    return new_dict


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))
