#!/usr/bin/env python3

# Import python modules
import sys
import argparse
import os

# Append lib path
sys.path.append("core/lib")

# Import core modules
from core import algorithm_loader
from core import check_page
from core import adiffer
from core import colors
from core.log import *
from core import warning

test_algorithms = ["titlechanger",]

test_algorithms1 = ["ucc", "brfix",
	"centerfix", "smallfix", "titlechanger",
	"textinen", "seealsotoexl", "twovlines",
	"typofix", "reftosrc", "titlelevel",
	"refstemp", "fix2brackets", "filedelinker",
	"fixpiped", "replacecomms", "replacesrc", "replaceseealso",
	"replaceli", "fixreflist",]

test_ignore = ["typofix", "ucc", "fixblinks", "fixreflinks", "filedelinker"]

def main(file):
	printblank = False
	f = open("core/testarticles/"+file, "r").read()
	try:
		algorithms = algorithm_loader.load_algorithms(algorithms=test_algorithms, ignore=test_ignore)
		data = check_page.run(f, file, algorithms)
		if f != data[0]:
			if printblank:
				print(data[0]+"\n--------------")
			adiffer.show_diff(f, data[0])
			print(colors.yellow+str(file)+": "+data[1]+colors.end)
			print("zeroedit: "+str(data[2]))
			warning.check(data[0], f)
			printwarnings()
		else:
			print("no changes made")

	except KeyboardInterrupt:
		print("thanatos terminated")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", nargs='?', default=None, help='file name')
	args = parser.parse_args()

	if args.f == None:
		parser.print_help()
		sys.exit(0)
	main(args.f)
