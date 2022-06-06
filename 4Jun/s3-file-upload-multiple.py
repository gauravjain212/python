import boto3
import os

s3 = boto3.client("s3")

bucket_name = "gaurav-14"

files_path = input("Enter directory which contains files to upload: ")

files_list = os.listdir(files_path)

for file_name in files_list:
    if os.path.isfile(file_name):
        s3.upload_file(file_name,bucket_name,file_name)
        print(f"{file_name} ---> {bucket_name}")