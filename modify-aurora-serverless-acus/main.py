import boto3
import json

def lambda_handler(event, context):
    rds = boto3.client('rds', region_name='sa-east-1')

    cluster_identifier = 'teste123'
    min_capacity = event.get('min_capacity', 4)
    max_capacity = event.get('max_capacity', 50)

    try:
        print(f"Tentando modificar o cluster: {cluster_identifier}")
        
        response = rds.modify_db_cluster(
            DBClusterIdentifier=cluster_identifier,
            ApplyImmediately=True,
            ServerlessV2ScalingConfiguration={
                'MinCapacity': min_capacity,
                'MaxCapacity': max_capacity
            }

            #############################
            # Para versão V1 do scaling #
            #############################
            # ScalingConfiguration={
            #     'MinCapacity': min_capacity,
            #     'MaxCapacity': max_capacity
            # }
        )
        
        print(f"Cluster modificado com sucesso: {json.dumps(response, default=str)}")
        return {
            'statusCode': 200,
            'body': json.dumps('Cluster modificado com sucesso!')
        }

    except Exception as e:
        print(f"Erro desconhecido: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Erro desconhecido: {e}")
        }