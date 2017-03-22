from setuptools import setup

setup(name='s3streamcat',
      version='0.1.0',
      description='Streaming based unix cat like functionality for file on S3',
      url='',
      author='Samarth Gahire',
      author_email='samarth.gahire@gmail.com',
      license='',
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
      )
