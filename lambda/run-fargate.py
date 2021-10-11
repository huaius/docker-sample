# This lambda will migrate the db to the PROD account and do the whitelist
# First set the TABLE_NAME with the real table name created by cfn stack

STAGE='DEV'
TABLE_NAME='name'

REGION='us-east-1'
SUBNET='subnet-00'

import boto3
def lambda_handler(event, context):
    stage = event.get("region") if event.get("region") else STAGE
    print("Update table for region " + stage)
    client = boto3.client('ecs')
    response = client.run_task(
    cluster='fargate-db-migration-cluster', # name of the cluster
    launchType = 'FARGATE',
    taskDefinition='db-migration:4', # replace with your task definition name and revision
    count = 1,
    platformVersion='LATEST',
    overrides={
          'containerOverrides': [
              {
                  'name': 'db-migration-container',
                  'environment': [
                      {
                          'name': 'STAGE',
                          'value': stage
                      },
                      {
                          'name': 'TABLE_NAME',
                          'value': TABLE_NAME
                      },
                      {
                          'name': 'REGION',
                          'value': REGION
                      }
                  ]
              }
          ],
          'taskRoleArn': 'arn:aws:iam::00000000000:role/ecs_db_migration'
      },
    networkConfiguration={
          'awsvpcConfiguration': {
              'subnets': [
                  SUBNET # replace with your public subnet or a private with NAT
              ],
              'assignPublicIp': 'ENABLED'
          }
      })
    return str(response)

