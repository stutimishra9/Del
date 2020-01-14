import Assgmt_1func as af
while True:
    i=input('Enter ID: ')
    i=eval(i)
    l=[10,20,30]
    r=af.dev_id_search(i,l)
    print('result=',r)
    ch=input('Quit(y/n)?:')
    if ch=='y':
        break