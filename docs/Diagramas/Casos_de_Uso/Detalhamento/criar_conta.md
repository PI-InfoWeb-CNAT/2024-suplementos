# Projeto Comercio Eletrônico - PowerUp

## Especificação do caso de uso - Criar conta

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 30/04/2024 | **1.00** | Adição da seção de resumo e atores | Lucas Brito |


### 1. Resumo 
Como usuário não identificado, desejo ter a opção de criar uma conta.

### 2. Atores
- Visitante (usuário não cadastrado)

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
- 	Possuir um email existente para criação da conta

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  Permitir navegação e usar os serviços de compra do site

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


