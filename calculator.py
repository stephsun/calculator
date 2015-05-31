from lexer import Lexer
from constants import OPERATORS, HIGH_PRIORITY_OPERATORS


class Calculator:
    def __init__(self, tokens):
        self.tokens = tokens
        self.stack = []


    def calculate_once(self):
        for token in self.tokens:
            if token in OPERATORS:
                self.stack.append(token)
            else:
                if not self.stack:
                    self.stack.append(token)
                    continue
                operator = self.stack[-1]
                if operator in HIGH_PRIORITY_OPERATORS:
                    operator = self.stack.pop()
                    prev = self.stack.pop()
                    new_num = self.calc(operator, prev, token)
                    self.stack.append(new_num)
                else:
                    self.stack.append(token)


    def calculate_twice(self):
        value1 = self.stack.pop(0)
        while self.stack:
            operator = self.stack.pop(0)
            value1 = self.calc(operator, value1, self.stack.pop(0))
        return value1


    def calc(self, operator, value1, value2):
        value1 = int(value1)
        value2 = int(value2)

        if operator == '+':
            return value1 + value2
        elif operator == '-':
            return value1 - value2
        elif operator == '*':
            return value1 * value2
        elif operator == '/':
            return value1 / value2
        elif operator == '%':
            return value1 % value2


if __name__ == '__main__':
    lexer = Lexer('5 - 6')
    cal = Calculator(lexer.tokens)
    cal.calculate_once()
    print cal.calculate_twice()