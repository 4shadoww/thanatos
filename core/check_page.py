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
		if warning.precheck(page.text, str(page)):
			log.addwarpage(page.title())
			return page.text, comments, zeroedit
		for algorithm in algorithms:
			algorithm.__init__()

			if algorithm.parse:
				page.text = parser.parse(page.text)
			data = algorithm.run(page)

			if data[1] == 1 and algorithm.comments[config.lang+"0"] not in edit_comments and page.text != data[0]:
				edit_comments.append(algorithm.comments[config.lang+"0"])

			elif data[1] > 1 and config.lang+"1" not in algorithm.comments and page.text != data[0]:
				edit_comments.append(algorithm.comments[config.lang+"0"])

			elif data[1] > 1 and algorithm.comments[config.lang+"1"] not in edit_comments and page.text != data[0]:
				edit_comments.append(algorithm.comments[config.lang+"1"])

			if algorithm.zeroedit == False and page.text != data[0]:
				zeroedit = False

			newtext = data[0]
			if algorithm.parse:
				newtext = parser.deparse(newtext)

		parser.clear()
		comments = create_comment.comment(edit_comments)
		return newtext, comments, zeroedit
	except:
		print("unexcepted error:")
		traceback.print_exc()
		raise SystemExit
