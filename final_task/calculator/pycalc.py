from calculator.operators_constants import OPERATORS, ALL_OPERATORS, BINARY_OPERATORS, \
                                           NUMBERS, COMPARISON_OPERATORS, CONSTANTS, Operator
from calculator.validation import validate_input_data
from calculator.argparser import parse_args
import operator


def prepare_expression_to_converting(input_formula):
    input_formula = input_formula.lower().replace(' ', '')
    input_formula = input_formula.replace(')(', ')*(')
    input_formula = input_formula.replace('**', '^')
    input_formula = input_formula.replace('(-', '(0-')

    for function_name in ['pow', 'log(', 'copysign', 'ldexp', 'atan2', 'hypot', 'fmod', 'gcd']:
        if function_name in input_formula:
            if function_name == 'log(':
                function_name = 'log'
            input_formula = process_function_with_2_arguments(input_formula, function_name)

    for index, element in enumerate(input_formula):
        if element == '^' and input_formula[index + 1].isalpha():
            input_formula = process_degree_operation(input_formula)
            break

    if input_formula.count("^") > 1:
        input_formula = process_degree_priority(input_formula)

    new_list = [input_formula[0]]
    for element in input_formula[1:]:
        if element == '-' and new_list[-1] == '-':
            new_list[-1] = '+'
        elif element == '-' and new_list[-1] == '+':
            new_list[-1] = '-'
        elif element == '+' and new_list[-1] == '-':
            new_list[-1] = '-'
        elif element == '+' and new_list[-1] == '+':
            new_list[-1] = '+'
        else:
            new_list.append(element)
    if new_list[0] == "+":
        new_list.pop(0)
    elif new_list[0] == '-':
        new_list.insert(0, '0')

    input_formula = "".join(new_list)

    input_formula = input_formula.replace('/-', '*(0-1)/')
    input_formula = input_formula.replace('*-', '*(0-1)*')
    if '^-' in input_formula:
        input_formula = process_degree_minus(input_formula)

    if 'fsum' in input_formula:
        input_formula = process_fsum(input_formula)

    return input_formula


def process_degree_priority(formula_with_several_degrees):
    """Function add new degree
    If we have more than one degree, then program add one more degree with high priority.
    2^3^4 -> 2^3^^4, where '^^' has more priority then '^'
    """

    result_formula = []

    for index, key in enumerate(formula_with_several_degrees.split('^')):
        result_formula.append(key)
        if index != len(formula_with_several_degrees.split('^')) - 1:
            result_formula.append('^' * (index + 1))
            OPERATORS.update({'^' * (index + 1): Operator(priority=4 + index, function=operator.pow)})
            BINARY_OPERATORS.append('^' * (index + 1))
            ALL_OPERATORS.append('^' * (index + 1))

    return ''.join(result_formula)


def process_degree_operation(formula_with_degree):
    """Function replace degree by function into degree by function with brackets
       For example: 1^gcd(5,10) into ==> 1^(gcd(5.10))
    """
    expression_without_brackets = []
    argument_checker = False
    brackets_counter = 0
    for index, element in enumerate(formula_with_degree):
        if argument_checker:
            expression_without_brackets.append(element)

        if element == '(':
            brackets_counter += 1
        elif element == ')':
            brackets_counter -= 1
        elif element == '^' and formula_with_degree[index + 1].isalpha():
            argument_checker = True

        if element == ')' and not brackets_counter and argument_checker:
            break

    formula_with_degree = formula_with_degree.replace("{}".format(''.join(expression_without_brackets)),
                                                      "({})".format(''.join(expression_without_brackets)), 1)

    brackets_checker = False
    for index, element in enumerate(formula_with_degree):
        if element == '^' and formula_with_degree[index + 1].isalpha():
            brackets_checker = True
            break
    if brackets_checker:
        formula_with_degree = process_degree_operation(formula_with_degree)

    return formula_with_degree


