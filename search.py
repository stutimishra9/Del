'''This is a program comprising of concatination of 2 lists and searching of desired element in it using functions
 l=[10,20,30]
>>> dev_id_search(50,l)
'Dev ID found,Dev ID=20Index=1'
>>> dev_id_search(50)
Traceback (most recent call last):
File "<input>", line 1, in <module>
TypeError: dev_id_search() missing 1 required positional argument: dev_list'''
def dev_id_search(dev_id,dev_list):
    if dev_id in dev_list:
        return 'Dev ID found,Dev ID='+str(dev_id)+'Index='+str(dev_list.index(dev_id))
    elif dev_id>max(dev_list):
        return 'Not found'
    else:
        for i in dev_list:
            if i>dev_id:
                return 'val='+str(i)+'ind='+str(dev_list.index(i))
def main():
    l1 = [1, 3, 5, 16, 8]
    l2 = [6, 5, 9, 4, 13, 12]
    l3=l1+l2
    s=set(l3)
    l4=list(s)
    l4.sort()
'''This is a program comprising of concatination of 2 lists and searching of desired element in it using functions
 l=[10,20,30]
>>> dev_id_search(50,l)
'Dev ID found,Dev ID=20Index=1'
>>> dev_id_search(50)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: dev_id_search() missing 1 required positional argument: 'dev_list'
'''
def dev_id_search(dev_id,dev_list):
    if dev_id in dev_list:
        return 'Dev ID found,Dev ID='+str(dev_id)+'Index='+str(dev_list.index(dev_id))
    elif dev_id>max(dev_list):
        return 'Not found'
    else:
        for i in dev_list:
            if i>dev_id:
                return 'val='+str(i)+'ind='+str(dev_list.index(i))
def main():
    l1 = [1, 3, 5, 16, 8]
    l2 = [6, 5, 9, 4, 13, 12]
    l3=l1+l2
    s=set(l3)
    l4=list(s)
    l4.sort()
    while True:
        i=input('Enter id to search:')
        i=eval(i)
        r=dev_id_search(i,l4)
        print('search res=',r)
        ch=input('Quit(y/n)?:')
        if ch=='y':
            break

if __name__=='__main__':
    main()
    import doctest
    doctest.testmod()