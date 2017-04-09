import re

def endat(string, ending):
	if string.endswith(ending):
		return len(string)-len(ending)
	return 0

def startat(string, starting):
	if string.startswith(starting):
		return len(starting)
	return 0

def parse_comments(text):
	comments = re.findall("<!--.*?-->", text, re.DOTALL)
	print(comments)
	for comment in comments:
		spos = startat(comment, "<!--")
		epos = endat(comment[spos:], "-->")

		cdata = list(comment)

		for i in range(epos):
			if cdata[spos+i] != "\n":
				cdata[spos+i] = "#"

		parsed_comment = ''.join(cdata)
		text = text.replace(comment, parsed_comment)

	return text

def parse(text):
	text = parse_comments(text)
	return text
