# Import python modules
import sys
import os

# Append lib
sys.path.append("core/lib")

# Import pywikibot
import pywikibot
from pywikibot import pagegenerators

# Pages per file
limit = 2000

output = "core/articles/newpages.txt"

# Remove old file
print("removing old file...")
try:
	os.remove(output)

except FileNotFoundError:
	pass

output_file = open(output, "a")

site = pywikibot.Site()
gen = pagegenerators.NewpagesPageGenerator(site=None, namespaces=[0], total=limit)

print("now writing...")

for page in gen:
	output_file.write(page.title()+"\n")
	print(page.title())

output_file.close()

print("saved to", output)
print("done")
