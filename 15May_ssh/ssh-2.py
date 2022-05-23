from paramiko import SSHClient
from paramiko.client import AutoAddPolicy
import sys

def ssh():
    client = SSHClient()                            #short cut assigned to client instead SSHClient
    client.set_missing_host_key_policy(AutoAddPolicy)   #add host machine in known_host
    client.connect(hostname=sys.argv[1],username=sys.argv[2],password=sys.argv[3])   #connect to Host Machine and key_file=/home/gaurav/.ssh/id_rsa, port=24
    stdin, stdout, stderr = client.exec_command(sys.argv[4])        #3 output and assigned variable
    print(stdout.read().decode())                           #print stdout
    print(stderr.read().decode())                           #print stderr
    client.close()


ssh()