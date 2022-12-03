#!.venv/bin/python
import string
import requests
from bs4 import BeautifulSoup as bs

import cookie

# get input
link = "https://adventofcode.com/2022/day/3/input"
headers = {"cookie": cookie}
html = requests.get(link, headers=headers).text
input = bs(html, "html.parser")

print(input)

# create priority lookup table
priority = 1
priority_lut = {}

for c in string.ascii_lowercase:
    priority_lut[c] = priority
    priority += 1

for c in string.ascii_uppercase:
    priority_lut[c] = priority
    priority += 1
