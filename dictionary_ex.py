#dictionary->class
#dictionary doesnot produce the index values
l=['python',10,'Blr']
print(l[0])
d={'course':'python','dur':10,'loc':'Blr'}
print(d['course'])
#it's unordered

#add or update
d['course']=[d['course'],'c++','java']
print(d['course'])

d['adhaar']='cxvb'
print(d)
e=d.copy()
print(e['course'])
#print(d)
#remove
r1=d.pop('course')
print('pop=',r1,d)

del d['dur']
print('after del=',d)

r2=d.popitem()
print('r2=',r2,d)

#other methods
k=e.keys()
v=e.values()
i=e.items()
print(k,v,i,sep='\n')
