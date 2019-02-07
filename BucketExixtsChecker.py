import boto3
import botocore
s3resource = boto3.resource('s3')

exists = True     
try:
	s3resource.meta.client.head_bucket(Bucket='mybucket')     
except botocore.exceptions.ClientError as e:    # if a client error is thrown, then check the error code
	error_code = e.response['Error']['Code']         
	if error_code == '404':                          
		exists=False                            # if it was a 404 error, then the bucket does not exist
print (exists)
 