# debug_mlflow_s3.py
import boto3
import os
import json

def test_s3_access():
    print("=== MLflow S3 Debug ===")
    print(f"AWS_ACCESS_KEY_ID: {os.environ.get('AWS_ACCESS_KEY_ID')}")
    print(f"AWS_SECRET_ACCESS_KEY: {'*' * len(os.environ.get('AWS_SECRET_ACCESS_KEY', ''))}")
    print(f"MLFLOW_S3_ENDPOINT_URL: {os.environ.get('MLFLOW_S3_ENDPOINT_URL')}")
    
    try:
        s3 = boto3.client(
            's3',
            endpoint_url=os.environ.get('MLFLOW_S3_ENDPOINT_URL'),
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            region_name=os.environ.get('AWS_DEFAULT_REGION', 'us-east-1')
        )
        
        # Test bucket listing
        print("\n1. Testing bucket listing...")
        buckets = s3.list_buckets()
        print(f"Buckets: {[b['Name'] for b in buckets['Buckets']]}")
        
        # Test object listing
        print("\n2. Testing object listing...")
        objects = s3.list_objects_v2(Bucket='mlflow')
        if 'Contents' in objects:
            print(f"Objects: {[obj['Key'] for obj in objects['Contents']]}")
        else:
            print("No objects found")
        
        # Test write permission
        print("\n3. Testing write permission...")
        test_key = "test-trace.json"
        test_content = json.dumps({"test": "data"})
        
        s3.put_object(
            Bucket='mlflow',
            Key=test_key,
            Body=test_content,
            ContentType='application/json'
        )
        print(f"Successfully wrote test object: {test_key}")
        
        # Clean up test object
        s3.delete_object(Bucket='mlflow', Key=test_key)
        print("Test object cleaned up")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_s3_access()