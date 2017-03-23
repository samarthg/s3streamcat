from setuptools import setup

setup(name='s3streamcat',
      version='0.1.4',
      description='Streaming based unix cat like functionality for file on S3. Supports gzip, bzip and xz compressed files as well',
      long_description=open('README.md').read(),
      url='https://github.com/samarthg/s3streamcat',
      download_url = 'https://github.com/samarthg/s3streamcat/archive/0.1.4.tar.gz',
      author='Samarth Gahire',
      author_email='samarth.gahire@gmail.com',
      license='MIT',
      packages=['s3streamcat', 's3client'],
      install_requires=[
          'boto3==1.3.1',
      ],
      zip_safe=False,
      entry_points={
          'console_scripts': [
              's3streamcat = s3streamcat.s3streamcat:stream_s3_file'
          ]
      },
      keywords = ['s3', 'print', 'aws', 'cat', 'stream', 'gzip', 'bzip', 'xz'],
      )
