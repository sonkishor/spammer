import re

output = open("output.txt", "w+")

file = open( "subtitle.srt", "r")
lines = file.readlines()
file.close()

text = ''
for line in lines:
    if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
        text += ' ' + line.rstrip('\n')
        text = text.lstrip()
    output.write(text)

#this is buggy
