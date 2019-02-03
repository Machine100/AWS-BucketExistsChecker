for word in words:
	#bucket = s3.Bucket(word)     
	exists = true     
	try:
		s3.meta.client.head_bucket('name')     

	except botocore.exceptions.ClientError as e:         
		# if a client error is thrown, then check that it was a 404 error
		# if it was a 404 error, then the bucket does not exist
		error_code = e.response['Error']['Code']         
		if error_code == '404':
			exists=false