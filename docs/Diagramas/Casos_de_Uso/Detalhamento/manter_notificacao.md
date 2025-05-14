# Projeto Comercio Eletrônico - PowerUp

## Especificação do caso de uso - Manter conta

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 14/05/2025 | **1.00** | Detalhamento completo | Lucas Brito |


### 1. Resumo 
Como um administrador, desejo gerenciar as notificações do site.

### 2. Atores
- Moderador/Administrador

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
-  Ter uma conta previamente registrada no sistema.
-  Estar logado como administrador.

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  O administrador deve conseguir gerenciar (visualizar, criar, atualizar e excluir) as notificações do site.

### 5. Fluxos de evento

#### 5.1. Fluxo Principal 
##### visualização das notificações

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Notificações" | --- |
| --- | 2. Redireciona para a página e exibe uma tabela com as notificações (se houver) |
| 3. Visualiza as notificações (se houver) | --- |
| 4. Navega pelo site | --- |

#### 5.2. Fluxo alternativo
##### criação de uma notificação

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Notificações" | --- |
| --- | 2. Redireciona para a página e exibe uma tabela com as notificações (se houver) |
| 3. Clica no botão "Adicionar notificação" | --- |
| --- | 4. Exibe um modal para o administrador com os campos necessários |
| 5. Preenche todos os campos e clica no botão "Adicionar" | --- |
| --- | 6. Recarrega a página e mostra a tabela, agora com a notificação adicionada |
| 7. Navega pelo site | --- |

#### 5.3. Fluxo alternativo
##### edição de uma notificação

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Notificações" | --- |
| --- | 2. Redireciona para a página e exibe uma tabela com as notificações |
| 3. Visualiza as notificações | --- |
| 4. Escolhe uma notificação e clica no botão de "Editar" | --- |
| --- | 5. Exibe um modal para o administrador com os campos necessários |
| 6. Preenche algum(ns) campo(s) e clica no botão "Atualizar" | --- |
| --- | 7. Recarrega a página e mostra a tabela, agora com a notificação atualizada |
| 8. Navega pelo site | --- |

#### 5.4. Fluxo alternativo
##### exclusão de uma notificação

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Notificações" | --- |
| --- | 2. Redireciona para a página e exibe uma tabela com as notificações |
| 3. Visualiza as notificações | --- |
| 4. Escolhe uma notificação e clica no botão de "Excluir" | --- |
| --- | 5. Exibe um modal alertando que a exclusão é permanente |
| 6. Aperta o botão de "Excluir" novamente e confirma a exclusão | --- |
| --- | 7. Recarrega a página e exibe a tabela de notificações sem a notificação excluída |
| 8. Navega pelo site | --- |
### 6. Dicionário de dados

### 7. Protótipos de UI