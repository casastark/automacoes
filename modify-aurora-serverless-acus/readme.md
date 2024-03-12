Ajuste Automático de ACUs no Amazon RDS Serverless com AWS Lambda e EventBridge
1. Função Lambda
Primeiramente, garanta que sua função Lambda esteja preparada para receber e utilizar parâmetros.

```python
python
Copy code
import json
import boto3

def lambda_handler(event, context):
    min_acu = event.get('min_acu', 1)  # Obtém o valor min_acu do evento ou usa 1 como padrão
    max_acu = event.get('max_acu', 2)  # Obtém o valor max_acu do evento ou usa 2 como padrão
```

# O resto do código para modificar o RDS...
2. Regras do EventBridge
Crie duas regras do EventBridge:

Para disparar a Lambda às 9h com determinados parâmetros.
Para disparar a Lambda às 18h com outros parâmetros.
Ao configurar cada regra, você pode fornecer um objeto JSON como entrada constante para a função Lambda. Este objeto JSON pode conter os parâmetros min_acu e max_acu que você deseja passar.

Exemplo de entrada constante para a regra das 9h:
```python
json
Copy code
{
  "min_acu": 5,
  "max_acu": 10
}
```
Exemplo de entrada constante para a regra das 18h:
```python
json
Copy code
{
  "min_acu": 1,
  "max_acu": 2
}
```
3. Expressão Cron
Ao configurar a regra do EventBridge, use uma expressão cron para definir o horário. Por exemplo:

Para as 9h: cron(0 9 ? * MON-FRI *)
Para as 18h: cron(0 18 ? * MON-FRI *)
Estas expressões cron irão disparar a função às 9h e às 18h de segunda a sexta-feira, respectivamente.

