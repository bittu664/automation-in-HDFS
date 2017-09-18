#########IPSCAN-------------------------------------------------------------------------------------------------------------------------------------
import commands
def sysscan():
	iprange=raw_input("enter the ip range(NETWORK ID) for network scanning-->>")
	print("dns server configured or not ?")
	dnsstatus=raw_input("press n or N for NO-- and y for yes>>")
	print(dnsstatus)
	
		
	if(dnsstatus=="y" or dnsstatus=="Y"):
		nh1="nmap -sP "+iprange+".0/24  --system-dns | grep 'Nmap scan report' | awk  '{print$6}' "			
		ipdata=commands.getoutput(nh1)
		ipinfo=ipdata.split()
		iplist=[]
		for i in ipinfo:
			iplist.append(i[1:-1])

		nh2="nmap -sP "+iprange+".0/24   --system-dns | grep 'Nmap scan report' | awk  '{print$5}' "
		hostinfo=commands.getoutput(nh2)
	
	else:
		print("please configure DNS server first then try again")
		exit()

	
	hostlist=hostinfo.split()
	tup=(iplist,hostlist)

	
	return tup
