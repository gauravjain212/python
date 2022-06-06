import boto3

old_bucket_name = "gaurav-14"
new_bucket_name = "gaurav-15"

s3_resource = boto3.resource('s3')

def copy_objects(old_bucket_name,new_bucket_name,old_object_name,new_object_name):
    old_s3_object = s3_resource.Object(old_bucket_name,old_object_name)
    new_s3_object = s3_resource.Object(new_bucket_name,new_object_name)

    new_s3_object.copy_from(CopySource=f'{old_bucket_name}/{old_object_name}')

    print(f"Copied: {old_bucket_name}/{old_object_name} --> {new_bucket_name}/{new_object_name}")

copy_objects(old_bucket_name,new_bucket_name,'test1.txt','test2.txt')
