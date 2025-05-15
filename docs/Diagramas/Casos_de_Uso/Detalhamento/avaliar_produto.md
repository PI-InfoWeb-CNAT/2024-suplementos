# Projeto Comércio Eletrônico - PowerUp

## Especificação do caso de uso - Avaliar Produto

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 14/10/2024 | **1.00** | Finalização do detalhamento | Maria Vitória |

### 1. Resumo 
Como um usuário identificado, desejo avaliar um produto que já comprei.

### 2. Atores
- Cliente

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
- 	O usuário deve possuir conta no site.
-   O usuário deve estar logado no site.
-   O usuário deve ter comprado o produto que ele irá avaliar.
-   O status do pedido deve ser "Recebido".

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  Cadastre a avaliação feita pelo usuário no sistema.
-  Exiba na página do produto avaliado o número de avaliações e a quantidade de estrelas delas, incluindo a avaliação feita pelo usuário.

### 5. Fluxos de evento

#### 5.1. Fluxo Principal
##### dentro da página de produto

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica em "Meus Pedidos" | --- |
| 2. Escolhe um pedido e clica em "Detalhes do Pedido" | --- |
| --- | 3. Exibe um modal com os produtos do pedido |
| 4.  Clica em "Avaliar Produto" | --- |
| --- | 5. Exibe um modal com os campos necessários para a avaliação |
| 6. Preenche os campos e clica em "Avaliar" | --- |
| --- | 7. Exibe mensagem de sucesso |
| 8. Continua navegando | --- |


#### 5.2. Fluxo alternativo
##### Avaliação Incompleta

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão para avaliar | --- |
| --- | 2. Verifica se todos os campos obrigatórios foram preenchidos|
| --- | 3. Informa ao usuário que alguns campos obrigatórios estão vazios. |
| 4. Preenche os campos faltantes e tenta enviar a avaliação novamente. | --- |
| 5. Continua Navegando | --- |

### 6. Dicionário de dados

### 7. Protótipos de UI


