import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_FILE_OVERWRITE = False
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")
STORAGES = {"default": {"BACKEND": "HoapAndHappiness.aws.backends.MediaS3Boto3Storage"}, "staticfiles": {"BACKEND": "HoapAndHappiness.aws.backends.StaticS3Boto3Storage"}}
# AWS_S3_ADDRESSING_STYLE = "path"
# AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_QUERYSTRING_AUTH = False