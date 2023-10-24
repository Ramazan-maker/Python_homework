import sys
import re


with open(sys.argv[1], 'r') as files:

    file = files.read().split()

pattern = r'\w[\w\.-_]+\w@\w[\w\.-_]+\.[a-zA-Z]{2,3}'

for email in file:
    matches = re.search(pattern, email)
    if not matches:
        print('Некорректный адрес: ', email)
