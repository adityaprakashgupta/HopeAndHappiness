from storages.backends.s3boto3 import S3Boto3Storage

class MediaS3Boto3Storage(S3Boto3Storage):
	location ='media'


class StaticS3Boto3Storage(S3Boto3Storage):
	location ='static'