def process_degree_minus(expression_with_degree_minus):
    """Function replace negative number with degree in formula into zero with brackets
    For example:
        ^-10 ==> into ^(0-10)
        ^-(7+10) == > into ^(0-(7+10))
    """
    expression_for_replacing = []
    degree_minus_checker = False
    brackets_counter = 0
    for index, element in enumerate(expression_with_degree_minus):

        if degree_minus_checker:
            if element == ')' and not brackets_counter:
                expression_for_replacing.append(element)
                break
            elif element == ')':
                brackets_counter -= 1
            elif element == '(':
                brackets_counter += 1

            if expression_for_replacing and (element in BINARY_OPERATORS or element in COMPARISON_OPERATORS) \
                    and not brackets_counter:
                break
            else:
                expression_for_replacing.append(element)

        if element == '^' and expression_with_degree_minus[index + 1] == '-':
            degree_minus_checker = True

    expression = expression_with_degree_minus.replace(("^{}".format(''.join(expression_for_replacing))),
                                                      "^(0{})".format(''.join(expression_for_replacing)), 1)

    if '^-' in expression:
        expression = process_degree_minus(expression)

    return expression


def process_fsum(formula_with_fsum):
    brackets_counter = 0
    square_brackets_counter = 0
    arguments_counter = []
    last_argument = []

    for element in formula_with_fsum.split('fsum([', 1)[1:][0]:
        if element == ']' and not square_brackets_counter:
            break

        if element == ',' and not brackets_counter:
            arguments_counter.append("".join(last_argument))
            last_argument = []
        else:
            last_argument.append(element)

        if element == '(':
            brackets_counter += 1
        elif element == ')':
            brackets_counter -= 1
        elif element == '[':
            square_brackets_counter += 1
        elif element == ']':
            square_brackets_counter -= 1

    arguments_counter.append("".join(last_argument))

    fsum_result = 0
    for argument in arguments_counter:
        fsum_result += float(calculate_reversed_polish_notation(argument))

    replace_expression = "fsum([{}])".format(','.join(arguments_counter), 1)

    formula_with_fsum = formula_with_fsum.replace(replace_expression, str(fsum_result), 1)

    if 'fsum' in formula_with_fsum:
        formula_with_fsum = process_fsum(formula_with_fsum)

    return formula_with_fsum


def process_function_with_2_arguments(input_formula, function_name):
    first_argument = []
    second_argument = []
    first_argument_checker = True
    bracket_checker = 0

    for item in ("".join(input_formula.split(function_name)[1:])):
        if item == '(':
            bracket_checker += 1
        elif item == ')':
            bracket_checker -= 1
        elif item == ',':
            first_argument.pop(0)
            first_argument_checker = False

        if item == ')' and not bracket_checker and not first_argument_checker:
            break
        elif item == ')' and not bracket_checker:
            first_argument.append(item)
            break
        elif first_argument_checker:
            first_argument.append(item)
        elif item != ',':
            second_argument.append(item)

    if function_name == 'log' and not second_argument:
        second_argument.append('e')
        replace_expression = function_name + ''.join(first_argument)
    else:
        replace_expression = function_name + '(' + ''.join(first_argument) + ',' + ''.join(second_argument) + ')'

    x = calculate_reversed_polish_notation(''.join(first_argument))
    y = calculate_reversed_polish_notation(''.join(second_argument))

    if function_name == 'gcd':
        x = int(x)
        y = int(y)

    final_expression = str(OPERATORS[function_name].function(x, y))
    final_expression = input_formula.replace(replace_expression, str(final_expression), 1)

    if function_name == 'log':
        if 'log(' in final_expression:
            final_expression = process_function_with_2_arguments(final_expression, function_name)
    else:
        if function_name in final_expression:
            final_expression = process_function_with_2_arguments(final_expression, function_name)
    return final_expression


