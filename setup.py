from setuptools import setup

# Read the README file properly
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(name='s3streamcat',
      version='0.1.6',
      description='Streaming based unix cat like functionality for file on S3. Supports gzip, bzip and xz compressed files as well',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/samarthg/s3streamcat',
      download_url = 'https://github.com/samarthg/s3streamcat/archive/v0.1.6.tar.gz',
      author='Samarth Gahire',
      author_email='samarth.gahire@gmail.com',
      license='MIT',
      packages=['s3streamcat', 's3client'],
      python_requires='>=3.6',
      install_requires=[
          'boto3>=1.26.0',
      ],
      zip_safe=False,
      entry_points={
          'console_scripts': [
              's3streamcat = s3streamcat.s3streamcat:stream_s3_file'
          ]
      },
      keywords = ['s3cat', 's3', 'print', 'aws', 'cat', 'stream', 'gzip', 'bzip', 'xz'],
      )
