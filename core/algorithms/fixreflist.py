from core.algcore import *
import re

class Algorithm:
	notzeroedit = 1
	error_count = 0

	comments = {
		"fi0": u"",
		"fi00": u"lisäsi puuttuvan viitteet osion",
		"fi01": u"lisäsi puuttuvan viitteet mallinen",
		"fi02": u"lisäsi puuttuvan lähteet osion",
	}

	def __init__(self):
		self.error_count = 0

	def addrefs0(self, text, article):
		listfound = False

		srclist = ["*", "{{IMDb-h", "#",
		getwordlc("bref"), getword("bref"),
		getwordlc("wref"), getword("wref"),
		getwordlc("mref"), getword("mref"),
		getwordlc("sref"), getword("sref"),
		getwordlc("nref"), getword("nref"),
		getwordlc("commons"), getword("commons"),
		"\n", "\t", "\b", "\a", "\r", "|"]

		pos = titlepos(getword("srcs"), text)
		belows = text[pos:len(text)].split("\n")

		refpos = len(text.split("\n"))-1

		for l, line in  enumerate(belows[1:]):
			if l == 2 and listfound == False:
				refpos = len(text.split("\n"))-len(belows)
				break
			
			if anymatch(srclist, line):
				listfound = True

			elif zeromatch(srclist, line) and line != "" and listfound and zeromatch(srclist, belows[l+1]):
				refpos = len(text.split("\b"))-len(belows)+l
				break
		if refpos != None and listfound == False:
			self.error_count += 1
			text = text.split("\n")
			text[refpos] = text[refpos]+"\n{{"+getword("refs")+"}}"
			text = '\n'.join(text)
			self.comments[config.lang+"0"] = self.comments[config.lang+"01"]

		elif refpos != None and listfound:
			nl0 = "\n"
			nl1 = "\n"
			self.error_count += 1
			text = text.split("\n")
			if text[refpos-1] == "":
				nl0 = ""
			if text[refpos] != "":
				nl1 += "\n"

			text[refpos] = nl0+"==="+getword("refs")+"===\n"+"{{"+getword("refs")+"}}"+nl1+text[refpos]
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
				print("loop")
				if anymatch(unwanted, line):
					if l+1 != len(text):
						pos = l+1
					else:
						pos = l
					break

				elif zeromatch(nono, line) and zeromatch(nono, text[l-1]) and line != "":
					if l+1 != len(text):
						pos = l+1
					else:
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


	def run(self, text, article):
		nono = ["<references/>", "<references />", 
		"{{"+getword("refs"), "{{"+getwordlc("refs")]

		if "<ref>" not in text:
			return text, self.error_count

		if andop(nono, text):
			return text, self.error_count

		if titlein(getword("srcs"), text) and "{{"+getword("refs") not in text and "{{"+getwordlc("refs") not in text:
			text = self.addrefs0(text, article)

		if titlein(getword("srcs"), text) == False:
			text = self.addrefs1(text, article)

		return text, self.error_count