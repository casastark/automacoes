# Introdução

## Requisitos

```
boto3

python-docx

python3
```

### O script tem o objetivo de mapear alguns recursos da AWS e então gerar um arquivo docx com as informações levantadas.

### Uso recomendado para levantar informações em ambientes grandes :)

## Como usar?

### Acesse a conta/ambiente que você deseja gerar a documentação com uma role/user que tenha permissões o suficiente para listar os recursos que você deseja buscar.

### Vá para a região que você deseja mapear e então use o seguinte comando no terminal do seu computador:

```
python3 doc.py
```

### O script deve retornar "Informações detalhadas foram adicionadas ao arquivo "informacoes_aws.docx"