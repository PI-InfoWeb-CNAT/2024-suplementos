# Projeto Comercio Eletrônico - PowerUp

## Especificação do caso de uso - Manter conta

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 14/05/2025 | **1.00** | Detalhamento completo | Lucas Brito |


### 1. Resumo 
Como um administrador, desejo gerenciar os pedidos do site.

### 2. Atores
- Moderador/Administrador

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
-  Ter uma conta previamente registrada no sistema.
-  Estar logado como administrador.

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  O administrador deve conseguir gerenciar (visualizar, atualizar e excluir) os pedidos do site.

### 5. Fluxos de evento

#### 5.1. Fluxo Principal 
##### visualização dos pedidos

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Pedidos" | --- |
| --- | 2. Redireciona para a página e exibe uma tabela com os pedidos (se houver) |
| 3. Visualiza os pedidos (se houver) | --- |
| 4. Navega pelo site | --- |

#### 5.2. Fluxo alternativo
##### edição de um pedido

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Pedidos" | --- |
| --- | 2. Redireciona para a página e exibe uma tabela com os pedidos |
| 3. Visualiza os pedidos | --- |
| 4. Escolhe um pedido e clica no botão de "Editar" | --- |
| --- | 5. Exibe um modal para o administrador com os campos necessários |
| 6. Altera o campo e clica no botão "Atualizar" | --- |
| --- | 7. Recarrega a página e mostra a tabela, agora com o pedido atualizado |
| 8. Navega pelo site | --- |

#### 5.3. Fluxo alternativo
##### exclusão de um pedido

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Pedidos" | --- |
| --- | 2. Redireciona para a página e exibe uma tabela com os pedidos |
| 3. Visualiza os pedidos | --- |
| 4. Escolhe um pedido e clica no botão de "Excluir" | --- |
| --- | 5. Exibe um modal alertando que a exclusão é permanente |
| 6. Aperta o botão de "Excluir" novamente e confirma a exclusão | --- |
| --- | 7. Recarrega a página e exibe a tabela de pedidos sem o pedido excluído |
| 8. Navega pelo site | --- |
### 6. Dicionário de dados

### 7. Protótipos de UI