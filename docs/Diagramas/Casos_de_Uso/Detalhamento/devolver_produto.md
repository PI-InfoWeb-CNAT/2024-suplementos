# Projeto Comércio Eletrônico - PowerUp

## Especificação do caso de uso - Devolver produto

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 21/10/2024 | **1.00** | Cliente solicita a devolução de um item | Maria Vitoria |


### 1. Resumo 
O usuário solicita a devolução de um produto dentro de um tempo determinado após comprá-lo.

### 2. Atores
- Cliente
- Sistema

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
- 	Estar logado, O produto a ser devolvido deve estar registrado na conta do cliente e estar dentro do prazo de devolução.

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  O cliente é informado sobre o status da devolução.

### 5. Fluxos de evento
- No fluxo principal, definir o passo a passo de como vai ocorrer o caso de uso da forma padrão.
- No fluxo alternativo, definir o passo a passo de como vai ocorrer o caso de uso em uma forma alternativa. Opcional.
- Exemplo abaixo de um caso de uso "Adicionar ao carrinho".

#### 5.1. Fluxo Principal
##### dentro da página de produto

|  Ator  | Sistema |
|:-------|:------- |
| 1. Usuário acessa a página de "Meus Pedidos"| --- |
| --- |2. O sistema registra a solicitação de devolução|
| 3. Usuário seleciona o pedido com o produto a ser devolvido | --- |
| --- |	4. Sistema exibe detalhes do pedido |---
| 5. Usuário clica no botão "Solicitar Devolução" | --- 
| --- | 6. Sistema solicita confirmação da devolução|
|7. Usuário confirma a devolução|---
| --- | 8. Sistema registra a solicitação e informa o prazo para reembolso|
|9. Usuário é informado sobre o status da devolução|---

#### 5.2. Fluxo alternativo
##### Devolução fora do prazo

|  Ator  | Sistema |
|:-------|:------- |
| 1. Usuário tenta solicitar devolução após o prazo | --- |
| --- | 2. Sistema valida data|
| --- | 3. Sistema exibe mensagem informando que o prazo para devolução expirou|
|4. Usuário é informado que a devolução expirou | --- |


### 6. Dicionário de dados

### 7. Protótipos de UI


