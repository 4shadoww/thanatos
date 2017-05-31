from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0
	parse = True

	comments = {
		"fi0": u"siirsi \"Kirjallisuutta\" -osion oikeaan kohtaan",
	}

	warnings = {
		"fi00": "siirretty vain otsikko",
		"fi01": "tagi ilman loppua",
	}

	def __init__(self):
		self.error_count = 0

	def run(self, page, text):
		srclist = ["*", "{{IMDb-h", "#",
		getwordlc("bref"), getword("bref"),
		getwordlc("wref"), getword("wref"),
		getwordlc("mref"), getword("mref"),
		getwordlc("sref"), getword("sref"),
		getwordlc("nref"), getword("nref"),
		getwordlc("commons"), getword("commons")]
		nono = ["[["+getwordc("cat"), "{{Tynkä", "{{tynkä", "{{AAKKOSTUS", "{{DEFAULTSORT", "{{OLETUSAAKKOSTUS"]

		if titlein(getword("li"), text) and titlein(getword("exl"), text) and titlepos(getword("li"), text) > titlepos(getword("exl"), text):
			feed = listend(text, getword("li"), srclist, nono)
			if feed[0] == feed[1]:
				warning(self.warnings[config.lang+"00"])

			if tagwithoutend('\n'.join(text[feed[0]:feed[1]])):
				warning(self.warnings[config.lang+"01"])

			text = text.split("\n")
			if "===" in text[titleline(getword("li"), '\n'.join(text))]:
				text = '\n'.join(text)
				return text, self.error_count

			exlec = text[feed[0]:feed[1]+1]
			text = removefromlist(exlec, text)
			n1 = "\n"
			exlec = '\n'.join(exlec)
			if text[titleline(getword("exl"), '\n'.join(text))-1] == "":
				n1 = ""
			text[titleline(getword("exl"), '\n'.join(text))] = n1+exlec+"\n\n"+text[titleline(getword("exl"), '\n'.join(text))]
			text = '\n'.join(text)
			self.error_count += 1

		return text, self.error_count
