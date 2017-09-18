#!/usr/bin/python

import os
import commands

s1 ="export JAVA_HOME=/usr/java/jdk1.7.0_79"
s2 ="export PATH=$JAVA_HOME/bin:$PATH"

os.system('export JAVA_HOME=/usr/java/jdk1.7.0_79')
os.system('export PATH=$JAVA_HOME/bin:$PATH')

def path():
	os.system('echo /root/.bashrc > utils.txt')
	with open('utils.txt' , 'r') as file:
		var = file.read()
	if s1 in var:
		print "already set"
	else:
		print "setting java_home"	
		os.system('echo '+s1+' >> /root/.bashrc')
		print "java home set"

	if s2 in var:
		print "path already set"
	else:
		print "setting path"	
		os.system('echo '+s2+' >> /root/.bashrc')
		print "path set"
		
	c = '[cdrpm]\nbaseurl="file:///run/media/root/RHEL-7.3 Server.x86_64"\ngpgcheck=0'
	os.system('echo ' + c + ' > /etc/yum.repos.d/cdrpm.repo')

	print "all done"


