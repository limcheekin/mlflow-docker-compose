import boto3
import os

print('AWS_ACCESS_KEY_ID:', os.environ.get('AWS_ACCESS_KEY_ID'))
print('AWS_SECRET_ACCESS_KEY:', os.environ.get('AWS_SECRET_ACCESS_KEY'))
print('MLFLOW_S3_ENDPOINT_URL:', os.environ.get('MLFLOW_S3_ENDPOINT_URL'))

try:
    s3 = boto3.client('s3',
                      endpoint_url=os.environ.get('MLFLOW_S3_ENDPOINT_URL'),
                      aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                      aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
    
    response = s3.list_buckets()
    print('Buckets:', [bucket['Name'] for bucket in response['Buckets']])
    
    response = s3.list_objects_v2(Bucket='mlflow')
    if 'Contents' in response:
        print('Objects in mlflow bucket:', [obj['Key'] for obj in response['Contents']])
    else:
        print('mlflow bucket is empty')
        
except Exception as e:
    print('Error connecting to S3:', e)