def reverse(s):
	l=list(s)
	j=len(l)-1
	i=0
	while i<j:
		l[i],l[j]=l[j],l[i]
		i+=1
		j-=1
	return "".join([str(k)for k in l])
s='lucknow'
t=reverse(s)
print(t)

