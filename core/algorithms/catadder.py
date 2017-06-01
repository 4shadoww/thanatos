from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0
	parse = True

	comments = {
		"fi0": u"lisäsi luokan",
		"fi1": u"lisäsi luokkat",
	}

	cats = []

	def __init__(self):
		self.error_count = 0

	def run(self, page, text):
		self.cats = ["Luokka:"+page.title()[0:len(page.title())-2]+"0"*2+"-luku"]

		if "[[Luokka:" in text:
			return text, self.error_count

		for cat in self.cats:
			if cat not in text:
				text += "\n[["+cat+"]]"
				self.error_count += 1

		return text, self.error_count
