import os
import shutil
import subprocess
import markdown
import http.server

import settings
import parser

ROOT = settings.ROOT


def build():
	# Copy entire assets folder: stdout=open(os.devnull, 'wb')
	for file in settings.included_files:
		print('xcopy /q /i /y "' + os.path.join(ROOT, file) + '" "' + os.path.join(ROOT, 'public', file) + '"')
		subprocess.run('xcopy /q /i /y "' + os.path.join(ROOT, file) + '" "' + os.path.join(ROOT, 'public', file) + '"')
	for file in settings.included_dirs:
		subprocess.run('xcopy /e /y /i /q "' + os.path.join(ROOT, file) + '" "' + os.path.join(ROOT, 'public', file) + '"')

	# Iterate over each page in content folder
	for file in os.listdir(os.path.join(ROOT, settings.in_dir)):
		# Get page content
		with open(os.path.join(ROOT, settings.in_dir, file)) as in_file:
			text = in_file.read()

		if file[-4:] == 'html':
			page = {'title': file[:-5], settings.in_dir: text}
			out_link = os.path.join(ROOT, settings.out_dir, file)
		if file[-2:] == 'md':
			page = parser.parse(text, markdown.markdown)
			out_link = os.path.join(ROOT, settings.out_dir, file[:-3] + '.html')

		with open(os.path.join(ROOT, settings.templates, "default.html")) as template_file:
			template = template_file.read()

		with open(out_link, 'w') as out_file:
			out_file.write(template.format(page = page))

def serve():
	os.chdir(os.path.join(ROOT, 'public'))
	http.server.test(http.server.SimpleHTTPRequestHandler)