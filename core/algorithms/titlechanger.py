from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0

	comments = {
		"fi0": "muutti osion oikean nimiseksi",
		"fi1": "muutti osioita oikean nimisiksi",
	}

	warnings = {
		"fi0": "otsikko ei tasolla 2",
	}

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):
		titles2change = [["Ulkoiset linkit", "Aiheesta muualla"], ["Ulkoiset linkit:", "Aiheesta muualla"], ["Asiasta muualla", "Aiheesta muualla"],
		["Lähteet:", "Lähteet"], ["lähteet:", "Lähteet"], ["Viitteet:", "Viitteet"]]

		text = text.split("\n")
		i = 0
		for line in text:
			for title in titles2change:
				if istitle(line) and titlein(title[0], line):
					if text.count("=") == 4:
						text[i] = "=="+title[0]+"=="
						self.error_count += 1
					else:
						warning(self.warnings[config.lang+"0"])
			i += 1
		text = '\n'.join(text)
		return text, self.error_count
