x=10
def f1():
    x=20 #enclosed scope
    def f2():
        #global y
        #y=200
        nonlocal x
        x=30 #local scope
        print('f2=',x)
    f2()
    print('f1=',x)
f1()
print('global=',x)

print(dir(__builtins__))