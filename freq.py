#from itertools import frequency
def freq(s):
	m={}
	for st in s:
		if st in m.keys():
			m[st]+=1
		else:
			m[st]=1
		for key in m.keys():
			print(key,m[key])
s='lucknow junction'
freq(s)
