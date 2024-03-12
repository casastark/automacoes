import boto3


def add_tags_to_rds(resource_arn):
    rds_client = boto3.client('rds')

    try:
        response = rds_client.add_tags_to_resource(
            ResourceName=resource_arn,
            Tags=[
                {'Key': 'backup', 'Value': 'yes'},
                {'Key': 'recursobkp', 'Value': 'rds'}
            ]
        )
        print(f"As tags foram aplicadas com sucesso no recurso {resource_arn}.")
    except Exception as e:
        print(f"Erro ao aplicar as tags no recurso {resource_arn}: {str(e)}")


def add_tags_to_ec2(resource_id):
    ec2_client = boto3.client('ec2')

    try:
        ec2_client.create_tags(
            Resources=[resource_id],
            Tags=[
                {'Key': 'backup', 'Value': 'yes'},
                {'Key': 'recursobkp', 'Value': 'ec2'}
            ]
        )
        print(f"As tags foram aplicadas com sucesso no recurso {resource_id}.")
    except Exception as e:
        print(f"Erro ao aplicar as tags no recurso {resource_id}: {str(e)}")


def add_tags_to_dynamodb(resource_arn):
    dynamodb_client = boto3.client('dynamodb')

    try:
        response = dynamodb_client.tag_resource(
            ResourceArn=resource_arn,
            Tags=[
                {'Key': 'backup', 'Value': 'yes'},
                {'Key': 'recursobkp', 'Value': 'dynamodb'}
            ]
        )
        print(f"As tags foram aplicadas com sucesso no recurso {resource_arn}.")
    except Exception as e:
        print(f"Erro ao aplicar as tags no recurso {resource_arn}: {str(e)}")


def add_tags_to_aurora(resource_arn):
    rds_client = boto3.client('rds')

    try:
        response = rds_client.add_tags_to_resource(
            ResourceName=resource_arn,
            Tags=[
                {'Key': 'backup', 'Value': 'yes'},
                {'Key': 'recursobkp', 'Value': 'aurora'}
            ]
        )
        print(f"As tags foram aplicadas com sucesso no recurso {resource_arn}.")
    except Exception as e:
        print(f"Erro ao aplicar as tags no recurso {resource_arn}: {str(e)}")


def add_tags_to_ebs(resource_id):
    ec2_client = boto3.client('ec2')

    try:
        response = ec2_client.create_tags(
            Resources=[resource_id],
            Tags=[
                {'Key': 'backup', 'Value': 'yes'},
                {'Key': 'recursobkp', 'Value': 'ebs'}
            ]
        )
        print(f"As tags foram aplicadas com sucesso no recurso {resource_id}.")
    except Exception as e:
        print(f"Erro ao aplicar as tags no recurso {resource_id}: {str(e)}")


def add_tags_to_efs(resource_id):
    efs_client = boto3.client('efs')

    try:
        response = efs_client.create_tags(
            FileSystemId=resource_id,
            Tags=[
                {'Key': 'backup', 'Value': 'yes'},
                {'Key': 'recursobkp', 'Value': 'efs'}
            ]
        )
        print(f"As tags foram aplicadas com sucesso no recurso {resource_id}.")
    except Exception as e:
        print(f"Erro ao aplicar as tags no recurso {resource_id}: {str(e)}")


def add_tags_to_storage_gateway(resource_arn):
    storage_gateway_client = boto3.client('storagegateway')

    try:
        response = storage_gateway_client.add_tags_to_resource(
            ResourceARN=resource_arn,
            Tags=[
                {'Key': 'backup', 'Value': 'yes'},
                {'Key': 'recursobkp', 'Value': 'storage_gateway'}
            ]
        )
        print(f"As tags foram aplicadas com sucesso no recurso {resource_arn}.")
    except Exception as e:
        print(f"Erro ao aplicar as tags no recurso {resource_arn}: {str(e)}")


def add_tags_to_s3(bucket_name):
    s3_client = boto3.client('s3')

    try:
        response = s3_client.put_bucket_tagging(
            Bucket=bucket_name,
            Tagging={
                'TagSet': [
                    {'Key': 'backup', 'Value': 'yes'},
                    {'Key': 'recursobkp', 'Value': 's3'}
                ]
            }
        )
        print(f"As tags foram aplicadas com sucesso no recurso {bucket_name}.")
    except Exception as e:
        print(f"Erro ao aplicar as tags no recurso {bucket_name}: {str(e)}")

def add_tags_to_documentdb(resource_id):
    documentdb_client = boto3.client('docdb')

    try:
        response = documentdb_client.add_tags_to_resource(
            ResourceName=resource_id,
            Tags=[
                {'Key': 'backup', 'Value': 'yes'},
                {'Key': 'recursobkp', 'Value': 'documentdb'}
            ]
        )
        print(f"As tags foram aplicadas com sucesso no recurso {resource_id}.")
    except Exception as e:
        print(f"Erro ao aplicar as tags no recurso {resource_id}: {str(e)}")

def add_tags_to_neptune(resource_arn):
    neptune_client = boto3.client('neptune')

    try:
        response = neptune_client.add_tags_to_resource(
            ResourceName=resource_arn,
            Tags=[
                {'Key': 'backup', 'Value': 'yes'},
                {'Key': 'recursobkp', 'Value': 'neptune'}
            ]
        )
        print(f"As tags foram aplicadas com sucesso no recurso {resource_arn}.")
    except Exception as e:
        print(f"Erro ao aplicar as tags no recurso {resource_arn}: {str(e)}")