def break_expression_into_tokens(preparing_formula):
    current_token = []
    for element in preparing_formula:

        if element in NUMBERS:
            if len(current_token) > 2 and ''.join(current_token[:3]) == 'log':

                current_token.append(element)
                if ''.join(current_token) in ALL_OPERATORS:
                    yield ''.join(current_token)
                    current_token = []

            elif current_token and (current_token[0] not in NUMBERS):
                yield ''.join(current_token)
                current_token = [element]
            else:
                current_token.append(element)

        else:
            if element in '()':
                if current_token and (current_token[0] in NUMBERS):
                    yield float(''.join(current_token))
                elif current_token:
                    yield ''.join(current_token)

                current_token = [element]

            elif len(current_token) > 2 and ''.join(current_token[:3]) == 'log':
                current_token.append(element)
                if ''.join(current_token) in ALL_OPERATORS:
                    yield ''.join(current_token)
                    current_token = []

            elif current_token and current_token[0] in NUMBERS:
                yield float(''.join(current_token))
                current_token = [element]

            else:

                if ''.join(current_token) + element in ALL_OPERATORS:
                    current_token.append(element)

                elif ''.join(current_token) in CONSTANTS:
                    if element == 'e' and current_token:
                        current_token.append(element)
                    else:
                        yield CONSTANTS.get(''.join(current_token))
                        current_token = [element]

                elif ''.join(current_token) in ALL_OPERATORS:
                    yield ''.join(current_token)
                    current_token = [element]
                else:
                    current_token.append(element)

    if current_token and (current_token[0] in NUMBERS):
        yield float(''.join(current_token))
    elif ''.join(current_token) in CONSTANTS:
        yield CONSTANTS.get(''.join(current_token))
    else:
        yield ''.join(current_token)


def convert_to_reversed_polish_notation(tokenize_formula):
    stack = []
    for token in tokenize_formula:
        if token in CONSTANTS:
            token = CONSTANTS.get(''.join(token))
        if token in OPERATORS:
            while stack and stack[-1][0] != '(' and OPERATORS[token].priority <= OPERATORS[stack[-1]].priority:
                yield stack.pop()
            stack.append(token)
        elif token == ")":
            while stack:
                last_element = stack.pop()
                if last_element == "(":
                    break
                yield last_element
        elif token == "(":
            stack.append(token)
        else:
            yield float(token)
    while stack:
        yield stack.pop()


def calculate_reversed_polish_notation(input_expression):
    if validate_input_data(input_expression):
        return validate_input_data(input_expression)
    if type(process_comparison_operators(input_expression)) == bool:
        return process_comparison_operators(input_expression)
    reversed_polish_notation = convert_to_reversed_polish_notation(break_expression_into_tokens(
        prepare_expression_to_converting(input_expression)))

    stack = []
    for element in reversed_polish_notation:
        if element in OPERATORS:
            if element in BINARY_OPERATORS:
                first_number, second_number = stack.pop(), stack.pop()
                try:
                    stack.append(OPERATORS[element].function(second_number, first_number))
                except ValueError:
                    return "ERROR: Value Error"
            else:
                first_number = stack.pop()
                try:
                    stack.append(OPERATORS[element].function(first_number))
                except ValueError:
                    return "ERROR: Value Error"
        else:
            stack.append(element)

    return int(stack[0]) if stack[0] == int(stack[0]) else stack[0]


def process_comparison_operators(formula_with_comparison):
    for item in COMPARISON_OPERATORS:
        if item in formula_with_comparison:
            return COMPARISON_OPERATORS[item].function(
                calculate_reversed_polish_notation(formula_with_comparison.split(item)[0]),
                calculate_reversed_polish_notation(formula_with_comparison.split(item)[1]))
    return formula_with_comparison


def main():
    user_input = parse_args()
    print(calculate_reversed_polish_notation(user_input))


if __name__ == '__main__':
    main()
