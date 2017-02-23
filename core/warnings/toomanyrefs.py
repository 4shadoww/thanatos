from core.lop import *

class Warning:
	wm = {
	"fi": "Liian monta viitteet mallinetta",}

	error_count = 0

	def __init__(self):
		self.error_count = 0

	def run(self, text):
		r0 = 0
		r1 = 0
		r2 = 0
		r3 = 0
		r0 = text.count("{{"+getword("refs")+"}}")
		r1 = text.count("{{"+getwordlc("refs")+"}}")
		r2 = text.count("{{"+getword("refs")+"|")
		f3 = text.count("{{"+getwordlc("refs")+"|")

		if r0 + r1 + r2 + r3 > 1:
			self.error_count += 1

		return self.error_count
