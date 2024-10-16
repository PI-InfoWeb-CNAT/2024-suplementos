# Projeto Comércio Eletrônico - PowerUp

## Especificação do caso de uso - Cancelar Pedido

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 14/10/2024 | **1.00** | Finalização do detalhamento | Maria Vitória |


### 1. Resumo 
Como usuário identificado, desejo ter a opção de cancelar o pedido e, após isso, ser reembolsado.

### 2. Atores
- Cliente

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
- 	Estar logado, Produto ter sido comprado.

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  Receber reembolso.

### 5. Fluxos de evento

#### 5.1. Fluxo Principal
##### dentro da página de produto

|  Ator  | Sistema |
|:-------|:------- |
| 1. Usuário clica no anúncio do produto | --- |
| --- | 2. Sistema redireciona usuário para página do Produto clicado |
| 3.  Usuário clica no botão para adicionar produto no carrinho | --- |
| --- | 4. Sistema adiciona produto no carrinho do usuário |
| --- | 5. Sistema informa mensagem de que o produto foi adicionado |
| 6. Usuário Continua Navegando | --- |

#### 5.2. Fluxo alternativo
##### fora da página de produto

|  Ator  | Sistema |
|:-------|:------- |
| 1. usuário clica no botão de adicionar produto no carrinho | --- |
| --- | 2. Sistema adicionar/remove produto no carrinho do usuário |
| --- | 3. Sistema informa mensagem de que o produto foi adicionado/removido |
| 4. Usuário Continua Navegando | --- |

#### 5.3. Fluxo alternativo
##### página do carrinho

|  Ator  | Sistema |
|:-------|:------- |
| 1. usuário clica no botão para lista de carrinhos | --- |
| --- | 2. Sistema redireciona usuário para página do carrinho |
| 3. usuário clica no botão do carrinho do produto | --- |
| --- | 2. Sistema remove produto do carrinho |
| --- | 2. Sistema informa remoção da lista do carrinho |
| 4. Usuário Continua Navegando | --- |

### 6. Dicionário de dados

### 7. Protótipos de UI


