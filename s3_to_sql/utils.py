import os
import json
import urllib.parse
import boto3
import datetime
import psycopg2

s3 = boto3.client('s3')

def parse_filename(filename):
    hostname = filename.split("/")[1]
    date_str = filename.split("-")[2]
    date = datetime.datetime.strptime(date_str, "%Y%m%dT%H%M%S")
    return hostname, date


def lambda_handler(parse_func, upload_func, event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')


    HOST = os.environ.get("DB_HOST")
    PORT = os.environ.get("DB_PORT")
    DATABASE= os.environ.get("DB_NANE")
    USER = os.environ.get("DB_USERNAME")
    PASSWORD = os.environ.get("DB_PASSWORD") 

    con = psycopg2.connect(
        host=HOST,
        port=PORT,
        dbname=DATABASE,
        user=USER,
        password=PASSWORD
    )

    try:

        response = s3.get_object(Bucket=bucket, Key=key)
        body = json.loads(response["Body"].read())
        parsed_data = parse_func(key, body)

        upload_func(parsed_data, con)
        
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
