# Unicode converter

import html
from core import algcore

class Algorithm:
	notzeroedit = 1
	error_count = 0
	comments = {
		"fi0": u"muunsi [[unicode|unicode-syntaksin]] unicode merkeiksi",
	}

	def __init__():
		error_count = 0

	def run(self, article, text):
		newtext = html.unescape(text)
		if newtext != text:
			error_count = 1

		return newtext, error_count