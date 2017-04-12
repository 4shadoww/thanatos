from core.algcore import *
import re

class Algorithm:
	zeroedit = False
	error_count = 0

	comments = {
		"fi0": u"",
		"fi00": u"siirsi \"Viitteet\" -osion oikealle tasolle",
		"fi01": u"muutti \"Viitteet\" -osion muotoon \"Lähteet\"",
	}

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):
		parser = wtparser.Parser()
		text = parser.parse(text)
		textlist = text.split('\n')
		for l, line in enumerate(textlist):
			matches = re.findall(r"\=.*\=", line)

			if len(matches) == 0:
				continue
			if getword("refs") in matches[0] and titlein(getword("srcs"), text) and matches[0].count("=") <= 4:
				textlist[l] = "===Viitteet==="
				error = 0
				self.error_count += 1

			elif getword("refs") in matches[0] and titlein(getword("srcs"), text) == False:
				textlist[l] = "==Lähteet=="
				error = 1
				self.error_count += 1

		text = '\n'.join(textlist)

		if self.error_count > 0 and error == 0:
			self.comments[config.lang+"0"] = self.comments[config.lang+"00"]
		elif self.error_count > 0 and error == 1:
			self.comments[config.lang+"0"] = self.comments[config.lang+"01"]

		text = parser.deparse(text)
		return text, self.error_count
