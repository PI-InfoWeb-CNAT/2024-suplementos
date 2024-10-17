# Projeto Comércio Eletrônico - PowerUp

## Especificação do caso de uso - Modelo

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 25/04/2024 | **1.00** | Adição do resumo e ator(es) | Pedro Edi |


### 1. Resumo 
Detalha o processo de como manter um produto (CRUD).
### 2. Atores
- Moderador/administrador

### 3. Pré-condições
**Autenticação como Administrador Válido**: O administrador deve estar autenticado com um login e senha válidos.
**Nome do produto**: Único na tabela do banco de dados , com limite de até 100 caracteres.
**Preço**: Valor numérico positivo, com duas casas decimais, armazenado no formato decimal(10, 2).
**Quantidade em estoque**: Número inteiro (ex: 100 unidades).
**Data de validade**: Data futura, no formato YYYY-MM-DD.
**Imagem válida**: A imagem do produto deve estar no formato correto (JPG, PNG,JPEG). O sistema deve verificar se a imagem é válida antes do upload para o servidor.
**Produto Válido para Operações de Atualização ou Exclusão**:Para editar ou excluir um produto, o sistema deve verificar que o ID do produto existe no banco de dados e que não está associado a pedidos pendentes (em caso de exclusão).


### 4.Pós-condições
**Criação de Produto**:Um novo produto é adicionado ao banco de dados, com todas as informações necessárias (nome, preço, estoque, etc.).
**Atualização de Produto**: O produto é atualizado no banco de dados com as alterações feitas (como preço ou estoque).
**Exclusão de Produto**: O produto é removido do banco de dados, e o sistema confirma a exclusão com uma mensagem (ex: "Produto excluído com sucesso").
**Exibição de Produto**: As informações detalhadas do produto (nome, preço, estoque, etc.) são exibidas corretamente na interface de administração.Se buscado por filtros, o produto é exibido de acordo com os critérios de pesquisa.


### 5. Fluxos de evento
- No fluxo principal, definir o passo a passo de como vai ocorrer o caso de uso da forma padrão.
- No fluxo alternativo, definir o passo a passo de como vai ocorrer o caso de uso em uma forma alternativa. Opcional.
- Exemplo abaixo de um caso de uso "Adicionar ao carrinho".

#### 5.1. Fluxo Principal
##### dentro da página de administração

|  Ator  | Sistema |
|:-------|:------- |
| 1. Administrador faz login no sistema | --- |
| 2. Administrador acessa o módulo de gerenciamento de produtos |  --- |
| 3.  O administrador escolhe entre:
  Criar: Cadastrar um novo produto.
  Ler: Visualizar informações de um produto existente.
  Atualizar: Editar as informações de um produto.
  Deletar: Excluir um produto. | --- |

| --- | 4. O administrador seleciona "Criar Novo Produto". |
| --- | 5. Insere informações obrigatórias como nome, preço, categoria, estoque, descrição, e imagem do produto. |
| 6. O sistema valida as entradas (como formato de preço, imagem, e validade)| --- |
| --- | 7. O administrador confirma a criação. |
| 8. O sistema salva o novo produto no banco de dados e exibe a mensagem "Produto criado com sucesso". | --- |
| 9. O sistema salva as alterações no banco de dados e exibe a mensagem "Produto atualizado com sucesso".| --- |

| --- | 10. Atualização de Produto (fluxo padrão) |
| --- | 11. O administrador seleciona um produto da lista para edição. |
| --- | 12.  Altera as informações necessárias, como preço ou quantidade em estoque. |
| 13. O sistema valida os dados alterados.| --- | 
| --- | 14. O administrador confirma as mudanças.|
| 15. O sistema salva as alterações no banco de dados e exibe a mensagem "Produto atualizado com sucesso".|  --- |

| --- | 16. Exclusão de Produto (fluxo padrão) |
| --- | 17. O administrador seleciona um produto da lista e escolhe a opção "Excluir". |
| 18. O sistema confirma se o produto pode ser excluído (verifica se não está vinculado a pedidos pendentes). | --- | 
| --- | 19.  O administrador confirma a exclusão. |
| 20. O sistema valida os dados alterados.| --- |
| --- | 21. O administrador confirma as mudanças.|
| 22. O sistema salva as alterações no banco de dados e exibe a mensagem "Produto excluído com sucesso".| --- |
| 22. Sistema retorna ao painel de gerenciamento. | --- |


#### 5.2. Fluxo alternativo
##### Erro ao tentar criar/atualizar produto com dados inválidos:

|  Ator  | Sistema |
|:-------|:------- |
| 1. O administrador insere informações incorretas ou incompletas (ex: campo de preço vazio, imagem no formato errado). | --- |
| --- | 2. O sistema detecta o erro e exibe mensagens de alerta indicando quais campos precisam ser corrigidos (ex: "Preço é um campo obrigatório"). |
| --- | 3. O administrador corrige os dados e tenta novamente. |
| 4. Administrador Continua Navegando | --- |

#### 5.3. Fluxo alternativo
##### Erro ao excluir produto vinculado a pedidos:

|  Ator  | Sistema |
|:-------|:------- |
| 1. O administrador tenta excluir um produto que está associado a pedidos em andamento. | --- |
| --- | 2. O sistema bloqueia a exclusão e exibe uma mensagem de erro (ex: "Produto não pode ser excluído pois está vinculado a pedidos pendentes"). |
| 3. O administrador cancela a operação ou tenta excluí-lo novamente após resolver as pendências. | --- |
| 4. Administrador Continua Navegando | --- |

### 6. Dicionário de dados

### 7. Protótipos de UI


