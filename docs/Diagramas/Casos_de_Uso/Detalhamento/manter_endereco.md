# Projeto Comercio Eletrônico - PowerUp

## Especificação do caso de uso - Visualizar promocoes

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 14/05/2025 | **1.00** | Detalhamento completo | Lucas Brito |


### 1. Resumo 
Como um usuário identificado desejo gerenciar os meus endereços.

### 2. Atores
- Cliente

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
- 	O usuário deve possuir conta no site.
-   O usuário deve estar logado no site.

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  O usuário deve conseguir gerenciar (visualizar, criar, atualizar e excluir) os endereços dele.

### 5. Fluxos de evento

#### 5.1. Fluxo Principal 
##### visualização dos endereços

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Meu Perfil" | --- |
| --- | 2. Redireciona para a página e exibe os endereços do cliente (se houver) |
| 3. Visualiza os seus endereços (se houver) | --- |
| 4. Navega pelo site | --- |

#### 5.2. Fluxo alternativo
##### criação de um endereço

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Meu Perfil" | --- |
| --- | 2. Redireciona para a página e exibe os cartões do cliente (se houver) |
| 3. Visualiza os seus endereços (se houver) | --- |
| 4. Aperta na caixa de "Adicione um novo endereço" | --- |
| --- | 5. Exibe um modal com os campos para o cliente adicionar |
| 6. Preenche todos os campos e aperta no botão "Adicionar" | --- |
| --- | 7. Atualiza a página e exibe a lista de endereços, incluindo o adicionado |
| 8. Navega pelo site | --- |

#### 5.3. Fluxo alternativo
##### edição de um endereço

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Meu Perfil" | --- |
| --- | 2. Redireciona para a página e exibe os endereços do cliente (se houver) |
| 3. Visualiza os seus endereços | --- |
| 4. Escolhe um endereço e aperta no botão de "Editar" | --- |
| --- | 5. Exibe um modal com os campos para o cliente atualizar |
| 6. Altera algum(ns) campo(s) e aperta no botão "Atualizar" | --- |
| --- | 7. Atualiza a página e exibe o endereço, agora atualizado |
| 8. Navega pelo site | --- |

#### 5.4. Fluxo alternativo
##### exclusão de um endereço

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Meu Perfil" | --- |
| --- | 2. Redireciona para a página e exibe os endereços do cliente (se houver) |
| 3. Visualiza os seus endereços | --- |
| 4. Escolhe um endereço e aperta no botão de "Excluir" | --- |
| --- | 5. Exibe um modal alertando que a exclusão é permanente |
| 6. Aperta o botão de "Excluir" novamente e confirma a exclusão | --- |
| --- | 7. Atualiza a página e exibe a lista de endereços sem o endereço excluído |
| 8. Navega pelo site | --- |

### 6. Dicionário de dados

### 7. Protótipos de UI