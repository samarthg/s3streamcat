import boto3

class S3Client:
    def __init__(self, bucket, key):
        self.client = boto3.client('s3')
        self.bucket = bucket
        self.key = key

    def get_content_length(self):
        return int(self.client.get_object(Bucket=self.bucket, Key=self.key)['ResponseMetadata']['HTTPHeaders']['content-length'])

    def get_data_with_byte_range(self, start, end):
        return self.client.get_object(Bucket=self.bucket, Key=self.key, Range='bytes={}-{}'.format(start, end))['Body'].read()

    def close_s3_client(self):
        pass