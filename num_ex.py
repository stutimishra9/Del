#Core Datatypes
#Numbers
#Strings
'''
LIST
TUPLE
'''
"""
Dictionary
Set
"""
#Numbers
a=10#int
b=12.5#float
c=0*12#hex
d=0b1010#bin
e=0O12#oct
print('Hello')
print('a')
print('result=',a,b,c,d,e,sep='|',end='.')
print('Test')#file=,flush=
f=int(20)
print(f)
print(a)
print(id(a))#prints reference or adress of a
print(type(a))
print(type(a).__name__)
a=100
print(id(a))
b=a#reference copy
print(b)
print(id(a))
a=200
print(a)
print(id(a))
b=300
print(b)
print(id(b))
#Sys.getRefcount
