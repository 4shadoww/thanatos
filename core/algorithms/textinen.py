from core.algcore import *
import re

class Algorithm:
	notzeroedit = 1
	error_count = 0

	comments = {
		"fi0": u"muutti englanninkielisen viitteen suomenkieliseksi",
		"fi1": u"muutti englanninkieliset viitteet suomenkielisiksi"
	}

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):
		self.error_count += text.count("[[Category:")
		self.error_count += text.count("[[File:")
		self.error_count += text.count("[[Image:")

		text = text.replace("[[Category:", "[["+getwordc("cat", lang=config.lang)).replace("[[File:", "[["+getwordc("file", lang=config.lang)).replace("[[Image:", "[["+getwordc("img", lang=config.lang))

		return text, self.error_count