#!/usr/bin/env python3

# Import python modules
import sys
import argparse
from glob import glob
import os

# Append lib path
sys.path.append("core/lib")

# Import core modules
from core import page_feeder
from core import job_handler

def main(file):
	try:
		pages = page_feeder.loadpages(file)
		if pages == None:
			return

		job_handler.check_pages(pages)

	except KeyboardInterrupt:
		print("thanatos terminated")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", nargs='?', default=None, help='file name')
	parser.add_argument("-l", nargs='?', default=False, help='list files')
	args = parser.parse_args()
	
	if args.l != False:
		listfiles = glob('core/articles/*')
		print('\navailable lists:\n')
		i = 1
		for item in listfiles:
			if i == len(listfiles):
				print(item.replace("core/articles/", ""))
			else:
				print(item.replace("core/articles/", "")+"    ",end="")
			i += 1
		sys.exit(0)

	if args.f == None:
		parser.print_help()
		sys.exit(0)
	try:
		os.remove("throttle.ctrl")
	except:
		pass
	main(args.f)