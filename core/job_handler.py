# Import python modules


# Import core modules
from core import check_page


def check_pages(pages):

	for page in pages:
		check_page.run(page)