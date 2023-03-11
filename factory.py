class methoddemo:
    n=None
    def __init__(self):
        self.x=10
        self.y=20
    @staticmethod
    def objectcreator():
        if methoddemo.n is None:
            methoddemo.n=methoddemo()
        return methoddemo.n
    
m=methoddemo.objectcreator()
print('x={},y={}'.format(m.x,m.y))
m.x=20
m.y=30
m1=methoddemo.objectcreator()
print('x={},y={}'.format(m1.x,m1.y))
#print('id of m={ },id of m1={ }'.format(id(m),id(m1))
