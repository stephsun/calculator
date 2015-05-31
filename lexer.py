from operator import Operator
from number import Number
from constants import OPERATORS


class Lexer:
    def __init__(self, string):
        self.string = string
        self.tokens = self.get_tokens()


    def get_tokens(self):
        # tokenize the original input
        tokens = []
        for t in self.string.split(' '):
            if not t: continue
            if t in OPERATORS:
                tokens.append(Operator(t))
            else:
                tokens.append(Number(t))
        return self.is_valid(tokens)        


    def is_valid(self, tokens):
        # validate input
        if not len(tokens):
            raise Exception('Empty expression')
        if isinstance(tokens[-1], Operator):
            raise Exception('Expression can not end with operator')
        expect_num = True
        for token in tokens:
            if expect_num and not isinstance(token, Number):
                raise Exception('Invalid number')
            if not expect_num and not isinstance(token, Operator):
                raise Exception('Invalid operator')
            expect_num = not expect_num
        return tokens