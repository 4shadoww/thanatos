from core.lop import *

class Warning:
	wm = {
	"fi": "artikkelissa on kommentti",}

	error_count = 0

	def __init__(self):
		self.error_count = 0

	def run(self, text):
		if "<!--" in text or "-->" in text:
			self.error_count += 1

		return self.error_count
