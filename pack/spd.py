#!/usr/bin/python
import os
import commands
def ipp():


	ip_list = ['192.168.43.200', '192.168.43.102']
	ip = raw_input("enter the ip address")
	if ip in ip_list:
		ip_list = [i for i in ip_list if i != ip]

	#os.system("sshpass -p redhat ssh -o stricthostkeychecking=no root@"+ip)
	os.system("sshpass -p redhat scp -r -o stricthostkeychecking=no /root/projects/pack/software/ root@"+ip":/root/software")
	os.system("sshpass -p redhat ssh -o stricthostkeychecking=no root@"+ip" rpm -ivh /root/software/jdk*   hadoop* --replacefiles")
	os.system("sshpass -p redhat scp -r -o stricthostkeychecking=no /root/projects/pack/.bashrc root@"+ip":/root/.bashrc")
	os.system("sshpass -p redhat scp -r -o stricthostkeychecking=no /projects/pack/hdfs-site.xml root@"+ip+":/etc/hadoop/")
	
	
	
	

	for ip in ip_list:
	
		#os.system("sshpass -p redhat ssh -o stricthostkeychecking=no root@"+ip)
		os.system("sshpass -p redhat scp -r -o stricthostkeychecking=no /projects/pack/software/  root@"+ip+":/root/software")
		os.system("sshpass -p redhat ssh -o stricthostkeychecking=no root@"+ip" rpm -ivh /root/software/jdk*  hadoop*  --replacefiles")
	os.system("sshpass -p redhat scp -r -o stricthostkeychecking=no /root/projects/pack/.bashrc root@"+ip":/root/.bashrc")
		
		os.system("sshpass -p redhat scp -r -o stricthostkeychecking=no /root/Public/hdfs-site.xml root@"+ip+":/etc/hadoop/")
	
		
