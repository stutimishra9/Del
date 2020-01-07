#list->class
l1=list([10,20,30])
l2=[10,12.5,'python',['a','b']]
print(l2)
print(l2[1])
print(l2[2][1])
print(l2[-1:1:-1])
#add
l2.append(200)
print('append=',l2)
l2.insert(2,300)#insert 300 on 2nd position
print('Insert=',l2)
l3=[10,20]
l4=['a','b']
l5=l3+l4
l6=l3*10
print(l5,l6,sep='\n')
l3.extend(l4)
print('Extend=',l3)#not creating a new object, extending l3

#remove
r1=l5.pop()
print('r1=',r1,l5)
r2=l5.pop(2)
print('r2=',r2,l5)
r3=l5.remove(20)#removes only one 20 from the left side
print('remove=',r3,l5)
del l5[0]
print('After del=',l5)

#update
print('l3=',l3)
l3[1]='java'
print('After update=',l3)

#some other methods
l6=[10,30,20]
l6.sort() #ascending
#sort doesnt work on heterogenous data
print('sort asc=',l6)
l7=['z','a','b']
l7.sort(reverse=True) #desc
print('sort desc=',l7)
l8=[10,'a',20,'b']
l8.reverse()
print('reverse=',l8)
#list is the collection of references

l8.clear()
print('l5=',l5)
#copy
l=[10,['a','b']]
m=l #reference copy
n=l.copy() #shallow copy

#copy module->copy(),deepcopy()
import copy
p=copy.deepcopy(l)
print(id(l[0]),id(p[0]))
print(id(l[1]),id(p[1]))
cp=copy.deepcopy
q=cp(l)
