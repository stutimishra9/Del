import paramiko as p
client=p.SSHClient()
client.set_missing_host_key_policy(p.AutoAddPolicy)
client.connect('test.rebex.net',username='demo',password='password',port=22)
stdin,out,err=client.exec_command('ls')
cmd_out=out.read()
print('cmd_out=',cmd_out)
ftp=client.open_sftp()
ftp_out=ftp.get('readme.txt','ftp_readme.txt')
print('ftp_out=',ftp_out)
ftp.put('out1.txt','out1.txt')