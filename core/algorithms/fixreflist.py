from core.algcore import *
import re

class Algorithm:
	zeroedit = False
	error_count = 0

	comments = {
		"fi0": u"",
		"fi00": u"lisäsi puuttuvan \"Viitteet\" -osion",
		"fi01": u"lisäsi puuttuvan \"Viitteet\" mallineen",
		"fi02": u"lisäsi puuttuvan \"Lähteet\" -osion",
		"fi03": u"siirsi \"Viitteet\" -osion oikeaan kohtaan",
	}

	warnings = {
		"fi00": "siirretty vain otsikko",
		"fi01": "tagi ilman loppua",
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
		getwordlc("commons"), getword("commons"),
		"{{"+getword("refs"), "{{"+getwordlc("refs"),
		"<references", "{{Käännös|", "{{käännös|"]

		nono = ["[["+getwordc("cat"), "{{Tynkä", "{{tynkä", "{{AAKKOSTUS", "{{DEFAULTSORT", "{{OLETUSAAKKOSTUS"]

		feed = listend(text, getword("srcs"), srclist, nono)
		print(feed)
		if tagwithoutend('\n'.join(text[feed[0]:feed[1]])):
			warning(self.warnings[config.lang+"01"])

		if feed[0] == feed[1]:
			warning(self.warnings[config.lang+"00"])

		if feed[1] != None and feed[2] == False:
			self.error_count += 1
			text = text.split("\n")
			nl00 = "\n"
			if text[feed[0]] == "":
				nl00 = ""
			text[feed[0]] = text[feed[0]]+nl00+"{{"+getword("refs")+"}}"
			text = '\n'.join(text)
			self.comments[config.lang+"0"] = self.comments[config.lang+"01"]

		elif feed[1] != None and feed[2]:
			nl0 = "\n"
			nl1 = ""
			self.error_count += 1
			text = text.split("\n")
			if text[feed[1]] != "":
				nl0 = "\n\n"
			if text[feed[1]+1] != "":
				nl1 += "\n\n"

			text[feed[1]] = text[feed[1]]+"\n\n"+"==="+getword("refs")+"===\n"+"{{"+getword("refs")+"}}"+nl1
			text = '\n'.join(text)
			self.comments[config.lang+"0"] = self.comments[config.lang+"00"]

		return text

	def addrefs1(self, text, article):
		targetline = None

		pos = None
		nono = ["{{", getwordc("cat"),
		getwordlcc("cat"),]

		unwanted = ["{{"+getword("commons"), "{{"+getwordlc("commons"), "*", "#",
		"<ref>", "</ref>", "\n", "\t", "\b", "\a", "\r", "|}"]

		text = text.split("\n")
		firstcat = len(text)
		for l, line in enumerate(text):
			if getwordlcc("cat") in line or getwordc("cat") in line:
				firstcat = l
				pos = l
				break

		for l, line in reversed(list(enumerate(text[:firstcat]))):
			if anymatch(unwanted, line):
				minus = len(text)-l
				pos = len(text)-minus+1
				break

			elif zeromatch(nono, line) and zeromatch(nono, text[l-1]) and line != "":
				minus = len(text)-l
				pos = len(text)-minus+1
				break

		if pos == len(text):
			pos -= 1

		if pos != None:
			nl = ""
			if text[pos] != "":
				nl = "\n"
			text[pos] = text[pos]+nl+"\n=="+getword("srcs")+"==\n{{"+getword("refs")+"}}\n"

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
		getwordlc("commons"), getword("commons"),
		"{{"+getword("refs"), "{{"+getwordlc("refs"),
		"<references", "{{Käännös|", "{{käännös|"]

		nono = ["[["+getwordc("cat"), "{{Tynkä", "{{tynkä", "{{AAKKOSTUS", "{{DEFAULTSORT", "{{OLETUSAAKKOSTUS"]

		text = text.split("\n")

		feed0 = listend('\n'.join(text), getword("refs"), srclist, nono)

		if feed0[0] == feed0[1]:
			warning(self.warnings[config.lang+"00"])

		refsec = '\n'.join(text[feed0[0]:feed0[1]+1])


		for l,t in zip(range(feed0[0], feed0[1]+1), range(0, feed0[1]-feed0[0]+1)):
			text.pop(l-t)


		feed = listend('\n'.join(text), getword("srcs"), srclist, nono)

		if tagwithoutend('\n'.join(text[feed[0]:feed[1]])):
			warning(self.warnings[config.lang+"01"])

		if feed[0] == feed[1]:
			warning(self.warnings[config.lang+"00"])

		if feed[1] != None:
			nl0 = "\n"
			nl1 = "\n"
			self.error_count += 1

			text[feed[1]] = text[feed[1]]+nl0+refsec+"\n"+nl1
			text = '\n'.join(text)
			self.comments[config.lang+"0"] = self.comments[config.lang+"03"]
		return text

	def run(self, text, article):
		parser = wtparser.Parser()
		text = parser.parse(text)
		nono = ["<references/>", "<references />", "<references>",
		"{{"+getword("refs"), "{{"+getwordlc("refs"), "{{reflist", "{{Reflist"]

		if titlein(getword("refs"), text) and titlein(getword("srcs"), text) and not titlebefore(getword("srcs"), getword("refs"), text, subtitles=False):
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
		text = parser.deparse(text)
		return text, self.error_count
