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
-  Exiba o produto no carrinho.

### 5. Fluxos de evento

#### 5.1. Fluxo Principal
##### dentro da página de produto

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no anúncio do produto | --- |
| --- | 2. Redireciona usuário para página do produto clicado |
| 3.  Clica no botão para adicionar produto no carrinho | --- |
| --- | 4.Verifica a disponibilidade do produto |
| --- | 5. Adiciona produto no carrinho do usuário |
| --- | 6. Informa mensagem de que o produto foi adicionado |
| --- | 7. Redireciona para a página do Carrinho |
| 8. Continua navegando | --- |

#### 5.2. Fluxo alternativo
##### Produto Indisponível

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão de adicionar produto no carrinho | --- |
| --- | 2. Verifica a disponibilidade do produto. |
| --- | 3. Informa ao usuário que o produto está indisponível. | --- |
| 4. Continua navegando | --- |

### 6. Dicionário de dados

### 7. Protótipos de UI