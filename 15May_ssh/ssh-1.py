from http import client
from sys import stderr, stdin, stdout
from paramiko import SSHClient
from paramiko.client import AutoAddPolicy
import getpass

host_name = input("Enter IP or hostname: ")
user_name = input("Enter username: ")
passwd = getpass.getpass("Enter password: ")
cmd = input("Enter command to execute: ")
#print(host_name)
#print(user_name)
#print(passwd)
#print(cmd)

def ssh(host_name,user_name,passwd,cmd):
    client = SSHClient()                            #short cut assigned to client instead SSHClient
    client.set_missing_host_key_policy(AutoAddPolicy)   #add host machine in known_host
    client.connect(hostname=host_name,username=user_name,password=passwd)   #connect to Host Machine and key_file=/home/gaurav/.ssh/id_rsa, port=24
    stdin, stdout, stderr = client.exec_command(cmd)        #3 output and assigned variable
    print(stdout.read().decode())                           #print stdout
    print(stderr.read().decode())                           #print stderr
    client.close()


ssh(host_name,user_name,passwd,cmd)