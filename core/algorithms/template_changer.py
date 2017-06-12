from core.algcore import *
import re

class Algorithm:
	zeroedit = False
	error_count = 0
	parse = True

	comments = {
		"fi0": "vaihtoi mallineen",
		"fi1": "vaihtoi mallineita",
	}

	template_name = ""

	def __init__(self):
		self.error_count = 0

	def run(self, page, text):
		target_template = "verkkosivu"

		templates = findtemplates(text)
		for template in templates:
			orgtemplate = template
			template = template.split("\n")

			for i in range(len(template)):
				if target_template[0].upper()+target_template[1:] not in template[i] and target_template[0].lower()+target_template[1:] not in template[i] and i == 0:
					break
				if i == 0:
					template[i] = "{{Verkkosivusto"
					self.error_count += 1
				if "kuvakaappaus" in template[i] and "=" in template[i]:
					kuvalist = template[i].split("=")
					kuva = kuvalist[1]

					if not kuva.isspace() and kuva != "" and "[[Kuva:" not in kuva:
						kuva = kuva.rstrip().lstrip()
						kuva = " [[Kuva:"+kuva+"|250px]]"
						kuvalist[1] = kuva
						template[i] = '='.join(kuvalist)
			template = '\n'.join(template)

			if orgtemplate != template:
				text = text.replace(orgtemplate, template)

		return text, self.error_count
