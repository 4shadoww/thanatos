from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0

	comments = {
		"fi0": u"siirsi \"Katso myös\" -osion oikeaan kohtaan",
	}

	warnings = {
		"fi00": "siirretty vain otsikko",
		"fi01": "tagi ilman loppua",
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

		if titlein(getword("seealso"), text) and titlein(getword("srcs"), text) and titlepos(getword("seealso"), text) > titlepos(getword("srcs"), text):
			feed = listend(text, getword("seealso"), srclist, nono)

			if feed[0] == feed[1]:
				warning(self.warnings[config.lang+"00"])

			if tagwithoutend('\n'.join(text[feed[0]:feed[1]])):
				warning(self.warnings[config.lang+"01"])

			text = text.split("\n")
			seealsoec = text[feed[0]:feed[1]+1]
			text = removefromlist(seealsoec, text)

			if seealsoec[len(seealsoec)-1] != "":
				seealsoec.append("")

			if seealsoec[len(seealsoec)-2] != "":
				seealsoec.append("")

			seealsoec = '\n'.join(seealsoec)

			text[titleline(getword("srcs"), '\n'.join(text))] = seealsoec+text[titleline(getword("srcs"), '\n'.join(text))]
			text = '\n'.join(text)
			self.error_count += 1

		return text, self.error_count
