# Import python modules


# Import core modules
from core import config
from core import create_comment

def run(text, page, algorithms):
	zeroedit = True
	edit_comments = []
	for algorithm in algorithms:
		algorithm.__init__()
		data = algorithm.run(text, page)
		if data[1] == 1 and algorithm.comments[config.lang+"0"] not in edit_comments:

			edit_comments.append(algorithm.comments[config.lang+"0"])

		elif data[1] > 1 and algorithm.comments[config.lang+"1"] not in edit_comments:
			
			edit_comments.append(algorithm.comments[config.lang+"1"])
		text = data[0]

		if algorithm.notzeroedit == 1:
			zeroedit = False

	comments = create_comment.comment(edit_comments)
	return text, comments, zeroedit