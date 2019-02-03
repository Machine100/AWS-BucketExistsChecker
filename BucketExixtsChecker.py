import boto3
import botocore
s3resource = boto3.resource('s3')

bucket = s3resource.Bucket('word')   #What does this do? Creates a Bucket Resource. Sub-resources are methods that create 
                                     #a new instance of a child resource. This resource's identifiers get passed along to the child.  
exists = True     
try:
	s3resource.meta.client.head_bucket(Bucket='mybucket')     
except botocore.exceptions.ClientError as e:         
		# if a client error is thrown, then check that it was a 404 error
		# if it was a 404 error, then the bucket does not exist
	error_code = e.response['Error']['Code']         
	if error_code == '404':
		exists=False