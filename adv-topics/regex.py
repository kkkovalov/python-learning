
# Basic patterns
# . (a point) - any character except '\n'
# \w - matches a letter or digit or underscore [a-zA-Z0-9_]
# \b - boundry between word and non-word
# \s - matches singles " " (whitespace), tab, newline or form
# \t, \n, \r - tab, newline, return
# \d - decimal digit [0-9]
# ^ - start, $ - end - match the start or end of the string


import re


str = 'an example word:car!!'
match = re.search(r'word', str)

if match:
    print("Found:", match.group())
else:
    print('did not found')