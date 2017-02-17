from core.lop import *
from core.algcore import *

class Warning:
	wm = {
	"fi": "Luokka ei ole lopussa",}

	error_count = 0

	def __init__(self):
		self.error_count = 0

	def run(self, text):
		text = text.split("\n")
		foundcat = False
		for line in text:
			if getwordc("cat") in line or getwordlcc("cat") in line:
				foundcat = True
			elif foudcat and line != "":
				self.error_count += 1
				return
		return self.error_count
