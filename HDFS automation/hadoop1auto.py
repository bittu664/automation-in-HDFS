#!/usr/bin/python
import commands,os
import sysscan
import resourcescan

	


retdata=sysscan.sysscan()
iplist=retdata[0]
hostlist=retdata[1]
npasswd="redhat"
print iplist
print hostlist

mhn=commands.getoutput("hostname ")
mipinfo=commands.getoutput("hostname -I")
mip=mipinfo.split()[0]

msel=raw_input("do you want to add your system(master) in cluster")

if(msel=='n' or msel=='N'):
	try :	
		iplist.remove(mip)
		hostlist.remove(mhn)
	except	ValueError :
		iplist.remove(mhn)

oip="192.168.122.1"
ohn="virtualmachine"
iplist.remove(oip)
hostlist.remove(ohn)
#######*****************************************************************************************************

#(STEP-3)--------------------------to distribute Hadoopv-1 folder to all systems of master and install them----------------------
for ip in iplist:
	com1="sshpass -p "+npasswd+" scp -r  -o StrictHostKeyChecking=no  /Hadoop-v1   "+ip+":/  "
	os.system(com1)
	com2="sshpass -p "+npasswd+" ssh   -o StrictHostKeyChecking=no  -l root  "+ip+"  bash /Hadoop-v1/script1.sh   "
	os.system(com2)
  
##***************************************************************************************************************


ipramdict=resourcescan.resrcscan(iplist)
hadoop_v1_dirpath="/Hadoop-v1"
####################################(HADOOP-V-1 WITH MAPREDUCE)################################################################### ----------------------------------------------------------------------------------------------------------------------------------------------

def hdfs(iplist,ipramdict,hadoop_v1_dirpath,npasswd):
		
		hcfloc=hadoop_v1_dirpath+"/hdfs"

		maxram=0
		for ip in iplist:
		     if maxram < ipramdict[ip]:
			     maxram=ipramdict[ip]
			     nnip=ip
		NNIP=nnip

##NAMENODE CONFIGURATION---------------------------------------------------------------------------------------------------------
		nncfloc=hcfloc+"/nn"
		nnserport="10001"
		com3="sed  -i  's/hostname_of_nn:nn_ser_port/"+nnip+":"+nnserport+"/'  "+nncfloc+"/core-site.xml   "

		os.system(com3)
		com4="sed  -i  's/hostname_of_nn/"+nnip+"/'  "+nncfloc+"/hdfs-site.xml   "
		os.system(com4)
		com5="sshpass -p "+npasswd+" scp   -o StrictHostKeyChecking=no  "+nncfloc+"/*   "+nnip+":/etc/hadoop/  "
		os.system(com5)
		com6="sshpass -p "+npasswd+" ssh   -o StrictHostKeyChecking=no  -l root  "+nnip+"  bash /Hadoop-v1/script2.sh   "
		os.system(com6)
		com7="sshpass -p redhat ssh  -o StrictHostKeyChecking=no -l root "+nnip+"  /usr/java/jdk1.7.0_79/bin/jps "
		nnss=commands.getoutput(com7)
		nnssinfo=nnss.split()
				
		for service in nnssinfo:
			try:			
				if service=="NameNode":
					print "NameNode "+nnip+" Service Is Running"
			except:
				print "NameNode "+nnip+" Service Is Not Running"	
		
##JOBTRACKER-----CONFIG----------------------------------------------------------------------------------------------------------------------
		iplist.remove(nnip)
		del ipramdict[nnip]
		jmaxram=0
		for ip in iplist:
		     if jmaxram < ipramdict[ip]:
			     maxram=ipramdict[ip]
			     jtip=ip
		JTIP=jtip
		jtserport="9002"
		hmrcfloc=hadoop_v1_dirpath+"/mapreduce"
		jtcfloc=hmrcfloc+"/jt"
		com8="sed  -i  's/hostname_of_nn:nn_ser_port/"+nnip+":"+nnserport+"/'  "+jtcfloc+"/core-site.xml   "
		os.system(com8)
		com9="sed  -i  's/host_name_of_jobtracker:jt_ser_port/"+jtip+":"+jtserport+"/'  "+jtcfloc+"/mapred-site.xml   "
		os.system(com9)
		com10="sshpass -p "+npasswd+" scp   "+jtcfloc+"/*   "+jtip+":/etc/hadoop/  "
		os.system(com10)
		com11="sshpass -p "+npasswd+" ssh  -o StrictHostKeyChecking=no -l root "+jtip+"    hadoop-daemon.sh start jobtracker  "
		os.system(com11)
		com12="sshpass -p redhat ssh  -o StrictHostKeyChecking=no -l root "+jtip+"  /usr/java/jdk1.7.0_79/bin/jps "
		nnss=commands.getoutput(com12)
		nnssinfo=nnss.split()
				
		for service in nnssinfo:
			try:			
				if service=="JobTracker":
					print " "+jtip+"'s JobTracker Service Is Running"
			except:
				print " "+jtip+"'s JobTracker Service Is Not Running"		

	

