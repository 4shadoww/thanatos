from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0
	parse = True

	comments = {
		"fi0": u"korjasi center tagin syntaksin",
		"fi1": u"korjasi center tagien syntaksit",
	}

	def __init__(self):
		self.error_count = 0

	def run(self, page, text):
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
