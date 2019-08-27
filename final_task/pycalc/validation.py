import re
from operators_constants import OPERATORS, ALL_OPERATORS, BINARY_OPERATORS


def validate_input_data(input_data):
    if not input_data:
        return "ERROR: no input data"
    if input_data.count("(") != input_data.count(")"):
        return "ERROR: brackets aren't balanced"
    if re.search(r'[*,/,^,%,<,>,<=,>=,!=,==][*,/,^,%,<,>]', input_data):
        return "ERROR: 2 operators in a row"
    if re.search(r'[*,/,^,%,<,>,<=,>=,!=,==]\s[*,/,^,%,<,>,<=,>=,!=,==]', input_data):
        return "ERROR: 2 operators in a row"
    if input_data[-1] in OPERATORS:
        return "ERROR: expression ends with operator"
    if input_data[0] in '^%*/= |\\':
        return "ERROR: expression starts with operator"
    if re.search(r'\d\s\d', input_data):
        return "ERROR: 2 digits in a row"
    tokens = re.findall(r'[a-z][a-z,0-9]+', input_data)
    for token in tokens:
        if token not in ALL_OPERATORS:
            return "ERROR: unknown function name" + token
    if validate_function_argument(input_data):
        return validate_function_argument(input_data)


def validate_function_argument(input_data):
    """function argument validation"""
    for function_name in OPERATORS:
        if function_name.isalpha() or function_name in ['atan2', 'log1p', 'log10', 'log2', 'expm1']:
            function_name_with_bracket = '{}('.format(function_name)
            if function_name_with_bracket in input_data:
                for part_of_expression in input_data.split(function_name_with_bracket)[1:]:
                    brackets_counter = 0
                    arguments_counter = 1
                    for element in part_of_expression:
                        if element == ')' and not brackets_counter:
                            break
                        elif element == ')':
                            brackets_counter -= 1
                        elif element == ',' and not brackets_counter:
                            arguments_counter += 1
                        elif element == '(':
                            brackets_counter += 1

                    if arguments_counter > 2:
                        return "ERROR: too many arguments in function"
                    elif arguments_counter > 1 and function_name not in BINARY_OPERATORS:
                        return "ERROR: too many arguments in function with 1 argument"
                    elif arguments_counter < 2 and function_name in BINARY_OPERATORS:
                        if not (function_name == "log" and arguments_counter == 1):
                            return "ERROR: too little arguments in function with 2 arguments"
