from core.lop import *
from core.algcore import *

class Warning:
	wm = {
	"fi": "osion siirto tuottaa ongelmia",}

	error_count = 0

	def __init__(self):
		self.error_count = 0

	def getsec(self, text):
		secs = []
		cut = False
		start = 0
		for l in  range(0, len(text)):
			thread_header = re.search('^== *([^=].*?) *== *$', text[l])
			if thread_header:
				if cut == True:
					secs.append(text[start:l])
				start = l
				cut = True
			elif len(text)-1 == l:
				secs.append(text[start:l])
		return secs

	def getlen(self, sec):
		nons = True
		length = 0
		for line in reversed(sec):
			if line == "" and nons:
				continue
			else:
				length += 1
				nons = False
		return length
	def run(self, text):
		self.wm["fi"] = "osion siirto tuottaa ongelmia"
		text = text.split("\n")
		secs = self.getsec(text)

		srclist = ["*", "{{IMDb-h", "#",
		getwordlc("bref"), getword("bref"),
		getwordlc("wref"), getword("wref"),
		getwordlc("mref"), getword("mref"),
		getwordlc("sref"), getword("sref"),
		getwordlc("nref"), getword("nref"),
		getwordlc("commons"), getword("commons"),
		"{{"+getword("refs"), "{{"+getwordlc("refs"),
		"<references", "===", "{{Käännös|", "{{käännös|"]

		nono = ["[["+getwordc("cat"), "{{Tynkä", "{{tynkä", "{{AAKKOSTUS", "{{DEFAULTSORT", "{{OLETUSAAKKOSTUS"]

		secsl = [getword("srcs"), getword("refs"), getword("li"), getword("exl"), getword("seealso")]

		for l, sec in enumerate(secs):
			if len(sec) > 0 and sec[0].replace("=", "") in secsl and l != len(secs)-1:
				feed = listend('\n'.join(text), sec[0].replace("=", ""), srclist, nono)
				if feed[1]-feed[0]+1 != self.getlen(sec):
					self.error_count += 1
					self.wm[config.lang] = sec[0].replace("=", "") +", "+ self.wm[config.lang]

		return self.error_count
