# Unicode converter

import html
from core import algcore

class Algorithm:
	zeroedit = False
	error_count = 0
	parse = True

	comments = {
		"fi0": u"muunsi [[unicode|unicode-syntaksin]] unicode merkeiksi",
	}

	def __init__(self):
		self.error_count = 0

	def run(self, page, text):
		newtext = html.unescape(text)
		if newtext != text:
			self.error_count = 1

		return newtext, self.error_count
