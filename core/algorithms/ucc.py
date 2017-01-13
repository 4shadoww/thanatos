# Unicode converter

import html
from core import algcore

class Algorithm:
	notzeroedit = 1
	error_count = 0
	comments = {
		"fi0": u"muunsi [[unicode|unicode-syntaksin]] unicode merkeiksi",
	}

	def __init__(self):
		self.error_count = 0

	def run(self,text, article):
		newtext = html.unescape(text)
		if newtext != text:
			self.error_count = 1
		return newtext, self.error_count