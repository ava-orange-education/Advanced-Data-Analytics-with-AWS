import json
import boto3
import urllib.request 

s3 = boto3.client('s3')

def lambda_handler(event, context):
    #url for the Zillow Home Value Index (ZHVI), latest url can be found at https://www.zillow.com/research/data/
    url = 'https://files.zillowstatic.com/research/public_csvs/zhvi/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv?t=1707444908'
    
    response = urllib.request.urlopen(url)
    csv_data = response.read()
    
    bucket_name = 'real-estate-roi-data'
    key_name = 'zhvi.csv'
    
    s3.put_object(Bucket=bucket_name, Key=key_name, Body=csv_data)
    
    #it is customary to return a success/failure message to conclude your 
    return {
        'statusCode': 200,
        'body': 'File downloaded and uploaded to S3 successfully!'
    }
