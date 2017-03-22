=============
S3 Stream Cat
=============

S3 Stream Cat powers you to instantly check the content of S3 file.
Especially it supports streaming and printing data from compressed files.

Compression Format Supported
============================

* Gzip

* XZ

* BZIP

You might find it most useful when you don't actually want to download the file 
however want to check the sample data, or to grep for few records matching 
certain search. 
Typical usage often looks like this::

    s3streamcat s3://bucketname/dir/file_path
    s3streamcat s3://bucketname/dir/file_path | more
    s3streamcat s3://bucketname/dir/file_path | grep something

Configurations
==============
If you have aws client installed on your system ``s3streamcat`` will work *out of the box*
If not you will have to have file at location ``HOME/.aws/credentials`` with aws cred::

    [default]
    aws_access_key_id=<put your aws access key>
    aws_secret_access_key=<put your aws secret key>

Dependancies
============

* Its written for Python3 which is the present and future of the language

* ``libssl-dev libffi-dev``

* ``python3-dev``

Ubuntu users can install dependancy packages with:

* ``sudo apt-get install -y libssl-dev libffi-dev``

* ``sudo apt-get install python3-dev``
