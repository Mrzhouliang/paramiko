#!/usr/bin/env python
#coding=utf-8
#date:2016-07-27
#开始学习写python,20160727 111111

import paramiko
import time

def _deploy(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        print stdout.read()
        print '%s\tOK\n'%(ip)
        ssh.close()
    except:
        print '%s\tError\n'%(ip)


def _put():
    iplist = ['192.168.1.100','192.168.1.101']
    for i in iplist:
        _perip = i
        scp=paramiko.Transport((_perip,22))
        scp.connect(username='root',password='123456')
        sftp=paramiko.SFTPClient.from_transport(scp)
        sftp.put('/root/mobile.zip','/data/m.xxxx.com/mobile.zip')
        scp.close()

_put()
print '##################上传完成####################################'
time.sleep(3)

print '##################开始备份####################################33333333333333'
_deploy("123.57.48.60","root","123456",'cd /data/m.xxxx.com;tar czf bak/mobile.`date "+%Y-%m-%d-%M"`.tar.gz mobile')
_deploy("123.57.0.49","root","123456",'cd /data/m.xxxx.com;tar czf bak/mobile.`date "+%Y-%m-%d-%M"`.tar.gz mobile')
print '##################备份完成，开始部署#############################'
_deploy("123.57.48.60","root","123456",'cd /data/m.xxxx.com;unzip -o mobile.zip')
_deploy("123.57.0.49","root","123456",'cd /data/m.xxxx.com;unzip -o mobile.zip')
print '##################部署完成，请验证#############################'
_deploy("123.57.48.60","root","123456",'cd /data/m.xxxx.com;rm -f mobile.zip')
_deploy("123.57.0.49","root","123456",'cd /data/m.xxxx.com;rm -f mobile.zip')
print '##################清理软件包完成#############################1111wwwww####'
