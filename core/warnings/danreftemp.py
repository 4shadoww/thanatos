from core.lop import *

class Warning:
	wm = {
	"fi": "tukematon viitteet malline",}

	error_count = 0

	def __init__(self):
		self.error_count = 0

	def run(self, text):
		if "<references>" in text:
			self.error_count += 1
		return self.error_count
