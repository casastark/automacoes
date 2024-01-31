# automacoes

Antes de fazer alterações na branch principal (main), por favor, siga as instruções abaixo para garantir um processo de contribuição suave.


## Como Usar

1. Clone este repositório:

    ```bash
    git clone https://github.com/casastark/automacoes.git
    ```

2. Navegue até o diretório da automação desejada:

    ```bash
    cd terraform/automacao1
    ```
    
3. Crie uma branch para suas alterações. Utilize o seguinte padrão de nomenclatura:
   ```bash
   git checkout -b nome-do-colaborador-nome-da-automacao
   por exemplo: git checkout -b joao-automacao-login

   git add .
   
   git commit -m "Mensagem descritiva das alterações"

   git push --set-upstream origin joao-automacao-login

# Contribuição ao Projeto

2. Faça suas alterações na branch recém-criada.

3. Submeta um Pull Request (PR) para a branch principal (main).

4. Seu PR será revisado pelo administrador. Certifique-se de seguir as diretrizes de codificação e documentação.

5. Após a aprovação do administrador, as alterações serão mescladas na branch principal (main).

## Padrões de Nomenclatura

- **Nome do Colaborador:** Utilize seu próprio nome ou um identificador único.
- **Nome da Automação:** Descreva brevemente a natureza da automação que está sendo implementada.
