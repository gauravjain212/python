import boto3

s3 = boto3.client('s3')

bucket_name = "gaurav-14"

file_name = input("Enter file name to upload: ")
new_name = input("Enter file name when uploaded: ")

s3.upload_file(file_name,bucket_name,new_name)

print(f"{file_name} has been uploaded to {bucket_name}")