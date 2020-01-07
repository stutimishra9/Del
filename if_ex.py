a=0
if a==10:
    print('a equal to 10')
if a>10:
    print('a gt 10')
if a<10:
    print('a lt 10')
#a=0
if a==10:
    print('a equal to 10')
elif a>10:
    print('a gt 10')
elif a<10:
    print('a lt 10')
#a=0
if a==10:
    print('a equal to 10')
elif a>10:
    print('a gt 10')
else:
    print('a lt 10')

s='python'
if 'th' in s:
    print('substring found')
if not s.startswith('java'):
    print('not java')
if not s!='c++':
    print('not c++')
if s[1:3]=='yt':
    print('yt found')

l1=[10,20]
l2=l1
l3=l1.copy()
if 20 in l1:
    print('20 found')
if l1 is l2:
    print('Both refers same object')
if id(l1)==id(l2):
    print('Both refers same object')
if l1==l3:
    print('contents are same')

D={'A':10,'B':20}
if 'B' in D:
    print('key-B found')
if 'B' in D.keys():
    print('key-B found')
if 20 in D.values():
    print('20 found')
if ('A',10) in D.items(): #[('A',10),('B',20)]
    print('item found')
if a==10:
    pass