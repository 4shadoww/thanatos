# Import python modules


# Import core modules
from core import config
from core import create_comment
import traceback
from core import warning
from core import log
from core import wtparser

def run(page, algorithms):
	try:
		parser = wtparser.Parser()
		zeroedit = True
		edit_comments = []
		comments = ""
		oldtext = page.text
		text = page.text
		if warning.precheck(text, str(page)):
			log.addwarpage(page.title())
			return text, comments, zeroedit
		for algorithm in algorithms:
			algorithm.__init__()

			if algorithm.parse:
				text = parser.parse(text)
			data = algorithm.run(page, text)

			if data[1] == 1 and algorithm.comments[config.lang+"0"] not in edit_comments and text != data[0]:
				edit_comments.append(algorithm.comments[config.lang+"0"])

			elif data[1] > 1 and algorithm.comments[config.lang+"1"] not in edit_comments and text != data[0]:
				edit_comments.append(algorithm.comments[config.lang+"1"])

			if not algorithm.zeroedit and text != data[0]:
				zeroedit = False

			text = data[0]
			if algorithm.parse:
				text = parser.deparse(text)

		parser.clear()
		comments = create_comment.comment(edit_comments)
		return text, comments, zeroedit
	except:
		print("unexcepted error:")
		traceback.print_exc()
		raise SystemExit
