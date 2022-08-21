def parse(text, parser):
	"""
	assumes string text and function parser
	outputs header data and parsed text
	"""
	text = text.strip().split('---')
	head, body = text[1].strip(), text[2].strip()

	output = {}

	for a in head.split('\n'):
		key,value = a.strip().split(':')
		output[key.strip()] = value.strip()

	output['content'] = parser(body)

	return output