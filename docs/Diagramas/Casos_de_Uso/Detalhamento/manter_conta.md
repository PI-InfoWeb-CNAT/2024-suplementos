# Projeto Comercio Eletrônico - PowerUp

## Especificação do caso de uso - Manter conta

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 14/05/2025 | **1.00** | Detalhamento completo | Lucas Brito |


### 1. Resumo 
Como um usuário identificado desejo gerenciar a minha conta.

### 2. Atores
- Cliente
- Moderador/Administrador

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
-  Ter uma conta previamente registrada no sistema.
-  Estar logado como administrador ou cliente.

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  O usuário deve conseguir gerenciar (visualizar, atualizar e excluir) a sua conta.

### 5. Fluxos de evento

#### 5.1. Fluxo Principal 
##### visualização da conta

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Meu Perfil" | --- |
| --- | 2. Redireciona para a página e exibe os dados do cliente |
| 3. Visualiza os seus dados | --- |
| 4. Navega pelo site | --- |

#### 5.2. Fluxo alternativo
##### edição dos dados da conta

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Meu Perfil" | --- |
| --- | 2. Redireciona para a página e exibe os dados do cliente |
| 3. Visualiza os seus dados | --- |
| 4. Altera algum(ns) campo(s) e aperta no botão "Atualizar" | --- |
| --- | 5. Recarrega a página, agora com os dados atualizados |
| 6. Navega pelo site | --- |

#### 5.3. Fluxo alternativo
##### exclusão da conta

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Meu Perfil" | --- |
| 2. Clica no botão "Excluir Conta" | --- |
| --- | 3. Exibe um modal alertando que a exclusão é permanente |
| 4. Aperta o botão de "Excluir" novamente e confirma a exclusão | --- |
| --- | 7. Redireciona o usuário, agora anônimo, para a página principal |
| 8. Navega pelo site | --- |

### 6. Dicionário de dados

### 7. Protótipos de UI