from core.algcore import *

class Algorithm:
	notzeroedit = 1
	error_count = 0

	comments = {
		"fi0": u"siirsi lähteet osion oikeaan kohtaan",
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
		getwordlc("commons"), getword("commons"),
		"{{"+getword("refs"), "{{"+getwordlc("refs"),
		"<references/>", "<references />",
		"==="+getword("refs")+"==="]

		if titlein(getword("srcs"), text) and titlein(getword("li"), text) and titlepos(getword("srcs"), text) > titlepos(getword("li"), text):
			startpos = titleline(getword("srcs"), text)
			text = text.split("\n")
			belows = text[startpos:]

			for l, line in enumerate(belows):
				if zeromatch(srclist, line) and zeromatch(srclist, belows[l+1]):
					endpos = len(text)-len(belows)+l
					break

			srcsec = '\n'.join(text[startpos:endpos])
			print(startpos)
			print(endpos)
			text = '\n'.join(text).replace(srcsec, "").split("\n")
			text[titleline(getword("li"), '\n'.join(text))] = srcsec+"\n\n"+text[titleline(getword("li"), '\n'.join(text))]
			text = '\n'.join(text)
			self.error_count += 1

		elif titlein(getword("srcs"), text) and titlein(getword("exl"), text) and titlepos(getword("srcs"), text) > titlepos(getword("exl"), text):
			startpos = titleline(getword("srcs"), text)
			text = text.split("\n")
			belows = text[startpos:]

			for l, line in enumerate(belows):
				if zeromatch(srclist, line) and zeromatch(srclist, belows[l+1]):
					endpos = len(text)-len(belows)+l
					break

			srcsec = '\n'.join(text[startpos:endpos])
			print(startpos)
			print(endpos)
			text = '\n'.join(text).replace(srcsec, "").split("\n")
			text[titleline(getword("exl"), '\n'.join(text))] = srcsec+"\n\n"+text[titleline(getword("exl"), '\n'.join(text))]
			text = '\n'.join(text)
			self.error_count += 1

		return text, self.error_count