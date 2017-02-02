from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0

	comments = {
		"fi0": u"siirsi Kirjallisuutta osion oikeaan kohtaan",
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
		nono = ["[["+getwordc("cat"),]

		spaces = ["\n", "\t", "\b", "\a", "\r", ""]

		if titlein(getword("li"), text) and titlein(getword("exl"), text) and titlepos(getword("li"), text) > titlepos(getword("exl"), text):
			feed = listend(text, getword("li"), srclist, nono, spaces)

			text = text.split("\n")
			exlec = '\n'.join(text[startpos:endpos])
			text = '\n'.join(text).replace(exlec, "").split("\n")
			text[titleline(getword("exl"), '\n'.join(text))] = exlec+"\n\n"+text[titleline(getword("exl"), '\n'.join(text))]
			text = '\n'.join(text)
			self.error_count += 1

		return text, self.error_count