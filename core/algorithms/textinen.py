from core.algcore import *
import re

class Algorithm:
	zeroedit = True
	error_count = 0

	comments = {
		"fi0": u"muutti englanninkielisen termin suomenkieliseksi",
		"fi1": u"muutti englanninkieliset termin suomenkielisiksi"
	}

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):
		self.error_count += text.count("[[Category:")
		self.error_count += text.count("[[category:")
		self.error_count += text.count("[[File:")
		self.error_count += text.count("[[file:")
		self.error_count += text.count("[[Image:")
		self.error_count += text.count("[[image:")
		self.error_count += text.count("{{Reflist")
		self.error_count += text.count("{{reflist")
		self.error_count += text.count("{{Reflist|")
		self.error_count += text.count("{{reflist|")

		text = text.replace("[[Category:", "[["+getwordc("cat")).replace("[[File:", "[["+getwordc("file")).replace("[[Image:", "[["+getwordc("img"))
		text = text.replace("[[category:", "[["+getwordc("cat")).replace("[[file:", "[["+getwordc("file")).replace("[[image:", "[["+getwordc("img"))
		text = text.replace("{{Reflist", "{{"+getword("refs")).replace("{{reflist", "{{"+getword("refs")).replace("{{Reflist|", "{{"+getword("refs")+"|").replace("{{reflist|", "{{"+getword("refs")+"|")
		return text, self.error_count