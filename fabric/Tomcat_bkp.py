import os
import time
import socket
os.system("ps aux | grep tomcat | grep -v grep |awk -F -Dcatalina.home= '{print $2}'| awk '{print $1}' 1>/tmp/tom.txt 2>/dev/null")
fp=open("/tmp/tom.txt")
x=fp.readlines()
Time=time.localtime()
v_time=str(Time[0])+"*"+str(Time[1])+"*"+str(Time[2])+"-"+str(Time[3])+"."+str(Time[4])+"."+str(Time[5])
v_host=socket.gethostname()
for i in x:
	v_org=i.rstrip("\n")
	v_data=v_host+"-"+v_org.split("/")[-1]+"-"+v_time+".tar.gz"
	os.system("mkdir -p /tmp/bkp")
	os.system(" tar cvfz /tmp/bkp/"+v_data+" "+ v_org +"&>/dev/null")

    
