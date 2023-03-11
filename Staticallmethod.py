class methoddemo:
    z=20
    def __init__(self):
        self.x=10 #class ke member ko call kr skta hai
        self.y=20
    def imethod(self):
        print('x={},y={},z={}'.format(self.x,self.y,self.__class__.z))
    @classmethod
    def cmethod(cls):
        print('z={}'.format(cls.z))
    @staticmethod
    def smethod():
         print('z={}'.format(methoddemo.z))
    
m=methoddemo()
print(id(m))
m1=methoddemo()
print(id(m1))
if m==m1:
	print('true')
else:
	print('false')
m.imethod()
m.cmethod()
methoddemo.cmethod()
methoddemo.smethod()
