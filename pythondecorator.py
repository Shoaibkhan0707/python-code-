def mydecorator(fn):
        def abc():
                print("decorating")
                fn()
                print('decorater')
        return abc
@mydecorator
def myfn():
        print('my function')
myfn()
#mydecorator(myfn)()
#a=mydecorator(myfn)
#a()

