f1=open('log_report.txt','w')
f2=open('log_report.csv','w')
f1.write('IPL\tDATE\tPICS\tURL')
f2.writelines(['IP','DATE','PICS','URL\n'])
f3=open(r'C:\Python Training\New folder\Server Log')
for line in f3:
    if line[:3].isdigit():
        print(line)
        sp=line.split()
        print(sp)
        ip=sp[0]
        print(ip)
        dt=sp[3]#'[26/Apr/2000..'
        dt1=dt[1:12]
        dt2=dt[1:dt.index(':')]
        print(ip,dt2)
        #if sp[6].startswith('pics')
        if 'pics' in sp[6]:
            im=sp[6]#'/pics/abc.jpg'
            im1=im[6:]#1-way
            im2=im.split('/')
            im2=im2[-1]#2nd-way
            im3=im.lstrip('/pics/')#3-way
            im4=im.replace('/pics','')#4 way
        else:
            im1='No Image'
        #print(ip,dt2,im1)
        url=sp[10][1:-1]
        print(ip,dt2,im1,url,sep='\t',file=f1)
        print(ip, dt2, im1, url, sep='\t', file=f2)
f1.close()
f2.close()
f3.close()
