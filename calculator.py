from lexer import Lexer
from operator import Operator
from number import Number
from constants import OPERATORS, HIGH_PRIORITY_OPERATORS


class Calculator:
    def __init__(self, tokens):
        self.tokens = tokens
        self.stack = []


    def calculate(self):
        self.calculate_first_pass()
        result = self.calculate_second_pass()
        return result.value


    def calculate_first_pass(self):
        for token in self.tokens:
            if isinstance(token, Operator):
                self.stack.append(token)
            else:
                if not self.stack:
                    self.stack.append(token)
                    continue
                operator = self.stack[-1]
                if operator.is_high_priority():
                    operator = self.stack.pop()
                    prev = self.stack.pop()
                    new_num = operator.calc(prev.value, token.value)
                    self.stack.append(new_num)
                else:
                    self.stack.append(token)


    def calculate_second_pass(self):
        value1 = self.stack.pop(0)
        while self.stack:
            operator = self.stack.pop(0)
            value1 = operator.calc(value1.value, self.stack.pop(0).value)
        return value1


if __name__ == '__main__':
    lexer = Lexer('1 + 1 + 4 * 4')
    calculator = Calculator(lexer.tokens)
    print calculator.calculate()
