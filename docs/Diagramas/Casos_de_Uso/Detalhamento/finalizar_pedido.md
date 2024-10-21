
# Projeto Comercio Eletrônico - PowerUp

## Especificação do caso de uso - Finalizar Pedido

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 15/05/2024 | **1.00** | Adicionar seção de resumo e atores | Pedro Edi |


### 1. Resumo 
Detalha o processo de como finalizar a compra dos itens do carrinho.

### 2. Atores
- Cliente

### 3. Pré-condições
**Autenticação**:O usuário deve estar logado em sua conta.
**Produto**:O produto que o usuário deseja comprar deve estar disponível no estoque.O produto deve estar corretamente registrado no sistema, com informações como descrição, preço e promoções.
**Informações de Pagamento:**:O usuário deve ter um método de pagamento válido associado à sua conta (cartão de crédito, PayPal, etc.).
**Endereço de Entrega:**:O usuário deve ter um endereço de entrega válido cadastrado em sua conta.

### 4.Pós-condições

**Registro do Pedido**: Os detalhes do pedido são registrados no banco de dados, incluindo:Informações do usuário (nome, e-mail, endereço de entrega),Itens comprados (nome, quantidade, preço),Método de pagamento utilizado,Status do pedido (ex: processando, enviado, concluído)
**Disponibilidade para Acompanhamento**:O usuário pode acessar sua conta para visualizar o histórico de pedidos e o status do pedido atual.

### 5. Fluxos de evento
- No fluxo principal, definir o passo a passo de como vai ocorrer o caso de uso da forma padrão.
- No fluxo alternativo, definir o passo a passo de como vai ocorrer o caso de uso em uma forma alternativa. Opcional.
- Exemplo abaixo de um caso de uso "Adicionar ao carrinho".

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
