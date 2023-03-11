import re
fp=open('email.text','r')
for line in fp:
	if re.search('^Message',line):
		print(line)
