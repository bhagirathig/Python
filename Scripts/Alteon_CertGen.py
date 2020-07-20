import paramiko
import time

ip_address = "127.0.0.1"
username = "username"
password = "password"
f = open ('Certificate-List.txt')

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print ("Successful connection to", ip_address)

remote_connection = ssh_client.invoke_shell()

for line in f:

	remote_connection.send("/c/slb/ssl/certs/cert " +line+"\n")
	time.sleep(1)
	remote_connection.send("generate\n")
	time.sleep(1)
	remote_connection.send("rsa\n")
	time.sleep(1)
	remote_connection.send("2048\n")
	time.sleep(1)
	remote_connection.send("sha256\n")
	time.sleep(1)
	remote_connection.send(line+"\n")
	time.sleep(1)
	remote_connection.send("n\n")
	time.sleep(1)
	remote_connection.send("y\n")
	time.sleep(1)
	remote_connection.send("3650\n")
	time.sleep(5)

remote_connection.send("lines 0\n")
remote_connection.send("verbose 0\n")
remote_connection.send("diff\n")
time.sleep(10)
remote_connection.send("apply\n")
time.sleep(10)
remote_connection.send("save\n")
remote_connection.send("y\n")
time.sleep(5)
remote_connection.send("lines 100\n")
remote_connection.send("verbose 32\n")

ssh_client.close
