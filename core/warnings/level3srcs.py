from core.lop import *

class Warning:
	wm = {
	"fi": "tasolla 3 lähteet osio",}

	error_count = 0

	def __init__(self):
		self.error_count = 0

	def run(self, text):
		for line in text.split("\n"):
			if titlein(getword("srcs"), line) and "===" in line:
				self.error_count += 1

		return self.error_count
