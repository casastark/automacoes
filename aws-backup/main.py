import boto3
import os

region = os.getenv('AWS_REGION')

session = boto3.Session(region_name=region)

client = session.client('backup')
sts_client = session.client('sts')

def get_account_id():
    return sts_client.get_caller_identity()["Account"]

def create_backup_plan():
    account_id = get_account_id()
    response = client.create_backup_plan(
        BackupPlan={
            'BackupPlanName': 'backup-production',
            'Rules': [
                {
                    "RuleName": "Diario",
                    "TargetBackupVaultName": "Diario",
                    "ScheduleExpression": "cron(0 2 ? * * *)",
                    "StartWindowMinutes": 480,
                    "CompletionWindowMinutes": 1080,
                    "Lifecycle": {
                        "DeleteAfterDays": 7
                    },
                    "EnableContinuousBackup": True
                },
                {
                    'RuleName': 'weekly-backup',
                    'TargetBackupVaultName': 'backup-cross-account',
                    'ScheduleExpression': 'cron(0 5 ? * 7 *)',
                    'StartWindowMinutes': 480,
                    'CompletionWindowMinutes': 10080,
                    'Lifecycle': {
                        'DeleteAfterDays': 90
                    },
                    'CopyActions': [
                        {
                            'Lifecycle': {
                                'MoveToColdStorageAfterDays': 1,
                                'DeleteAfterDays': 365
                            },
                            'DestinationBackupVaultArn': f'arn:aws:backup:{session.region_name}:{account_id}:backup-vault:backup-cross-account'
                        }
                    ],
                    'EnableContinuousBackup': False
                },
                {
                    'RuleName': 'monthly-backup',
                    'TargetBackupVaultName': 'backup-cross-account',
                    'ScheduleExpression': 'cron(0 5 1 * ? *)',
                    'StartWindowMinutes': 480,
                    'CompletionWindowMinutes': 10080,
                    'Lifecycle': {
                        'DeleteAfterDays': 90
                    },
                    'CopyActions': [
                        {
                            'Lifecycle': {
                                'MoveToColdStorageAfterDays': 1,
                                'DeleteAfterDays': 1825
                            },
                            'DestinationBackupVaultArn': f'arn:aws:backup:{session.region_name}:{account_id}:backup-vault:backup-cross-account'
                        }
                    ],
                    'EnableContinuousBackup': False
                }
            ]
        }
    )
    print(f'Backup Plan created with ID: {response["BackupPlanId"]}')
    return response['BackupPlanId']

def create_backup_selection(backup_plan_id):
    account_id = get_account_id()
    response = client.create_backup_selection(
        BackupPlanId=backup_plan_id,
        BackupSelection={
            'SelectionName': 'production',
            'IamRoleArn': f'arn:aws:iam::{account_id}:role/service-role/AWSBackupDefaultServiceRole',
            'Resources': [
                "arn:aws:dynamodb:*:*:table/*",
                "arn:aws:elasticfilesystem:*:*:file-system/*",
                "arn:*:fsx:*",
                "arn:aws:rds:*:*:cluster:*",
                "arn:aws:rds:*:*:db:*",
                "arn:aws:redshift:*:*:cluster:*"
            ],
            'ListOfTags': [],
            'Conditions': {}
        }
    )
    print(f'Backup Selection created with Selection ID: {response["SelectionId"]}')

backup_plan_id = create_backup_plan()
create_backup_selection(backup_plan_id)