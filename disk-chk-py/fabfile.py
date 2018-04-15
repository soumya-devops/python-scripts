from fabric import *
api.env.user="root"
api.env.password="root"
api.env.hosts=["172.31.95.233","172.31.93.200"]
def task():
	api.put("/root/fabric/disk.py","/root/")
	api.run("python /root/disk.py")
