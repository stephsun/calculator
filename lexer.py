from constants import OPERATORS


class Lexer:
    def __init__(self, string):
        self.string = string
        self.tokens = self.get_tokens()


    def get_tokens(self):
        tokens = [t for t in self.string.split(' ') if t]
        return self.is_valid(tokens)


    def is_number(self, token):
        flag = True
        try:
            token = int(token)
        except ValueError:
            try:
                token = float(token)
            except ValueError:
                flag = False
        finally:
            return flag
        

    def is_operator(self, token):
        return True if token in OPERATORS else False


    def is_valid(self, tokens):
        if not len(tokens):
            raise Exception('Empty expression')
        if tokens[-1] in OPERATORS:
            raise Exception('Expression can not end with operator')
        expect_num = True
        for token in tokens:
            if expect_num and not self.is_number(token):
                raise Exception('Invalid number')
            if not expect_num and not self.is_operator(token):
                raise Exception('Invalid operator')
            expect_num = not expect_num
        return tokens