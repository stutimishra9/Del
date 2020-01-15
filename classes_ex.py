class Account1:
    def adduser(self,n):
        self.name=n
    def viewuser(self):
        return self.name
    bank='ICICI'
    @classmethod
    def bankrules(cls,area):
        return 'Bank Rules'+area
    @staticmethod
    def bankinfo():
        return 'Bank Info'
    def __init__(self):
        print('SB LOGIC HERE')
class Account2(Account1):
    def addadhar(self,a):
        self.adhar=a
    def viewadhar(self):
        return self.adhar
    def viewuser(self):
        return 'Welcome'+self.name
    def __init__(self):
        super().__init__()
        print('CA LOGIC HERE')
        #Account1.__init__(self)
class RBI:
    def viewrules(self):
        return 'RBI Rules'
class Account3(Account2,RBI):
    pass
class Govt:
    def viewrules(self):
        return 'Govt Rules'
class Account4(Account3,Govt):
    pass
class Account5(Account3):
    def __init__(self):
        self.gov=Govt()
class Account6:
    def __init__(self,n):
        self.name=n
    def __add__(self,x):
        return self.name+x.name
    def __str__(self):
        return self.name
    def __len__(self):
        return len(self.name)
    def __iter__(self):
        self.count=0
        return self
    def __next__(self):
        c=self.count
        if c<len(self.name):
            self.count+=1
            return self.name[c]
        else:
            raise StopIteration
from abc import ABC,abstractmethod
class Account(ABC):
    def adduser(self,a):
        self.name=a
    @abstractmethod
    def viewuser(self):
        pass
class MyAccount(Account):
    def viewuser(self):
        return 'Hello'+'self.name'
cust1=Account1()
cust2=Account1()
cust1.adduser('c1')
cust2.adduser('c2')
print(cust1.viewuser())
print(cust2.viewuser())
print(Account1.bank)
print(cust1.name)
print(Account1.bank)
print(cust1.name)
print(Account1.bankrules('BLR'))
print(Account1.bankrules('BLR'))
print(Account1.bankinfo())
print(Account1.viewuser(cust2))
cust3=Account2()
cust3.adduser('c3')
print(cust3.viewuser())
print(Account2.bank)
print(Account2.bankrules('BLR'))
print(Account2.bankinfo())
cust3.addadhar('A1')
print(cust3.viewadhar())
cust4=Account3()
print(cust4.viewrules())
cust4.adduser('c4')
cust5=Account4()
print(cust5.viewrules())
print(Govt.viewrules(cust5))
cust6=Account5()
print(cust6.viewrules())
print(cust6.gov.viewrules())
cust7=Account6('abc')
cust8=Account6('xyz')
result=cust7+cust8
print('result=',result)
print('cust7=',cust7)
print('length=',len(cust7))
for i in cust7:
    print('i=',i)
#a=Account
b=MyAccount()
b.adduser('B')
print(b.viewuser())