
# Projeto Comercio Eletrônico - PowerUp

## Especificação do caso de uso - Finalizar Pedido

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 15/05/2024 | **1.00** | Adição da seção de resumo e atores | Pedro Edi |
| 14/10/2024 | **2.00** | Finalização do detalhamento | Pedro Edi |


### 1. Resumo 
Detalha o processo de como finalizar a compra dos itens do carrinho.

### 2. Atores
- Cliente

### 3. Pré-condições
- **Autenticação**:O usuário deve estar logado em sua conta.
- **Produto**:O produto que o usuário deseja comprar deve estar disponível no estoque.O produto deve estar corretamente registrado no sistema, com informações como descrição, preço e promoções.
- **Informações de Pagamento:**:O usuário deve ter um método de pagamento válido associado à sua conta (cartão de crédito, PayPal, etc.).
- **Endereço de Entrega:**:O usuário deve ter um endereço de entrega válido cadastrado em sua conta.

### 4. Pós-condições
- **Registro do Pedido**: Os detalhes do pedido são registrados no banco de dados, incluindo:Informações do usuário (nome, e-mail, endereço de entrega),Itens comprados (nome, quantidade, preço),Método de pagamento utilizado,Status do pedido (ex: processando, enviado, concluído)
- **Disponibilidade para Acompanhamento**:O usuário pode acessar sua conta para visualizar o histórico de pedidos e o status do pedido atual.

### 5. Fluxos de evento
- No fluxo principal, definir o passo a passo de como vai ocorrer o caso de uso da forma padrão.
- No fluxo alternativo, definir o passo a passo de como vai ocorrer o caso de uso em uma forma alternativa. Opcional.
- Exemplo abaixo de um caso de uso "Adicionar ao carrinho".

#### 5.1. Fluxo Principal
##### dentro da página de produto

|  Ator  | Sistema |
|:-------|:------- |
| 1. Adição ao Carrinho | --- |
| --- | 2. O sistema confirma que o produto foi adicionado |
| 3.  O usuário fornece ou confirma o endereço de entrega | --- 
| --- | 4. Sistema valida os dados |
| 5. O usuário seleciona o método de pagamento desejado (cartão de crédito, PayPal, etc.) e insere as informações necessárias | --- |
| --- | 6. Sistema valida os dados |
| 7. O usuário clica em "Confirmar Pedido".| --- |
| --- | 8. O sistema exibe uma página de confirmação do pedido, incluindo o número de referência e um resumo do que foi comprado |
| 9. Usuário continua navegando no site | --- |


#### 5.2. Fluxo alternativo
##### Cenário 1: Usuário Não Está Logado

|  Ator  | Sistema |
|:-------|:------- |
| 1. Adição ao Carrinho | --- |
| --- | 2. O sistema confirma que o produto foi adicionado |
| 3.  O usuário fornece ou confirma o endereço de entrega | --- |
| --- | 4. Sistema valida os dados |
| 5. O usuário seleciona o método de pagamento desejado (cartão de crédito, PayPal, etc.) e insere as informações necessárias | --- |
| --- | 6. Sistema valida os dados |
| 7. O usuário clica em "Confirmar Pedido".| --- |
| --- | 8. O usuário é redirecionado para a página de login |
| 9. Usuário Continua Navegando | --- |

#### 5.3. Fluxo alternativo
##### Cenário 2: Produto Indisponível


|  Ator  | Sistema |
|:-------|:------- |
| 1. Adição ao Carrinho | --- |
| --- | 2. Se o produto estiver fora de estoque, o sistema exibe uma mensagem informando que o item não está disponível |
| --- | 3. Sistema valida os dados |
| --- | 4. O sistema pode sugerir produtos similares ou oferecer a opção de ser notificado quando o item voltar ao estoque |
| 5. Usuário Continua Navegando | --- |

#### 5.3. Fluxo alternativo
##### Cenário 3: Falha no Pagamento

|  Ator  | Sistema |
|:-------|:------- |
| 1. Adição ao Carrinho | --- |
| --- | 2. O sistema confirma que o produto foi adicionado |
| 3.  O usuário fornece ou confirma o endereço de entrega | --- |
| --- | 4. Sistema valida os dados |
| 5. O usuário seleciona o método de pagamento desejado (cartão de crédito, PayPal, etc.) e insere as informações necessárias | --- |
| --- | 5. O sistema exibe uma mensagem de erro |
| 6. O usuário pode tentar um método de pagamento diferente ou corrigir as informações inseridas | --- |
| 7. Usuário Continua Navegando | --- |




### 6. Dicionário de dados

### 7. Protótipos de UI
