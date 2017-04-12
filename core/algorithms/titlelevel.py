from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0

	comments = {
		"fi0": u"siirsi otsikon oikealle tasolle",
		"fi1": u"siirsi otsikkoja oikealle tasolle",
	}

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):
		parser = wtparser.Parser()
		text = parser.parse(text)
		text = text.split("\n")
		for l in range(0, len(text)):
			if istitle(text[l]) and text[l].count("=") <= 2:
				self.error_count += 1
				text[l] = text[l].replace("=", "")
				text[l] = "=="+text[l]+"=="

		text = '\n'.join(text)
		text = parser.deparse(text)
		return text, self.error_count
