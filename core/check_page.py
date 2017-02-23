# Import python modules


# Import core modules
from core import config
from core import create_comment
import traceback
from core import warning
from core import log

def run(text, page, algorithms):
	try:
		zeroedit = True
		edit_comments = []
		comments = ""
		if warning.precheck(text, str(page)):
			log.addwarpage(page.title())
			return text, comments, zeroedit
		for algorithm in algorithms:
			algorithm.__init__()
			data = algorithm.run(text, page)

			if data[1] == 1 and algorithm.comments[config.lang+"0"] not in edit_comments and text != data[0]:
				edit_comments.append(algorithm.comments[config.lang+"0"])

			elif data[1] > 1 and config.lang+"1" not in algorithm.comments and text != data[0]:
				edit_comments.append(algorithm.comments[config.lang+"0"])

			elif data[1] > 1 and algorithm.comments[config.lang+"1"] not in edit_comments and text != data[0]:
				edit_comments.append(algorithm.comments[config.lang+"1"])

			if algorithm.zeroedit == False and text != data[0]:
				zeroedit = False

			text = data[0]

		comments = create_comment.comment(edit_comments)
		return text, comments, zeroedit
	except:
		print("unexcepted error:")
		traceback.print_exc()
		raise SystemExit
