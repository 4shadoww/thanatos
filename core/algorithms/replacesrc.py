from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0
	parse = True

	comments = {
		"fi0": u"siirsi \"Lähteet\" -osion oikeaan kohtaan",
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
		getwordlc("commons"), getword("commons"),
		"{{"+getword("refs"), "{{"+getwordlc("refs"),
		"<references/>", "<references />",
		"==="+getword("refs")+"===", "{{Käännös|", "{{käännös|"]
		nono = ["[["+getwordc("cat"), "{{Tynkä", "{{tynkä", "{{AAKKOSTUS", "{{DEFAULTSORT", "{{OLETUSAAKKOSTUS"]

		if titlein(getword("srcs"), text) and titlein(getword("exl"), text) and titlepos(getword("srcs"), text) > titlepos(getword("exl"), text) or titlein(getword("srcs"), text) and titlein(getword("li"), text) and titlepos(getword("srcs"), text) > titlepos(getword("li"), text):

			feed = listend(text, getword("srcs"), srclist, nono)

			if feed[0] == feed[1]:
				warning(self.warnings[config.lang+"00"])

			if tagwithoutend('\n'.join(text[feed[0]:feed[1]])):
				warning(self.warnings[config.lang+"01"])

			text = text.split("\n")
			srcsec = text[feed[0]:feed[1]+1]

			text = removefromlist(srcsec, text)
			print(text)
			srcsec = '\n'.join(srcsec)
			n1 = "\n"

			if titlein(getword("li"), '\n'.join(text)):
				if text[titleline(getword("li"), '\n'.join(text))-1] == "":
					n1 = ""
				text[titleline(getword("li"), '\n'.join(text))] = n1+srcsec+"\n\n"+text[titleline(getword("li"), '\n'.join(text))]
			elif titlein(getword("exl"), '\n'.join(text)):
				if text[titleline(getword("exl"), '\n'.join(text))-1] == "":
					n1 = ""
				text[titleline(getword("exl"), '\n'.join(text))] = n1+srcsec+"\n\n"+text[titleline(getword("exl"), '\n'.join(text))]
			text = '\n'.join(text)
			self.error_count += 1

		return text, self.error_count
