class Lexer:
	def __init__(self, string):
		self.string = string
		self.tokens = self.get_tokens()


	def get_tokens(self):
		tokens = [t for t in self.string.split(' ') if t]
		return tokens


# if __name__ == '__main__':
# 	lexer = Lexer('1 + 1 + 4 * 4')
# 	print lexer.tokens