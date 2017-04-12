from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0
	parse = True

	comments = {
		"fi0": u"lisäsi luokan",
		"fi1": u"lisäsi luokkat",
	}

	cats = ["Luokka:Botin luomat artikkelit"]

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):
		for cat in self.cats:
			if cat not in text:
				text += "\n[["+cat+"]]"
				self.error_count += 1

		return text, self.error_count
