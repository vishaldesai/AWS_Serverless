import boto3
import sys

client = boto3.client('glue')

response = client.start_job_run(
               JobName = 'glue_tranform',
               Arguments = {
                 '--parentFile'     : 's3://vishaldxc/glueinput/orders.txt',
                 '--childFile'      : 's3://vishaldxc/glueinput/order_items.txt',
                 '--joinCol'        : 'order_id',
                 '--s3Bucket'       : 'vishaldxc' ,
                 '--inputLoc'       : 'glueinput',
                 '--stageLoc'       : 'transform10',
                 '--outputLoc'      : 'glueoutput',
                 '--outputFileName' : 'transformfile1.txt',
                 '--kmsKey'         : '5998040d-2926-4ab4-82a3-ca59b49f4d18'
                 } )