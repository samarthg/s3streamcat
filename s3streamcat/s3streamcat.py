import argparse
import zlib
import bz2
import lzma
import sys
from s3client import S3Client

def get_compressed_data_from_s3_file_in_ranges(s3, data_type):
    d = zlib.decompressobj(16+zlib.MAX_WBITS)
    zd = bz2.BZ2Decompressor()
    lzmad = lzma.LZMADecompressor()
    start = 0
    end = 1023

    content_length = s3.get_content_length()
    if content_length < 1024:
        end = content_length-1
    body = s3.get_data_with_byte_range(start, end)

    while True:
        if data_type=='text':
            yield body.decode('utf-8')
        if data_type=='gz':
            yield (d.decompress(body)).decode('utf-8')
        if data_type=='bz':
            yield (zd.decompress(body)).decode('utf-8')
        if data_type=='xz':
            yield (lzmad.decompress(body)).decode('utf-8')
        if data_type=='tar':
            print('This compression format is currently not supported.')
        if data_type=='zip':
            print('This compression format is currently not supported.')

        remaining_content_length = content_length - (end+1)
        if remaining_content_length <=0:
            return
        if remaining_content_length <1024:
            start = end + 1
            end = start + remaining_content_length -1
        else:
            start = end + 1
            end = start + 1023

        body = s3.get_data_with_byte_range(start, end)

def stream_s3_file():
    data_type = 'text'

    parser = argparse.ArgumentParser()
    parser.add_argument("s3_file_path",
                        help="S3 file path in the format like 's3://bucketname/dir/file_path'",
                        type=str)
    args = parser.parse_args()

    file_url = args.s3_file_path
    path_data = file_url.split('/', 3)
    if len(path_data)!=4:
        print("\nS3 path provided seems to be incorrect. Please check.\n")
        sys.exit(1)
    bucket = path_data[2]
    file_key = path_data[3]

    if not file_key or file_key[-1]=='/':
        print("\nS3 Directory is not supported, please provide file path.\n")
        sys.exit(1)

    if ".gz" in file_key:
        data_type = 'gz'
    if ".bz" in file_key:
        data_type = 'bz'
    if ".xz" in file_key:
        data_type = 'xz'
    s3 = S3Client(bucket, file_key)
    try:
        last_line = ''
        for data in get_compressed_data_from_s3_file_in_ranges(s3, data_type):
            data=last_line + data
            lines = data.split('\n')
            last_line = lines[-1]

            for line in lines[:-1]:
                print(line)
        if last_line:
            print(last_line)
    except KeyboardInterrupt:
        sys.exit(0)
    except BrokenPipeError:
        sys.exit(0)
        #TODO close s3 stream in both these cases.
        #TODO: Testing for other compression format
        #TODO: Classes and object
        #TODO: Check if the last line is being handled or not
