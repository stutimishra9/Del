f1=open('SSH_log_Sample.txt','r')
r1=f1.readlines()
#print('r1=',r1[0][0])
cnt=0
for i in r1:
    if 'Failed password' in i:
        cnt=cnt+1
print('No of failed login attempt:',cnt)
for i in r1:
    if 'sshd version' in i:
        print('sshd version:',i[20],i[21],i[22],i[23],i[24],i[25],i[26],i[27],i[28],i[29],i[30],i[31])
        break
for i in r1:
    if 'rsa' in i:
        print('Encyption:',i[36],i[37],i[38],i[39],i[40],i[41],i[42])
        break

for i in r1:
    if 'Accepted password' in i:
        print('Successful Login User:',i[58],i[59],i[60],i[61])
        print('ip:', i[68], i[69], i[70], i[71],i[72],i[73],i[74],i[75],i[76],i[77])
        print('port:', i[84], i[85], i[86], i[87])



#import re
#for i in r1:

    #if i=='F' and r1[i.index(i)+7]=='p':
     #   cnt=cnt+1
#print(cnt)
        #ind=i.index(i)
        #if r1[ind + 7] == 'p':
         #   cnt = cnt + 1
          #  print(cnt)'''

        #if r1[ind+1]=='a' and r1[ind+2]=='i' and r1[ind+3]=='l' and r1[ind+4]=='e' and r1[ind+5]=='d'and r1[ind+6]==' ' and r1[ind+7]=='p'and r1[ind+8]=='a' and r1[ind+9]=='s' and r1[ind+10]=='s' and r1[ind+11]=='w' and r1[ind+12]=='o' and r1[ind+13]=='r' and r1[ind+14]=='d':

'''import re
for line in f1:
    if re.match('Failed password'):
        cnt=cnt+1
        print(cnt)
'''