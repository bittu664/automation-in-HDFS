
import commands
import os
def ipfun():
	ip_list = {"subhash":'192.168.43.173'}
	  
	

	for ip in ip_list:
		print ip_list[ip]
		
		#os.system( root@192.168.43.173')
		os.system('sshpass -p redhat ssh -o stricthostkeychecking=no scp -r /projects '+ ip + ':/root/software')
		
	
		print "done for {}".format(ip)




 






