import re
from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0
	parse = True

	comments = {
		"fi0": u"korjasi br tagin syntaksin tai korvasi sen {{clear}} mallineella",
		"fi1": u"korjasi br tagien syntaksit tai korvasi ne {{clear}} mallineella",
	}

	def __init__(self):
		self.error_count = 0

	def run(self, page, text):
		errorlist = re.findall(r"\<.*?\>", text)
		nono = ['abbr', 'wbr', 'ref', '<!--']
		for item in errorlist:
			if andop(nono, item) == False and istag("br", item):
				if 'clear' in item and '=' in item:
					if 'all' in item:
						text = text.replace(item, '{{clear}}')
						self.error_count += 1
					elif 'left' in item:
						text = text.replace(item, '{{clear|left}}')
						self.error_count += 1
					elif 'right' in item:
						text = text.replace(item, '{{clear|right}}')
						self.error_count += 1
				elif '/' in item and item != '<br />' and 'clear' not in item and '=' not in item:
					text = text.replace(item, '<br />')
					self.error_count += 1
				elif '/' not in item and item != '<br>' and 'clear' not in item and '=' not in item:
					text = text.replace(item, '<br>')
					self.error_count += 1

		return text, self.error_count
