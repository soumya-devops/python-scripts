#create 5 no of tomcat with configuring different port
import os
v_connectorport=8080
v_shutdownport=8005
v_ajpport=8009
os.system("cp -rf /home/ec2-user/apache-tomcat-7.0.39.tar.gz /root")#downloaded tomcat tar file,copy to root
os.system("tar -xvf /root/apache-tomcat-7.0.39.tar.gz &>/dev/null")#untar tomcat
for i in range(1,6):
	os.system("cp -rf /root/apache-tomcat-7.0.39 /usr/local/tomcat"+str(i))#create 5 no of tomcat 
for i in range(2,6):
	v_connectorport=v_connectorport+10
	v_shutdownport=v_shutdownport+10
	v_ajpport=v_ajpport+10
	fp=open("/usr/local/tomcat"+str(i)+"/conf/server.xml")
	v_serverxml= fp.read()
	x=v_serverxml.replace("8080",str(v_connectorport))
	y=x.replace("8005",str(v_shutdownport))
	z=y.replace("8009",str(v_ajpport))
	fp=open("/usr/local/tomcat"+str(i)+"/conf/server.xml","w")
	fp.write(z)
	fp.close()
for i in range(1,6):
	os.system("sh /usr/local/tomcat"+str(i)+"/bin/startup.sh")
	 
