import boto3


class S3Service:

	def __init__(self):
		self.s3 = boto3.client("s3")

	def upload_csv_to_s3(self, csv, s3_key='unstructured-text-1.csv', bucket_name="publicis-progresspoint"):
		self.s3.put_object(Bucket=bucket_name, Key=s3_key, Body=csv)
