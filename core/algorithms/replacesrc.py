from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0

	comments = {
		"fi0": u"siirsi Lähteet osion oikeaan kohtaan",
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
		nono = ["[["+getwordc("cat"),]
		listfound = False

		spaces = ["\n", "\t", "\b", "\a", "\r", ""]

		if titlein(getword("srcs"), text) and titlein(getword("exl"), text) and titlepos(getword("srcs"), text) > titlepos(getword("exl"), text) or titlein(getword("srcs"), text) and titlein(getword("li"), text) and titlepos(getword("srcs"), text) > titlepos(getword("li"), text):
			pos = titlepos(getword("srcs"), text)
			startpos = titleline(getword("srcs"), text)
			belows = text[pos:len(text)].split("\n")

			endpos = len(text.split("\n"))

			tries = 0
			lasttemp = False
			for l, line in  enumerate(belows[1:]):
				if abandop(spaces, line):
					tries += 1

				else:
					tries = 0

				if l == 2 and listfound == False:
					endpos = len(text.split("\n"))-len(belows)
					break

				if tries >= 2:
					endpos = len(text.split("\n"))-len(belows)+l
					break

				if anymatch(srclist, line):
					listfound = True

				if listfound and "|" in line and lasttemp:
					continue

				if anymatch(srclist, line) and "{{" in line:
					lasttemp = True

				if "}}" in line and lasttemp:
					lasttemp = False
					continue
					
				if anymatch(nono, line):
					endpos = len(text.split("\n"))-len(belows)+l
					break

				elif zeromatch(srclist, line) and line != "" and listfound and zeromatch(srclist, belows[l+1]):
					endpos = len(text.split("\n"))-len(belows)+l+1
					break

				print(line)

			text = text.split("\n")
			srcsec = '\n'.join(text[startpos:endpos])
			text = '\n'.join(text).replace(srcsec, "").split("\n")
			if titlein(getword("li"), '\n'.join(text)):
				text[titleline(getword("li"), '\n'.join(text))] = srcsec+"\n\n"+text[titleline(getword("li"), '\n'.join(text))]
			else:
				text[titleline(getword("exl"), '\n'.join(text))] = srcsec+"\n\n"+text[titleline(getword("exl"), '\n'.join(text))]
			text = '\n'.join(text)
			self.error_count += 1

		return text, self.error_count