#unordered collection
#no index
#no key
#mutable
#hold only immutable objects
#always stores UNIQUE values

s={10,10,20,'py'} #even if it stores duplicate values only one value is taken into consideration
print(s)

#add
s.add(30)
s.add(30)
print('add=',s)

#remove#return type of remove is NONE
r1=s.remove(10)
print('remove=',s,r1)

r2=s.pop() #pop will remove any random value becoz set is an unordered collection
print('pop=',r2,s)

#set operations
s1={10,20,30,40}
s2={30,40,50,60}

s3=s1.union(s2)
print('union=',s3)

s4=s1.intersection(s2)
print('intersection=',s4)

s5=s1.difference(s2)
s6=s1-s2
print('difference=',s5)
print('difference=',s6)
