class demo: # class varaible ko hm class ke name se bhi call kr skte hain aur object bna kr bhi call kr skte  hain
	age=20
	@classmethod # decorater
	def ageupdater(cls):
		cls.age+=1
		print(cls.age)
print(demo.age)
c=demo()
c.ageupdater()
c1=demo()
print(demo.age)
c1.ageupdater()
