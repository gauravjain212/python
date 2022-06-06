import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
    print(f"Instance ID: {instance.id}")
    print(f"\tInstance AMI: {instance.image_id}")
    print(f"\tInstance Public IPv4: {instance.public_ip_address}")
    print(f"\tCurrent State: {instance.state['Name']}")
    print("-----------------")

