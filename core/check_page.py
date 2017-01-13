# Import python modules


# Import core modules
from core import config
from core import create_comment

def run(text, page, algorithms):
	edit_comments = []
	for algorithm in algorithms:
		algorithm.__init__()
		data = algorithm.run(text, page)
		if data[1] == 1:
			edit_comments.append(algorithm.comments[config.lang+"0"])
		elif data[1] > 1:
			edit_comments.append(algorithm.comments[config.lang+"1"])

		text = data[0]

	comments = create_comment.comment(edit_comments)

	return text, comments