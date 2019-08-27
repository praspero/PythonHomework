from collections import namedtuple
import operator
import math

Operator = namedtuple("operator", ["priority", 'function'])

CONSTANTS = {
    'pi': math.pi,
    'e': math.e,
    'tau': math.tau,
    'inf': math.inf,
    'nan': math.nan
}

OPERATORS = {
    '+': Operator(priority=2, function=operator.add),
    '-': Operator(priority=2, function=operator.sub),
    '*': Operator(priority=3, function=operator.mul),
    '/': Operator(priority=3, function=operator.truediv),
    '%': Operator(priority=3, function=operator.mod),
    '//': Operator(priority=3, function=operator.floordiv),
    '^': Operator(priority=4, function=operator.pow),
    'round': Operator(priority=5, function=round),
    'abs': Operator(priority=5, function=abs),
}

for key, value in math.__dict__.items():
    if not key.startswith('_') and key not in CONSTANTS and key != 'fsum':
        OPERATORS.update({key: Operator(priority=5, function=value)})

BINARY_OPERATORS = ['+', '-', '*', '/', '//', '%', '^', 'copysign', 'fmod',
                    'gcd', 'isclose', 'ldexp', 'log', 'pow', 'hypot', 'atan2']

COMPARISON_OPERATORS = {
    '<=': Operator(priority=1, function=operator.le),
    '<': Operator(priority=1, function=operator.lt),
    '==': Operator(priority=0, function=operator.eq),
    '>=': Operator(priority=1, function=operator.ge),
    '!=': Operator(priority=0, function=operator.ne),
    '>': Operator(priority=1, function=operator.gt)
}

ALL_OPERATORS = ['(', ')', 'fsum']
for key in CONSTANTS.keys():
    ALL_OPERATORS.append(key)
for key in OPERATORS.keys():
    ALL_OPERATORS.append(key)


NUMBERS = '0123456789.'
