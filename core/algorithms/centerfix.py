
class Algorithm:
	notzeroedit = 1
	error_count = 0

	comments = {
		"fi0": u"korjasi br tagin syntaksin tai korvasi sen {{clear}} mallinella",
		"fi1": u"korjasi br tagien syntaksit tai korvasi ne {{clear}} mallinella",
	}

	def __init__(self):
		self.error_count = 0

	def run(self, text)
		errorlist = re.findall(r"\<.*?\>", text)

		for item in errorlist:
			if 'center' in item and len(item) <= 11 and '<!--' not in item and '>' in item:
				if '/' in item and item != '</center>':
					text = text.replace(item, '</center>')
					self.error_count += 1
				elif '/' not in item and item != '<center>':
					text = text.replace(item, '<center>')
					self.error_count += 1
