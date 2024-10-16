# Projeto Comércio Eletrônico - PowerUp

## Especificação do caso de uso - Avaliar Produto

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 14/10/2024 | **1.00** | Finalização do detalhamento | Maria Vitória |

### 1. Resumo 
Como um usuário identificado, desejo avaliar um produto que já comprei.

### 2. Atores
- Cliente

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
- 	Estar logado, produto ter sido comprado.

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  Exibir avaliações.

### 5. Fluxos de evento

#### 5.1. Fluxo Principal
##### dentro da página de produto

|  Ator  | Sistema |
|:-------|:------- |
| 1. Usuário clica em Meus pedidos, detalhes do pedido e avaliar produto| --- |
| --- | 2. Sistema redireciona usuário para modal de avaliação |
| 3.  Usuário clica no botão para avaliar | --- |
| --- | 4. Sistema adiciona avaliação |
| 6. Usuário Continua Navegando | --- |


#### 5.2. Fluxo alternativo
##### Avaliação Incompleta

|  Ator  | Sistema |
|:-------|:------- |
| 1. Usuário clica no botão para avaliar| --- |
| --- | 2. Sistema verifica se todos os campos obrigatórios foram preenchidos|
| --- | 2. Sistema informa ao usuário que alguns campos obrigatórios estão vazios. |
| 4. Usuário preenche os campos faltantes e tenta enviar a avaliação novamente. | --- |
| 4. Usuário Continua Navegando | --- |

### 6. Dicionário de dados

### 7. Protótipos de UI


