import sys
import boto3
from pyspark.sql import SparkSession
from awsglue.utils import getResolvedOptions

# Arguments
args = getResolvedOptions(sys.argv, ['parentFile','childFile','joinCol','s3Bucket','inputLoc','stageLoc','outputLoc','outputFileName','kmsKey'])

parentFile = args['parentFile']
childFile  = args['childFile']
joinCol    = args['joinCol']
s3Bucket   = args['s3Bucket']
inputLoc   = args['inputLoc']
stageLoc   = args['stageLoc']
outputLoc  = args['outputLoc']
outputFileName = args['outputFileName']
kmsKey     = args['kmsKey']


# Create sparksession variable
spark = SparkSession.builder.getOrCreate()

# Create emp and dept dataframe and join them using deptid
parentDF = spark.read.format("csv").option("header", "true").option("mode", "DROPMALFORMED").load(parentFile)
childDF = spark.read.format("csv").option("header", "true").option("mode", "DROPMALFORMED").load(childFile)
joinedDF = parentDF.join(childDF, (joinCol))

# Write csv file to S3 staging area
s3StageLoc =  "s3://" + s3Bucket + "/" + inputLoc + "/" + stageLoc
joinedDF.write.format('com.databricks.spark.csv').save(s3StageLoc)

# Retrieve contents of csv file, encrypt content using kms and write file to a different bucket

client = boto3.resource('s3') 
bucket = client.Bucket(s3Bucket)
for obj in bucket.objects.all():
    if obj.key.endswith(('.csv')):
        stageFileBody = obj.get()['Body'].read()
        stageFileKey  = obj.key


s3outputFileName = outputLoc + "/" + outputFileName

client = boto3.client('s3')

response = client.put_object(
    ACL='private',
    Body=stageFileBody,
    Bucket=s3Bucket,
    Key=s3outputFileName,
    ServerSideEncryption='aws:kms',
    StorageClass='STANDARD',
    SSEKMSKeyId=kmsKey
)


# Remove temporary staging folder/files
s3StageDir = inputLoc + "/" + stageLoc
client = boto3.client('s3')
client.delete_object(Bucket=s3Bucket, Key=stageFileKey)
client.delete_object(Bucket=s3Bucket, Key=s3StageDir)