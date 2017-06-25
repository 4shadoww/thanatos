from core.algcore import *
import re
from pywikibot import textlib

class Algorithm:
	zeroedit = False
	error_count = 0
	parse = True

	comments = {
		"fi0": "korjasi mallinetta",
		"fi1": "korjasi mallineita",
	}

	template_name = ""

	def __init__(self):
		self.error_count = 0

	def isInt(self, str):
		try:
			int(str)
			return True
		except ValueError:
			return False

	def glue_template_and_params(self, template_and_params):
		(template, params) = template_and_params
		text = ""
		for item in params:
			if self.isInt(item) and params[item] == "":
				continue
			text += u"| %s = %s\n" % (item, params[item])

		return u"{{%s\n%s}}" % (template, text)

	def run(self, page, text):
		target_template = "Jalkapalloseura"

		templates = findtemplates(text)
		for template in templates:
			ntemplate = textlib.extract_templates_and_params(template)
			for tem in ntemplate:
				temx = template.split("\n")
				if tem[0].lower() == target_template.lower():
						text = text.replace(template, self.glue_template_and_params(tem))
						self.error_count += 1

		return text, self.error_count
