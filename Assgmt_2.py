# -*- coding: utf-8 -*-
D={'ROM':['D1','des1'],
  'HDD':['D2','des2'],
   'FDD':['D3','des3'],
   'RAM':['D4','des4'],
   'CPU':['D5','des5']}
f=0

inp=input('Enter the device whose descp you want: ')
for i in D:
    if i==inp:
        print(D[i][1])

inp1=input('Enter the 1st charcter of device whose info you want: ')
for key,value in D.items():
    if inp1==key[0]:
        print(value)
        f=1
        #break
if f!=1:
    print('Device not found')
   # elif inp1=='R':
    #    print(D['ROM'],D['RAM'])

    #else:
     #   print('device not found')
      #  break
