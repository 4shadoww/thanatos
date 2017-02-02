from core.algcore import *
import re

class Algorithm:
	zeroedit = False
	error_count = 0

	comments = {
		"fi0": u"",
		"fi00": u"lisäsi puuttuvan Viitteet osion",
		"fi01": u"lisäsi puuttuvan Viitteet mallinen",
		"fi02": u"lisäsi puuttuvan Lähteet osion",
		"fi03": u"siirsi Viitteet osion oikeaan kohtaan",
	}

	def __init__(self):
		self.error_count = 0

	def addrefs0(self, text, article):
		srclist = ["*", "{{IMDb-h", "#",
		getwordlc("bref"), getword("bref"),
		getwordlc("wref"), getword("wref"),
		getwordlc("mref"), getword("mref"),
		getwordlc("sref"), getword("sref"),
		getwordlc("nref"), getword("nref"),
		getwordlc("commons"), getword("commons"),]

		nono = ["[["+getwordc("cat"), "{{Tynkä", "{{tynkä"]

		spaces = ["\n", "\t", "\b", "\a", "\r", ""]

		feed = listend(text, getword("srcs"), srclist, nono, spaces)

		if feed[1] != None and feed[2] == False:
			self.error_count += 1
			text = text.split("\n")
			text[feed[1]] = text[feed[1]]+"\n{{"+getword("refs")+"}}"
			text = '\n'.join(text)
			self.comments[config.lang+"0"] = self.comments[config.lang+"01"]

		elif feed[1] != None and feed[2]:
			nl0 = "\n"
			nl1 = "\n"
			self.error_count += 1
			text = text.split("\n")
			if text[feed[1]-1] == "":
				nl0 = ""
			if text[feed[1]] != "":
				nl1 += "\n"

			text[feed[1]] = nl0+"==="+getword("refs")+"===\n"+"{{"+getword("refs")+"}}"+nl1+text[feed[0]]
			text = '\n'.join(text)
			self.comments[config.lang+"0"] = self.comments[config.lang+"00"]

		return text

	def addrefs1(self, text, article):
		method = 0
		targetline = None

		for l, line in enumerate(text.split("\n")):

			if titlein(getword("exl"), line):
				method = 1
				targetline = l
				break

		if method == 0:
			pos = None
			nono = ["{{", getwordc("cat"),
			getwordlcc("cat")]

			unwanted = ["{{"+getword("commons"), "{{"+getwordlc("commons"), "*", "#",
			"<ref>", "</ref>", "\n", "\t", "\b", "\a", "\r"]

			text = text.split("\n")
			for l, line in reversed(list(enumerate(text))):
				if anymatch(unwanted, line):
					pos = l
					break

				elif zeromatch(nono, line) and zeromatch(nono, text[l-1]) and line != "":
					pos = l
					break

			if pos != None:
				text[pos] = text[pos]+"\n\n=="+getword("srcs")+"==\n{{"+getword("refs")+"}}\n"

			text = '\n'.join(text)
			self.error_count += 1
			self.comments[config.lang+"0"] = self.comments[config.lang+"02"]


		elif method == 1 and targetline != None:
			text = text.split("\n")
			text[targetline] = "=="+getword("srcs")+"==\n{{"+getword("refs")+"}}\n\n"+text[targetline]
			text = '\n'.join(text)
			self.error_count += 1
			self.comments[config.lang+"0"] = self.comments[config.lang+"02"]


		return text

	def addrefs2(self, text, article):
		line = titleline(getword("refs"), text)
		text = text.split("\n")
		text[line] = text[line]+"\n{{"+getword("refs")+"}}"
		self.error_count += 1
		self.comments[config.lang+"0"] = self.comments[config.lang+"01"]
		text = '\n'.join(text)
		return text

	def addrefs3(self, text, article):
		srclist = ["*", "{{IMDb-h", "#",
		getwordlc("bref"), getword("bref"),
		getwordlc("wref"), getword("wref"),
		getwordlc("mref"), getword("mref"),
		getwordlc("sref"), getword("sref"),
		getwordlc("nref"), getword("nref"),
		getwordlc("commons"), getword("commons"),]

		nono = ["[["+getwordc("cat"), "{{Tynkä", "{{tynkä"]

		spaces = ["\n", "\t", "\b", "\a", "\r", ""]


		text = text.split("\n")
		reftype = "{{"+getword("refs")+"}}"
		for l, line in enumerate(text):
			if titlein(getword("refs"), line):
				text.pop(l)
				break
		for l, line in enumerate(text):
			if "{{"+getword("refs") in line or "{{"+getwordlc("refs") in line or istag("references", line):
				if "{{viitteetön" not in line and "{{Viitteetön" not in line:
					reftype = text[l]
					text.pop(l)

		feed = listend('\n'.join(text), getword("srcs"), srclist, nono, spaces)

		if feed[1] != None:
			nl0 = "\n"
			nl1 = "\n"
			self.error_count += 1
			if text[feed[1]-1] == "":
				nl0 = ""
			if text[feed[1]-2] == "":
				nl0 += "\n"
			if text[feed[1]] != "":
				nl1 += "\n"
			print(text[feed[1]])
			text[feed[1]] = text[feed[1]]+nl0+"==="+getword("refs")+"===\n"+reftype+nl1
			text = '\n'.join(text)
			self.comments[config.lang+"0"] = self.comments[config.lang+"03"]
		return text

	def run(self, text, article):
		nono = ["<references/>", "<references />", 
		"{{"+getword("refs"), "{{"+getwordlc("refs"), "{{reflist", "{{Reflist"]

		if titlein(getword("refs"), text) and titlein(getword("srcs"), text) and titlebefore(getword("srcs"), getword("refs"), text) == False:
			text = self.addrefs3(text, article)

		elif titlein(getword("refs"), text) and titlein(getword("srcs"), text) and titlein(getword("li"), text) and titlebefore(getword("refs"), getword("li"), text) == False:
			text = self.addrefs3(text, article)

		elif titlein(getword("refs"), text) and titlein(getword("srcs"), text) and titlein(getword("exl"), text) and titlebefore(getword("refs"), getword("exl"), text) == False:
			text = self.addrefs3(text, article)

		if "<ref>" not in text and "</ref>" not in text:
			return text, self.error_count

		if andop(nono, text):
			return text, self.error_count

		elif titlein(getword("refs"), text) and titlein(getword("srcs"), text) and "{{"+getword("refs") not in text and "{{"+getwordlc("refs") not in text:
			text = self.addrefs2(text, article)
		elif titlein(getword("srcs"), text) and "{{"+getword("refs") not in text and "{{"+getwordlc("refs") not in text:
			text = self.addrefs0(text, article)

		elif titlein(getword("srcs"), text) == False:
			text = self.addrefs1(text, article)

		return text, self.error_count