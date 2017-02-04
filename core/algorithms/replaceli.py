from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0

	comments = {
		"fi0": u"siirsi \"Kirjallisuutta\" -osion oikeaan kohtaan",
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

		if titlein(getword("li"), text) and titlein(getword("exl"), text) and titlepos(getword("li"), text) > titlepos(getword("exl"), text):
			feed = listend(text, getword("li"), srclist, nono, spaces)

			text = text.split("\n")
			exlec = text[feed[0]:feed[1]+1]
			text = removefromlist(exlec, text)

			if exlec[len(exlec)-1] != "" and exlec[len(exlec)-2] != "":
				exlec.append("")
				exlec.append("")

			elif exlec[len(exlec)-1] != "":
				exlec.append("")

			exlec = '\n'.join(exlec)


			text[titleline(getword("exl"), '\n'.join(text))] = exlec+text[titleline(getword("exl"), '\n'.join(text))]
			text = '\n'.join(text)
			self.error_count += 1

		return text, self.error_count