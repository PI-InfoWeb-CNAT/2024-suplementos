# Projeto Comercio Eletrônico - PowerUp

## Especificação do caso de uso - Visualizar promocoes

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 16/09/2024 | **1.00** | Adicionar seção de resumo e atores | Pedro Edi |


### 1. Resumo 
Como um usuário, identificado ou não, desejo listar e filtrar produtos.

### 2. Atores
- Moderador/Administrador
- Cliente
- Visitante

### 3. Pré-condições
 - **Acesso ao site**: O usuário deve ter acesso ao site, garantindo que o site esteja online e disponível.
- **Navegador compatível**: O site deve ser acessado através de um navegador compatível para garantir que todas as funcionalidades
funcionem corretamente.
- **Existencia do opção promoções em uma página**: O usuário deve estar em uma área de navegação onde se tenha um link para a página de promoções (ex.: homepage).

### 4.Pós-condições
  - **Exibição correta das informações**: O site exibe corretamente as informações das promoções dos produtos (descrição, preços, prazos, etc.).

### 5. Fluxos de evento

#### 5.1. Fluxo Principal

|  Ator  | Sistema |
|:-------|:------- |
| 1.O usuário navega para a seção de promoções ou ofertas do site (por exemplo, clicando em um link ou botão de "Promoções"). | ---|
| --- | 2. Inicia o processo de pesquisa no banco de dados de produtos com promoção. |
| --- | 3. O sistema  carrega a página de promoções e exibe as ofertas atuais.
| 4.  Clica em um produto específico para obter mais informações detalhadas.| --- |
| --- | 5. Redireciona o usuário para a página de detalhes do produto, exibindo uma descrição completa, imagens adicionais, preço e avaliações de clientes.|
| 6. Usuário Continua Navegando | --- |

#### 5.2. Fluxo alternativo
##### Nenhum produto encontrado

|  Ator  | Sistema |
|:-------|:------- |
| 1.Usuário entra na página de promoções. | --- |
| --- | 2. Inicia o processo de pesquisa no banco de dados de produtos. |
|--- | 3. Exibe uma mensagem informando "Nenhum produto em promoção no momento". |
| 4. Usuário Continua Navegando | --- |


### 6. Dicionário de dados

### 7. Protótipos de UI


