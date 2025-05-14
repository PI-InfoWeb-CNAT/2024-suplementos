# Projeto Comercio Eletrônico - PowerUp

## Especificação do caso de uso - Adicionar ao carrinho

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 30/04/2024 | **1.00** | Adição do resumo e atores | Pedro Edi |
| 14/10/2024 | **2.00** | Finalização do detalhamento | Maria Vitória |


### 1. Resumo 
Detalha o processo de como adicionar um produto ao carrinho para a efetuação da compra.

### 2. Atores
- Visitante 
- Cliente

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
- Existir algum produto registrado.

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  Exibe produto no carrinho.

### 5. Fluxos de evento

#### 5.1. Fluxo Principal
##### dentro da página de produto

|  Ator  | Sistema |
|:-------|:------- |
| 1. Usuário clica no anúncio do produto | --- |
| --- | 2. Sistema redireciona usuário para página do Produto clicado |
| 3.  Usuário clica no botão para adicionar produto no carrinho | --- |
| --- | 4. Sistema verifica a disponibilidade do produto.|
| --- | 5. Sistema adiciona produto no carrinho do usuário |
| --- | 6. Sistema informa mensagem de que o produto foi adicionado |
| 6. Usuário Continua Navegando | --- |

#### 5.2. Fluxo alternativo
##### Produto Indisponível

|  Ator  | Sistema |
|:-------|:------- |
| 1. Usuário clica no botão de adicionar produto no carrinho | --- |
| --- | 2. Sistema verifica a disponibilidade do produto. |
| --- | 3. Sistema informa ao usuário que o produto está indisponível. | --- |
| 4. Usuário Continua Navegando | --- |


### 6. Dicionário de dados

### 7. Protótipos de UI
