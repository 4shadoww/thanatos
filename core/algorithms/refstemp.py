import re
from core.algcore import *

class Algorithm:
	notzeroedit = 0
	error_count = 0

	comments = {
		"fi0": u"muutti {{viitteet}} mallinen muotoon {{Viitteet}}",
		"fi1": u"muutti {{viitteet}} mallinen muotoon {{Viitteet}}",
	}

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):
		self.error_count += text.count("{{"+getwordlc("refs"))

		text = text.replace("{{"+getwordlc("refs"), "{{"+getword("refs"))

		return text, self.error_count