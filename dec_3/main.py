#!.venv/bin/python
import string
import requests
import os
import sys

from bs4 import BeautifulSoup as bs

# keep my cookies out of the repository
with open(os.path.join(sys.path[0], "cookie.txt")) as cf:
    cookie = cf.read()

# get input from site instead of copy/pasting this time!
link = "https://adventofcode.com/2022/day/3/input"
headers = {"cookie": cookie}
html = requests.get(link, headers=headers).text
input = bs(html, "html.parser").text

# create priority lookup table
priority = 1
priority_lut = {}

for c in string.ascii_lowercase:
    priority_lut[c] = priority
    priority += 1

for c in string.ascii_uppercase:
    priority_lut[c] = priority
    priority += 1

# for each line
#   split it in 2
#   compare each side for a duplicate character
#   fetch the priority of the duplicate
#   add priority to total

total_priority = 0

sack_counter = 0
sacks = []
sack_group = []

for sack in input.splitlines():
    # add to group for part 2
    sack_group.append(sack)
    sack_counter += 1
    if sack_counter % 3 == 0:
        sacks.append(sack_group)
        sack_group = []

    # split into 2 containers
    sack_size = len(sack)
    containers = [
        sack[inx : inx + int(sack_size / 2)]
        for inx in range(0, sack_size, int(sack_size / 2))
    ]

    # for each character in the first string .find in the second
    for c in containers[0]:
        match = containers[1].find(c)
        if match > -1:
            match = c
            break

    # fetch the score for the match and add it to the total
    total_priority += priority_lut[match]

# Part 1 - sack compartments
print(total_priority)

# Part 2 - badges
total_priority = 0

for sack_group in sacks:
    for s in sack_group[0]:
        badge = sack_group[1].find(s)
        if badge > -1:
            badge = sack_group[2].find(s)
            if badge > -1:
                badge = s
                break

    total_priority += priority_lut[badge]

print(total_priority)
