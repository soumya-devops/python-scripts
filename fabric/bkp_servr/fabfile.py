from fabric import *
api.env.user="fabric"
api.env.password="soumya"
api.env.hosts="172.31.93.195"
def bkp_tom():
	api.run("mkdir -p /tmp/tomcat-bkps")
	api.put("/root/fabric/tombkp/*" , "/tmp/tomcat-bkps/")

