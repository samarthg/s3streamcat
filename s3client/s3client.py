import boto3
import botocore
import sys
import os

class S3Client:
    def __init__(self, bucket, key):
        self.client = boto3.client('s3')
        self.bucket = bucket
        self.key = key

    def get_content_length(self):
        try:
            return int(self.client.get_object(Bucket=self.bucket, Key=self.key)['ResponseMetadata']['HTTPHeaders']['content-length'])
        except botocore.exceptions.NoCredentialsError:
            print("""\nAWS credentials not found, please ensure that the credentials are available at "%s" file
                  content should look something like
                  [default]
                  aws_access_key_id=<put your aws access key>
                  aws_secret_access_key=<put your aws secret key>\n""" % (os.path.join(os.getenv("HOME"), ".aws", "credentials")))
            sys.exit(1)
        except botocore.exceptions.ParamValidationError:
            print("\nCurrently only S3 file is supported and not directory. Please provide complete path of the intended file.\n")
            sys.exit(1)
        except botocore.exceptions.ClientError:
            print("""\nGiven file does not exists or not a file.
            Currently only S3 file is supported and not directory. Please provide complete path of the intended file.\n""")
            sys.exit(1)

    def get_data_with_byte_range(self, start, end):
        return self.client.get_object(Bucket=self.bucket, Key=self.key, Range='bytes={}-{}'.format(start, end))['Body'].read()

    def close_s3_client(self):
        pass