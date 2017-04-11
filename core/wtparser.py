import re
import string
import random

class Parser:

	data_holder = []

	def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))

	def unid(self):
		objectid = None
		while True:
			objectid = self.id_generator()
			if len(self.data_holder) == 0 or any(objectid != i[0] for i in self.data_holder):
				break
		return objectid

	def thanatosid(self, string):
		return "THANATOS_ID="+self.unid()

	def endat(self, string, ending):
		if string.endswith(ending):
			return len(string)-len(ending)
		return 0

	def startat(self, string, starting):
		if string.startswith(starting):
			return len(starting)
		return 0

	def parse_comments(self, text):
		comments = re.findall("<!--.*?-->", text, re.DOTALL)
		for comment in comments:
			parsedcomment = self.thanatosid(comment)
			self.data_holder.append([parsedcomment, comment])
			text = text.replace(comment, parsedcomment)

		return text

	def parse(self, text):
		text = self.parse_comments(text)
		return text

	def deparse(self, text):
		for i in self.data_holder:
			text = text.replace(i[0], i[1])
		return text

	def clear(self):
		self.data_holder = []
