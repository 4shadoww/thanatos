from core.algcore import *
import re

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

	def run(self, page):
		text = page.text

		target_template = "koirarotu"

		templates = findtemplates(text)
		for template in templates:
			orgtemplate = template
			template = template.split("\n")

			first_line = True
			edited = False
			for i in range(len(template)):
				if target_template[0].upper()+target_template[1:] not in template[i] and first_line and target_template[0].lower()+target_template[1:] not in template[i] and first_line:
					break

				if first_line and "|" not in template[i]:
					break
				else:
					self.error_count += 1

				newline = remove_ending("|", template[i])

				if newline != template[i] and not first_line and not template[i].startswith("|"):
					template[i] = "| "+newline

				elif newline != template[i] and first_line:
					template[i] = newline

				elif "=" in template[i] and "|" not in template[i]:
					template[i] = "| "+template[i]

				first_line = False
				edited = True
			if edited:
				template = '\n'.join(template)
				text = text.replace(orgtemplate, template)

		return text, self.error_count
