# Projeto Comercio Eletrônico - PowerUp

## Especificação do caso de uso - Favoritar Produto

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 21/10/2024 | **1.00** | O cliente adicionar produto a lista de favoritos | Maria Vitória |


### 1. Resumo 
Detalha o processo de como favoritar um determinado produto que gerou interesse.

## 2. Atores
- Cliente
- Sistema

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
- Estar logado, produto a ser favoritado estar cadastrado.

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  O produto é adicionado à lista de favoritos do cliente. 

### 5. Fluxos de evento
- No fluxo principal, definir o passo a passo de como vai ocorrer o caso de uso da forma padrão.
- No fluxo alternativo, definir o passo a passo de como vai ocorrer o caso de uso em uma forma alternativa. Opcional.
- Exemplo abaixo de um caso de uso "Adicionar ao carrinho".

#### 5.1. Fluxo Principal
##### Favoritar Produto

|  Ator  | Sistema |
|:-------|:------- |
| 1. Usuário clica no anúncio do produto | --- |
| --- | 2. Sistema redireciona usuário para página do Produto clicado |
| 3. Usuário clica no botão "Favoritar". | --- |
| --- | 4. Sistema adiciona o produto à lista de favoritos do usuário |
| --- | 5. Sistema informa mensagem de que o produto foi favoritado |
| 6. Usuário Continua Navegando | --- |

#### 5.2. Fluxo alternativo
##### Remover Produto da Lista de Favoritos

|  Ator  | Sistema |
|:-------|:------- |
| 1. Usuário acessa a página de "Favoritos" | --- |
| --- |	2. Sistema exibe a lista de produtos favoritos do usuário |
| 3. Usuário clica no botão "Remover" ao lado do produto desejado|
| 4. Sistema remove o produto da lista de favoritos e exibe mensagem de que o produto foi removido| --- |
| 5. Usuário Continua Navegando | --- |


### 6. Dicionário de dados
![image](https://github.com/user-attachments/assets/7c6b6cef-7d1b-4761-b932-3ddf51ac7cf5)


### 7. Protótipos de UI
