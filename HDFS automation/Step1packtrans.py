#!/usr/bin/python
import os
mip=raw_input("enter master ip address=")
mpasswd=raw_input("enter master password=")

#(STEP-1)---------------------------------------------------requirements--------------
print("""
1.DNS server must be configured.
2.hostname of all system must be seted.
3.entry of all systems must be done in /etc/hosts file of master and other systems.
5.ssh server service must  start on all systems including master.""")
print("\n")

#(STEP-2)------------------------------------------------ -to get packages on your system-------------
print("packages are transmiting on master at /Hadoop-v1...........")
cmd="sshpass -p "+mpasswd+" scp -r  -o StrictHostKeyChecking=no  /Hadoop-v1   "+mip+":/  "
os.system(cmd)
os.system("sshpass -p "+mpasswd+" ssh -o StrictHostKeyChecking=no -l root "+mip+" rpm -ivh /Hadoop-v1/nmap-6.40-7.el7.x86_64.rpm")
os.system("sshpass -p "+mpasswd+" ssh -o StrictHostKeyChecking=no -l root "+mip+" rpm -ivh /Hadoop-v1/sshpass-1.05-1.el7.rf.x86_64.rpm ")

print(" Transfer Done")




