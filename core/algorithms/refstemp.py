import re
from core.algcore import *

class Algorithm:
	zeroedit = True
	error_count = 0
	parse = True

	comments = {
		"fi0": u"muutti {{viitteet}} mallineen muotoon {{Viitteet}}",
		"fi1": u"muutti {{viitteet}} mallineen muotoon {{Viitteet}}",
		"fi00": u"muutti {{viitteet}} mallineen muotoon {{Viitteet}}",
		"fi01": u"muutti {{Viitteet|sarakkeet}} mallineen muotoon {{Viitteet}}",
	}

	def __init__(self):
		self.error_count = 0

	def run(self, page):
		text = page.text

		if text.count("<ref/>") < 1 and "{{"+getwordlc("refs")+"|sarakkeet}}" in text and "{{"+getword("refs")+"|sarakkeet}}" in text:
			self.error_count = 1
			text = text.replace("{{"+getwordlc("refs")+"|sarakkeet}}", "{{"+getword("refs")+"}}")
			text = text.replace("{{"+getword("refs")+"|sarakkeet}}", "{{"+getword("refs")+"}}")
			comments["fi0"] = comments["f01"]

		else:
			self.error_count += text.count("{{"+getwordlc("refs")+"}}")
			self.error_count += text.count("{{"+getwordlc("refs")+"|")
			text = text.replace("{{"+getwordlc("refs")+"}}", "{{"+getword("refs")+"}}")
			text = text.replace("{{"+getwordlc("refs")+"|", "{{"+getword("refs")+"|")

		return text, self.error_count
