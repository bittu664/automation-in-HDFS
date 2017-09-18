#!/usr/python/bin

import commands
from os import system


def software():
	system("ls /projects/pack/soft > /projects/pack/list.txt")
	with open('/projects/pack/list.txt', 'r') as soft:
		l = soft.read().split()
		for item in l:
			system('rpm -ivh /projects/pack/soft/'+item)
			print "done install " + item

