from constants import OPERATORS, HIGH_PRIORITY_OPERATORS
from number import Number

class Operator:
    def __init__(self, operator):
        if not self.is_operator(operator):
            raise Exception('Invalid operator')
        self.operator = operator


    def is_high_priority(self):
        # operator is '*', '/', '%'
        return self.operator in HIGH_PRIORITY_OPERATORS


    def is_operator(self, token):
        return True if token in OPERATORS else False


    def calc(self, value1, value2):
        result = 0
        if self.operator == '+':
            result = value1 + value2
        elif self.operator == '-':
            result = value1 - value2
        elif self.operator == '*':
            result = value1 * value2
        elif self.operator == '/':
            result = value1 / value2
        elif self.operator == '%':
            result = value1 % value2
        return Number(result)