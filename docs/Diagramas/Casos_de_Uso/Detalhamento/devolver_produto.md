# Projeto Comércio Eletrônico - PowerUp

## Especificação do caso de uso - Devolver produto

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 21/10/2024 | **1.00** | Cliente solicita a devolução de um item | Maria Vitória |


### 1. Resumo 
Como usuário identificado, desejo poder solicitar a devolução de um produto que veio com defeito.

### 2. Atores
- Cliente

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
- 	O usuário deve possuir conta no site.
-   O usuário deve estar logado no site.
-   O usuário deve ter comprado o produto que ele irá solicitar a devolução.
-   O status do pedido deve ser "Recebido".

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  O cliente é informado sobre o status da devolução, por meio de uma notificação, e, se for aprovada, o produto será devolvido.

### 5. Fluxos de evento

#### 5.1. Fluxo Principal

|  Ator  | Sistema |
|:-------|:------- |
| 1. Acessa a página de "Meus Pedidos" | --- |
| 2. Escolhe o pedido no qual o produto que ela quer devolver está, e clica em "Detalhes do Pedido" | --- |
| --- | 3. Exibe um modal com os produtos do pedido |
| 4.  Clica em "Devolver produto" | --- |
| --- | 5. Exibe um modal com os campos necessários para a devolução |
| 6. Preenche os campos e clica em "Enviar" | --- |
| --- | 7. Exibe mensagem de sucesso |
| --- | 8. Emite uma notificação para o cliente, dizendo que o status da solicitação está em "em análise" |
| 9. Continua navegando | --- |

### 6. Dicionário de dados

### 7. Protótipos de UI