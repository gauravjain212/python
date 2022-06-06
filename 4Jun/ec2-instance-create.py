import boto3

ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
    ImageId='ami-0756a1c858554433e',
    InstanceType='t2.micro',
    KeyName='python8am',
    MinCount=1,
    MaxCount=1
)

print("EC2 Instaance create successfully.")