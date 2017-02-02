from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0

	comments = {
		"fi0": u"siirsi Katso myös osion oikeaan kohtaan",
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

		if titlein(getword("seealso"), text) and titlein(getword("srcs"), text) and titlepos(getword("seealso"), text) > titlepos(getword("srcs"), text):
			feed = listend(text, getword("seealso"), srclist, nono, spaces)

			text = text.split("\n")
			seealsoec = '\n'.join(text[feed[0]:feed[1]])
			text = '\n'.join(text).replace(seealsoec, "").split("\n")
			text[titleline(getword("srcs"), '\n'.join(text))] = seealsoec+"\n\n"+text[titleline(getword("srcs"), '\n'.join(text))]
			text = '\n'.join(text)
			self.error_count += 1

		return text, self.error_count