import re


str = 'an example word:car!!'
match = re.search(r'word', str)

if match:
    print("Found:", match.group())
else:
    print('did not found')