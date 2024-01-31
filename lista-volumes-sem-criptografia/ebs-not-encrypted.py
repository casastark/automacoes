import boto3
from openpyxl import Workbook
from openpyxl.styles import Font, Border, Side, Alignment

def obter_nome_do_disco(volume):
    for tag in volume.get('Tags', []):
        if tag['Key'].lower() == 'name':
            return tag['Value']
    return None

def obter_caminho_montado(volume):
    for attachment in volume.get('Attachments', []):
        return attachment.get('Device')
    return None

def obter_volumes_ebs_nao_criptografados(regiao):
    ec2 = boto3.client('ec2', region_name=regiao)
    volumes_nao_criptografados = []

    # Obtém a lista de volumes EBS
    response = ec2.describe_volumes()

    for volume in response['Volumes']:
        # Verifica se o volume não é criptografado
        if 'Encrypted' in volume and not volume['Encrypted']:
            instancias_associadas = [attachment['InstanceId'] for attachment in volume.get('Attachments', [])]
            instancia_associada = instancias_associadas[0] if instancias_associadas else None

            nome_do_disco = obter_nome_do_disco(volume)
            caminho_montado = obter_caminho_montado(volume)

            volumes_nao_criptografados.append({
                'ID do Volume': volume['VolumeId'],
                'Nome do Disco': nome_do_disco,
                'Tamanho (GiB)': volume['Size'],
                'Tipo': volume['VolumeType'],
                'Estado': volume['State'],
                'Instância Associada': instancia_associada,
                'Região': regiao,
                'Caminho Montado': caminho_montado
            })

    return volumes_nao_criptografados

def criar_planilha(volumes_nao_criptografados):
    planilha = Workbook()
    planilha_ativa = planilha.active

    # Adiciona formatação aos títulos (primeira linha)
    cabecalho_fonte = planilha_ativa[1]
    for cell in cabecalho_fonte:
        cell.font = Font(bold=True)  # Texto em negrito
        cell.border = Border(left=Side(style="thin"), right=Side(style="thin"), top=Side(style="thin"), bottom=Side(style="thin"))
        cell.alignment = Alignment(wrap_text=True)

    # Adiciona os dados à planilha
    planilha_ativa.append(['ID do Volume', 'Nome do Disco', 'Tamanho (GiB)', 'Tipo', 'Estado', 'Instância Associada', 'Região', 'Caminho Montado'])

    for volume in volumes_nao_criptografados:
        planilha_ativa.append([
            volume['ID do Volume'],
            volume['Nome do Disco'],
            volume['Tamanho (GiB)'],
            volume['Tipo'],
            volume['Estado'],
            volume['Instância Associada'],
            volume['Região'],
            volume['Caminho Montado']
        ])

    # Ajusta a largura das colunas para melhor visualização
    for coluna in planilha_ativa.columns:
        max_largura = 0
        coluna = [cell for cell in coluna]
        for i, cell in enumerate(coluna, 1):
            try:
                if len(str(cell.value)) > max_largura:
                    max_largura = len(cell.value)
            except:
                pass
        ajuste_largura = (max_largura + 2)
        planilha_ativa.column_dimensions[coluna[0].column_letter].width = ajuste_largura

    return planilha

if __name__ == "__main__":
    regiao = 'sa-east-1'  # Substitua pela região desejada, como 'us-east-1', 'sa-east-1', etc.
    volumes_nao_criptografados = obter_volumes_ebs_nao_criptografados(regiao)

    if volumes_nao_criptografados:
        planilha = criar_planilha(volumes_nao_criptografados)
        planilha.save('volumes_nao_criptografados.xlsx')
        print("Planilha gerada com sucesso: volumes_nao_criptografados.xlsx")
    else:
        print("Nenhum volume EBS não criptografado encontrado.")