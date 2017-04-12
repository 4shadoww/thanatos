from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0
	parse = True

	comments = {
		"fi0": u"poisti turhan Viitteet tai Lähteet osion",
		"en0": u"removed useless References section",
	}

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):
		nono = ["{{iihfranking"]
		if text.count("<ref/>") == 0 and text.count("<ref />") == 0 and text.count("<ref>") == 0:
			self.error_count += 1
			if titlein(getword("refs"), text):
				text = text.split("\n")
				for l, line in enumerate(text):
					if titlein(getword("refs"), line):
						text.pop(l)
						break
				for l, line in enumerate(text):
					if "{{"+getword("refs") in line or "{{"+getwordlc("refs") in line or "<references" in line:
						text.pop(l)
						break
			else:
				text = text.split("\n")
				for l, line in enumerate(text):
					if titlein(getword("srcs"), line):
						text.pop(l)
						break
				for l, line in enumerate(text):
					if "{{"+getword("refs") in line or "{{"+getwordlc("refs") in line or "<references" in line:
						text.pop(l)
						break
			text = '\n'.join(text)
		return text, self.error_count