def add_tags_to_fsx(resource_id):
    fsx_client = boto3.client('fsx')

    try:
        response = fsx_client.tag_resource(
            ResourceARN=resource_id,
            Tags=[
                {'Key': 'backup', 'Value': 'yes'},
                {'Key': 'recursobkp', 'Value': 'fsx'}
            ]
        )
        print(f"As tags foram aplicadas com sucesso no recurso {resource_id}.")
    except Exception as e:
        print(f"Erro ao aplicar as tags no recurso {resource_id}: {str(e)}")

def add_tags_to_cloudformation(tags):
    cloudformation_client = boto3.client('cloudformation')

    stack_info = cloudformation_client.describe_stacks()
    tags=[{'Key': 'backup', 'Value': 'yes'}, {'Key': 'recursobkp', 'Value': 'cloudformation'}]

    if 'Stacks' in stack_info:
        stacks = stack_info['Stacks']

        for stack in stacks:
            stack_name = stack['StackName']
            stack_status = stack['StackStatus']

            if stack_status == 'CREATE_COMPLETE':
                cloudformation_client.update_stack(
                    StackName=stack_name,
                    UsePreviousTemplate=True,
                    Capabilities=['CAPABILITY_NAMED_IAM'],
                    Tags=tags
                )

                print(f"Tags adicionadas à stack {stack_name} com sucesso!")
            else:
                print(f"A stack {stack_name} não está no estado CREATE_COMPLETE e não serão aplicadas as tags.")
    else:
        print("Nenhuma stack encontrada.")


def check_and_apply_tags(resource_type, resource_id, engine=None):
    if resource_type == 'rds':
        if engine and 'aurora' in engine.lower():
            add_tags_to_aurora(resource_id)
        elif engine and 'docdb' in engine.lower():
            add_tags_to_documentdb(resource_id)
        elif engine and 'neptune' in engine.lower():
            add_tags_to_neptune(resource_id)
        else:
            add_tags_to_rds(resource_id)
    elif resource_type == 'ec2':
        add_tags_to_ec2(resource_id)
    elif resource_type == 'dynamodb':
        add_tags_to_dynamodb(resource_id)
    elif resource_type == 'aurora':
        if engine and 'docdb' in engine.lower():
            add_tags_to_documentdb(resource_id)
        elif engine and 'neptune' in engine.lower():
            add_tags_to_neptune(resource_id)
        else:
            add_tags_to_aurora(resource_id)
    elif resource_type == 'ebs':
        add_tags_to_ebs(resource_id)
    elif resource_type == 'efs':
        add_tags_to_efs(resource_id)
    elif resource_type == 'storage_gateway':
        add_tags_to_storage_gateway(resource_id)
    elif resource_type == 's3':
        add_tags_to_s3(resource_id)
    elif resource_type == 'fsx':
        add_tags_to_fsx(resource_id)
    elif resource_type == 'cloudformation':
        add_tags_to_cloudformation(resource_id)
    elif resource_type == 'documentdb':
        add_tags_to_documentdb(resource_id)
    else:
        print(f"Tipo de recurso desconhecido: {resource_type}. Nenhuma ação de tag foi executada.")


def analyze_aws_accounts(account_ids):
    for account_id in account_ids:
        session = boto3.Session(region_name='us-east-1')

        rds_client = session.client('rds')
        rds_response = rds_client.describe_db_instances()

        for db_instance in rds_response['DBInstances']:
            engine = db_instance.get('Engine')
            check_and_apply_tags('rds', db_instance['DBInstanceArn'], engine=engine)

        ec2_client = session.client('ec2')
        ec2_response = ec2_client.describe_instances()

        for reservation in ec2_response['Reservations']:
            for instance in reservation['Instances']:
                check_and_apply_tags('ec2', instance['InstanceId'])

        dynamodb_client = session.client('dynamodb')
        dynamodb_response = dynamodb_client.list_tables()

        for table_name in dynamodb_response['TableNames']:
            check_and_apply_tags('dynamodb', table_name)

        rds_response = rds_client.describe_db_clusters()

        for db_cluster in rds_response['DBClusters']:
            engine = db_cluster.get('Engine')
            check_and_apply_tags('aurora', db_cluster['DBClusterArn'], engine=engine)

        ec2_response = ec2_client.describe_volumes()

        for volume in ec2_response['Volumes']:
            check_and_apply_tags('ebs', volume['VolumeId'])

        efs_client = session.client('efs')
        efs_response = efs_client.describe_file_systems()

        for filesystem in efs_response['FileSystems']:
            check_and_apply_tags('efs', filesystem['FileSystemId'])

        storage_gateway_client = session.client('storagegateway')
        storage_gateway_response = storage_gateway_client.list_gateways()

        for gateway in storage_gateway_response['Gateways']:
            check_and_apply_tags('storage_gateway', gateway['GatewayARN'])

        s3_client = session.client('s3')
        s3_response = s3_client.list_buckets()

        for bucket in s3_response['Buckets']:
            check_and_apply_tags('s3', bucket['Name'])

        fsx_client = session.client('fsx')
        fsx_response = fsx_client.describe_file_systems()

        for filesystem in fsx_response['FileSystems']:
            check_and_apply_tags('fsx', filesystem['FileSystemId'])

        cloudformation_client = session.client('cloudformation')
        cloudformation_response = cloudformation_client.describe_stacks()

        for stack in cloudformation_response['Stacks']:
            check_and_apply_tags('cloudformation', stack['StackId'])


account_ids = ['123456789']
analyze_aws_accounts(account_ids)
