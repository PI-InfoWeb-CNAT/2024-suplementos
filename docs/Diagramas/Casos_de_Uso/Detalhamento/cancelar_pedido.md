# Projeto Comércio Eletrônico - PowerUp

## Especificação do caso de uso - Cancelar Pedido

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 14/10/2024 | **1.00** | Finalização do detalhamento | Maria Vitória |


### 1. Resumo 
Como usuário identificado, desejo ter a opção de cancelar o pedido.

### 2. Atores
- Cliente

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
- 	O usuário deve possuir conta no site.
-   O usuário deve estar logado no site.
-   O usuário deve ter realizado um pedido.
-   O status do pedido estar em "Processando".

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  Cancele o pedido que o usuário cancelar.

### 5. Fluxos de evento

#### 5.1. Fluxo Principal
##### dentro da página de produto

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica em "Meus Pedidos" | --- |
| 2. Escolhe um pedido e clica em "Cancelar pedido" | --- |
| --- | 3. Exibe um modal alertando que o cancelamento é permanente |
| --- | 4. Exibe mensagem de sucesso e recarrega a página, agora sem o pedido cancelado |
| 5. Continua navegando | --- |

### 6. Dicionário de dados

### 7. Protótipos de UI