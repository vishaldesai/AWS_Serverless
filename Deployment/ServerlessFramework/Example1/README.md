
# Steps:  

## Create service  
serverless create --template aws-nodejs --path Provisioning  

## Update serverless.yml file  
Sample file attached  

## Deploy  
serverless deploy  
Serverless: Packaging service...  
Serverless: Excluding development dependencies...  
Serverless: Uploading CloudFormation file to S3...  
Serverless: Uploading artifacts...  
Serverless: Uploading service .zip file to S3 (7.29 MB)...  
Serverless: Validating template...  
Serverless: Creating Stack...  
Serverless: Checking Stack create progress...  
...........................................................  
Serverless: Stack create finished...  
Service Information  
service: Provisioning  
stage: dev  
region: us-east-1  
stack: Provisioning-dev  
api keys:  
  None  
endpoints:  
  POST - https://iself86g8i.execute-api.us-east-1.amazonaws.com/dev/dxc/createStack/r1/V1  
  GET - https://iself86g8i.execute-api.us-east-1.amazonaws.com/dev/dxc/describeStack/r1/V1  
functions:  
  createStack: Provisioning-dev-createStack  
  describeStack: Provisioning-dev-describeStack  

