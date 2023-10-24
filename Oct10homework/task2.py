import sys
import re

if len(sys.argv) != 2:
    print('Пожалуйста, укажите имя HTML-файла в качестве аргумента командной строки.')
    sys.exit(1)

html_file = sys.argv[1]

with open(html_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

title_match = re.search(r'<title>(.*?)</title>', html_content)
title = title_match.group(1) if title_match else None

headers = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', html_content)

if title:
    print(title)

for header in headers:
    print(header)
