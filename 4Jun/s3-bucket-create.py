import boto3

AWS_REGION = "us-east-1"

s3 = boto3.resource("s3",region_name=AWS_REGION)

bucket_name = "gaurav-14"

s3.create_bucket(Bucket=bucket_name)

print(f"S3 bucket {bucket_name} create successfully")