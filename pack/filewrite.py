import os
import commands

def filewrite():
	f_list=["core-site.xml", "hdfs-site.xml" , "mapred-site.xml"]
	c_dir = "/root/etc/hadoop/"
	for f in f_list:
		os.system("cp /root/etc/hadoop/"+f+" /root/etc/hadoop/")
		return "done"

