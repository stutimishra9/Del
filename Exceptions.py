a=10
#b=0
try:
    r=a/b
    print('r=',r)
except:
    print('SOME ERROR')
try:
    r2=a/b
    print('r2=',r2)
except ZeroDivisionError:
    print('In ZDE')
except NameError as n:
    print('NE=',n)
except (KeyError,IndexError):
    print('KE or IE')

l=[]
try:
    print(l[1])
except Exception as e:
    print('e=',e)
    print('type=',type(e))

c=1
d=10
try:
    r=c/d
except:
    print('In except')
else:
    r=c/c
    print('In Else')

try:
    r=c/d
except:
    print('In except')
    #print(xyz)
finally:
    print('In finally')
#try finally
#try except finally
#try except else finally
e=10
f=0
try:
    if f==0:
        raise ZeroDivisionError
    print('stmt-100')
    r=e/f
except ZeroDivisionError:
    print('From raise')
result='Test case failed'
try:
    assert 'success' in result,'Some test failed'
    print('Testcase success')
except AssertionError as ae:
    print('ae=',ae)

class MyError(Exception):
    def __init__(self,m):
        self.msg=m
    def __str__(self):
        return 'ERROR DETAILS:'+self.msg
try:
    if 'sucess' not in result:
        raise MyError('Test Failed')
    else:
        print('Execution Success')
except MyError as me:
    print('me=',me)

