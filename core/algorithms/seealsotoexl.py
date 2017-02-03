import re
from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0

	comments = {
		"fi0": u"muutti \"Katso myös\" -osion muotoon \"Aiheesta muualla\"",
	}
	warnings = {
	"fic": "aihessta muualla osio ristiriita"
	}

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):
		srclist = ["*", "{{IMDb-h", "#",
		getwordlc("bref"), getword("bref"),
		getwordlc("wref"), getword("wref"),
		getwordlc("mref"), getword("mref"),
		getwordlc("sref"), getword("sref"),
		getwordlc("nref"), getword("nref"),
		getwordlc("commons"), getword("commons")]
		nono = ["[["+getwordc("cat"), "{{Tynkä", "{{tynkä", "{{AAKKOSTUS", "{{DEFAULTSORT", "{{OLETUSAAKKOSTUS"]

		spaces = ["\n", "\t", "\b", "\a", "\r", ""]

		if titlein(getword("seealso"), text) and "http://" in text or titlein(getword("seealso"), text) and "https://" in text:
			feed = listend(text, getword("seealso"), srclist, nono, spaces)
			text = text.split("\n")
			seealsosec = '\n'.join(text[feed[0]:feed[1]+1])

			if "[[" in seealsosec and "http://" in seealsosec or "[[" in seealsosec and "https://" in seealsosec:
				warning(self.warnings[config.lang+"c"])
			if "http://" in seealsosec or "https://" in seealsosec:
				text[feed[0]] = "=="+getword("exl")+"=="
				self.error_count += 1

			text = '\n'.join(text)
		return text, self.error_count