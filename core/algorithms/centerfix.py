from core.algcore import *

class Algorithm:
	notzeroedit = 1
	error_count = 0

	comments = {
		"fi0": u"korjasi br tagin syntaksin tai korvasi sen {{clear}} mallinella",
		"fi1": u"korjasi br tagien syntaksit tai korvasi ne {{clear}} mallinella",
	}

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):
		errorlist = re.findall(r"\<.*?\>", text)
		for item in errorlist:
			if istag("center", item):
				if '/' in item and item != '</center>':
					text = text.replace(item, '</center>')
					self.error_count += 1
				elif '/' not in item and item != '<center>':
					text = text.replace(item, '<center>')
					self.error_count += 1

		return text, self.error_count