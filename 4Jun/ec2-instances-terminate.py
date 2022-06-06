import boto3
import sys

ec2 = boto3.resource('ec2')

for id in sys.argv[1:]:
    instance = ec2.Instance(id)
    instance.terminate()
print("Instances Terminated")

#ec2 = input("Enter Instance ID to terminate: ")

#instance = ec2.instance(ec2_instance)
#instance.terminate()
#print("Instances Terminated")