##-----------------------------------DATANODE AND TASKTRACKER CONFIGURATION-----------------------------------------------------------------------
		iplist.remove(jtip)
		del ipramdict[jtip]
		
		snnmaxram=0
		for ip in iplist:
		     if snnmaxram < ipramdict[ip]:
			     maxram=ipramdict[ip]
			     snnip=ip
		
		SNNIP=snnip
		iplist.remove(snnip)
		del ipramdict[snnip]
		dniplist=iplist
		dncfloc=hcfloc+"/dn"
		ttcfloc=hmrcfloc+"/tt"
		com13="sed  -i  's/hostname_of_nn:nn_ser_port/"+nnip+":"+nnserport+"/'  "+dncfloc+"/core-site.xml   "
		os.system(com13)
		com14="sed  -i  's/host_name_of_jobtracker:jt_ser_port/"+jtip+":"+jtserport+"/'  "+ttcfloc+"/mapred-site.xml   "
		os.system(com14)
		
		DNIPLIST=dniplist
		for dnip in dniplist:
			com15="sshpass -p "+npasswd+"  scp  "+dncfloc+"/*   "+dnip+":/etc/hadoop/  "
			os.system(com15)
			com16="sshpass -p "+npasswd+"  scp  "+ttcfloc+"/*   "+dnip+":/etc/hadoop/  "
			os.system(com16)
			com17="sshpass -p "+npasswd+" ssh   -o StrictHostKeyChecking=no  -l root  "+dnip+"  bash /Hadoop-v1/script3.sh   "
			os.system(com17)
			com18="sshpass -p redhat ssh  -o StrictHostKeyChecking=no -l root "+dnip+"  /usr/java/jdk1.7.0_79/bin/jps "
			dnss=commands.getoutput(com18)
			dnssinfo=dnss.split()
			for service in dnssinfo:
				try:			
					if service=="DataNode"  :
						print " "+dnip+"'s DataNode  Service Is Running"
				except:
					print " "+dnip+"'s DataNode  Service Is Not Running"	

			for service in dnssinfo:
				try:			
					if service=="TaskTracker":
						print " "+dnip+"'s TaskTracker Service Is Running"
				except:
					print " "+dnip+"'s TaskTracker Service Is Not Running"	
			

		
		allinfo=(NNIP,DNIPLIST,JTIP,SNNIP)
		
	 	return allinfo

###############################################################HADOOP-V-1######################################################			

def info_of_nodes(nnip,dniplist,jtip,snnip):
	print "your nodes and their service status---"
	print "NAMENODE INFO:--"
	print "NNIP (or HOSTNAME) :--",nnip
	print "DATANODE INFO:--"
	for ip in dniplist:
		print "DN and TT IP (or HOSTNAME) :--",ip
	print "JOBTRACKER INFO:--"
	print "JTIP (or HOSTNAME) :--",jtip
	print "SECONDARY NAMENODE INFO:--"
	print "NNIP (or HOSTNAME) :--",snnip
	
#------------------------------------------------------------------------------------------------------------------------------
def hadoop_chkpointing(NNIP,SNNIP,hadoop_v1_dirpath,chkpp):
	snncfloc=hadoop_v1_dirpath+"/secondarynamenode"	
	nnserport="10001"
	com19="sed  -i  's/hostname_of_nn:nn_ser_port/"+NNIP+":"+nnserport+"/'  "+snncfloc+"/core-site.xml   "
	os.system(com19)
	com20="sshpass -p "+npasswd+" ssh  -o StrictHostKeyChecking=no -l root "+NNIP+"   hostname"
	hostname_of_primarynn=commands.getoutput(com20)
	com21="sshpass -p "+npasswd+" ssh  -o StrictHostKeyChecking=no -l root "+SNNIP+"   hostname"
	hostname_of_secondarynn=commands.getoutput(com21)
	com22="sed  -i  's/hostname_of_primarynn/"+hostname_of_primarynn+"/'  "+snncfloc+"/hdfs-site.xml   "
	os.system(com22)
	com23="sed  -i  's/hostname_of_secondarynn/"+hostname_of_secondarynn+"/'  "+snncfloc+"/hdfs-site.xml   "
	os.system(com23)
	com24="sed  -i  's/chk_point_period/"+chkpp+"/'  "+snncfloc+"/hdfs-site.xml "
	os.system(com24)
	com25="sshpass -p "+npasswd+" ssh   -o StrictHostKeyChecking=no  -l root  "+SNNIP+"  bash /Hadoop-v1/script4.sh   "
	os.system(com25)
	
	
	
##MENU---------------------------------------------------------------------------------------------------------------------------------------------------

chfc="y"

while chfc=="y" or chfc=="Y":
	os.system("clear")
	os.system("tput setab 4")
	print "		Menu    	"	
	print "Press 1 for Hadoop-Version-1 with mapreduce "
	print "Press 2 for Hadoop-Version-2 with yarn"
	print "Press 3 for Hive"
	print "Press 4 for Pig "
	print "Press 5 for Splunk "
	os.system("tput setab 4")

	ch=int(raw_input("enter your choice-->>"))
		
	if ch==1:
		main_info=hdfs(iplist,ipramdict,hadoop_v1_dirpath,npasswd)	
		print "CLUSTER INFO",main_info
		#nnip=main_info[0]
		#dniplist=main_info[1]
		#jtip=main_info[2]
		#snnip=main_info[3]
	elif ch==2:
		chkpp=raw_input("enter the check pointing period(in sec)")
		hadoop_chkpointing(nnip,snnip,hadoop_v1_dirpath,chkpp)
		info_of_nodes(nnip,dniplist,jtip,snnip)
	elif ch==3:
		print "3"
	elif ch==4:
		print "4"
	elif ch==5:
		print "5"
	else :
		print "invalid option"
	
	os.system("tput setab 1")
	chfc=raw_input("do you want to continue-->>")
	os.system("tput setab 4")
	

#-------------------------------------------------


	
