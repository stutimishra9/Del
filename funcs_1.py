def add():
    a=10
    b=20
    c=a+b
    print('c=',c)
add()
add()
def get_ips():
    f=open(r'C:\Python Training\New folder\Server Log')
    ips= [line.split()[0] for line in f2 if line[:3].isdigit()]
    #f=open('serverlog.txt')
    ips=[]
    print('ips=',ips)
get_ips()
