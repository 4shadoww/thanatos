# Unicode converter

import html
from core import algcore

class Algorithm:
	zeroedit = False
	error_count = 0
	comments = {
		"fi0": u"muunsi [[unicode|unicode-syntaksin]] unicode merkeiksi",
	}

	def __init__(self):
		self.error_count = 0

	def run(self,text, article):
		parser = wtparser.Parser()
		text = parser.parse(text)

		newtext = html.unescape(text)
		if newtext != text:
			self.error_count = 1

		text = parser.deparse(text)
		return newtext, self.error_count
