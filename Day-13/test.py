import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='abhay10371-boto3-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2',
    },
)

# response = client.get_bucket_acl(
#     Bucket='abhay10371-boto3-bucket',
# )

# print(response)

# response = client.delete_bucket(
#     Bucket='abhay10371-boto3-bucket',
# )

# print(response)