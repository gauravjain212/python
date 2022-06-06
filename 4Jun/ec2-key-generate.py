import boto3
import os

ec2 = boto3.resource('ec2')

key_pair = ec2.create_key_pair(KeyName='python8am')

with open ('python8am.pem','w') as outputfile:
    outputfile.write(str(key_pair.key_material))

os.chmod('python8am.pem',0o400)

print("key created and permission changed successfully")