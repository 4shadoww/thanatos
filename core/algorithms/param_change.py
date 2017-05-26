from core.algcore import *
from pywikibot import textlib

class Algorithm:
	zeroedit = False
	error_count = 0
	parse = True

	comments = {
		"fi0": "muutti mallineen parametrin",
		"fi1": "muutti mallineen parametreja",
	}

	def __init__(self):
		self.error_count = 0

	def isInt(self, str):
		try:
			int(str)
			return True
		except ValueError:
			return False

	def createTemplate(self, dictionary):
		template = "{{"+dictionary[0]
		if len(dictionary[1]) > 0:
			for value in dictionary[1]:
				template += "|"+str(dictionary[1][value])

		template += "}}"

		return template

	def fixParam(self, template):
		for param in template[1]:
			try:
				template[1][param] = template[1][param].replace("id=", "")
			except:
				pass
			try:
				template[1][param] = template[1][param].replace("nimi=", "")
			except:
				pass

			if self.isInt(template[1][param]):
				template[1][param] = int(template[1][param]) + 123
		return template

	def run(self, page):
		text = page.text

		templates = findtemplates(text)
		for template in templates:
			try:
				ext_temp = textlib.extract_templates_and_params(template)[0]
			except IndexError:
				continue
			if ext_temp[0] == "Eurohockey" or ext_temp[0] == "eurohockey":
				ext_temp = self.fixParam(ext_temp)
				text = text.replace(template, self.createTemplate(ext_temp))

				self.error_count += 1

		return text, self.error_count
