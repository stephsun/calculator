from constants import OPERATORS


class Lexer:
    def __init__(self, string):
        self.string = string
        self.tokens = self.get_tokens()


    def get_tokens(self):
        tokens = [t for t in self.string.split(' ') if t]
        return tokens