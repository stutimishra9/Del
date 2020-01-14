list1=[1,3,5,16,8]
list2=[6,5,9,4,13,12]
list3=list1+list2
#print(list3)
set3=set(list3)
#print(set3)
list3=list(set3)
print(list3)
n=input('enter the value you wanna search: ')
n=eval(n)
k=0
#print(n)
#for i in list3:
 #   if i>n:
#    print('not found')
for i in list3:
    if i==n:
        print('found')
        print('index and value is respectively: ',list3.index(i),n)
        k=1
        break
if k!=1:
    for i in list3:
        if i > n:
            print('not found')
            print('index and value is respectively: ', list3.index(i), i)
            break
        elif n>max(list3):
            print('not found')
            break


#   print('not found')
        #for i in list3:

      # x=id(i)

        #break
    #i=i+1
#s=list3[0]
#i=0
#for i in list3:
#    if list3[i]!=n:
#else:
  #          s=list3[i]
   #         g=list3[i+1]
    #        i=i+1
#for i in list3:
 #   if list3[i]<=n:
