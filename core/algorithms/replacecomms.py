from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0

	comments = {
		"fi0": u"siirsi Commonscat mallineen \"Aiheesta muualla\" -osioon",
	}

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):
		template = None
		if "{{commonscat|" in text and titlein(getword("exl"), text) and not insec("{{commonscat|", getword("exl"), text) or "{{Commonscat|" in text and titlein(getword("exl"), text) and not insec("{{Commonscat|", getword("exl"), text):
			text = text.split("\n")
			for l in range(0, len(text)):
				if "{{commonscat|" in text[l] or "{{Commonscat|" in text[l]:
					template = text[l]
					text.pop(l)
					break
			if template != None:
				self.error_count += 1
				text[titleline(getword("exl"), '\n'.join(text))] = text[titleline(getword("exl"), '\n'.join(text))] +"\n"+template
			text = '\n'.join(text)

		return text, self.error_count
