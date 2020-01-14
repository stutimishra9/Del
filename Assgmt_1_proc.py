'''This is a program comprising of concatination of 2 lists and searching of desired element in it using procedures'''
l1=[1,3,5,16,8]
l2=[6,5,9,4,13,12]
l3=l1+l2
s=set(l3)
l4=list(s)
l4.sort()
while True:
    in_val=input('Enter Device ID:')
    in_val=int(in_val)
    if in_val in l4:
        print('Device ID Found,ID=',in_val,'Its Index:',l4.index(in_val))
    elif in_val>max(l4):
        print('not found')
    else:
        for i in l4:
            if i>in_val:
                print('val=',i,'ind=',l4.index(i))
                break
    ch=input('Do you want to Quit(y/n)?:')
    if ch=='y':
        break
