s='python'
for a in s:
    print('a=',a)
b='java'
l=[10,20,30]
for b in l:
    print('b=',b)
print('Now a and b=',a,b)

D={'A':10,'B':20}
for k in D:
    print('k=',k)

line='-'*40
print(line)

for k in D.keys():
    print('key=',k,'value=',D[k])

print(line)

for v in D.values():
    print('v=',v)

print(line)

for i in D.items(): #[('A',10),('B',20)]
    print('i=',i,i[0],i[1])

print(line)
#i=('A',10)
for i,j in D.items():
    print(i,j)
print(line)

hosts=['h1','h2','h3']
ips=['ip1','ip2']
z=zip(hosts,ips)
print(z)
print(list(z))

for h,p in zip(hosts,ips):
    print(h,p)

#for h,p in z:
#   print(h,p)

print(line)
#for()

r1=range(10)
r2=range(1,10)
r3=range(1,10,2)
print(list(r1),list(r2),list(r3),sep='\n')
r4=range(10,1,-1)
print(list(r4))
for i in range(2,10,2):
    print('i=',i)

print(line)

for h in range(0,len(hosts)):
    print(hosts[h])

for h in range(0,len(hosts),2):
    print(hosts[h])

for h in hosts[::2]:
    print('h=',h)

print(line)

comp=['IBM','DEL1','SAP','DEL2']
f=0
for c in comp:
    if c.startswith('DEL'):
        print('found')
        f=1
        break
    #else:
     #   print('not found')
if f==0:
    print('not found')
print(line)
for i in comp:
    if not i.startswith('DEL'):
        continue
    if i.startswith('DEL'):
        print('some logic')
    print('last statmenet of for')