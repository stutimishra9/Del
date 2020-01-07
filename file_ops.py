F1=open('out1.txt','w')
x=10
s='python\n'
x=str(x)+'\n'
F1.write(x)
F1.write(s)
F1.flush()
#2nd way to write
l=[x,s]
F1.writelines(l)
F1.close()

f2=open('out1.txt','r')
r1=f2.read()
print('r1=',r1)

f2.seek(0)
r2=f2.read()
print('r2=',r2)

f2.seek(0)
r3=f2.readline()
print('r3=',r3)
while True:
    line=f2.readline()
    if line=='':#EOF
        break
    else:
        print('line=',line)

f2.seek(0)
r4=f2.readlines()
print('r4=',r4)
r5=[]
for l in r4:
    l=l.strip()
    r5.append(l)
print('r5=',r5)

f2.seek(0)
for x in f2:
    print('line=',x)

f2.seek(0)
r6=list(f2)
f2.seek(0)
r7=tuple(f2)

l1=['h1','h2']
l2=['ip1','ip2']
D1=dict(zip(l1,l2))
print('D1=',D1)

e=enumerate (l1)
print(list(e))

f2.seek(0)
D2=dict(enumerate(f2))
print('D2=',D2)
f2.close()

f3.open('oot1.txt','a')
f4.open('out2.csv','a')

print(20,'java',sep='\n',file=f3,flash=True)
print(20,'java',sep='\n',file=f4)
f3.closed
f3.closed

#'wb'
#
