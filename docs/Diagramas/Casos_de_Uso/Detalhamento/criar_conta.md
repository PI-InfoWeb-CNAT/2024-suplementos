# Projeto Comercio Eletrônico - PowerUp

## Especificação do caso de uso - Criar conta

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 30/04/2024 | **1.00** | Adição da seção de resumo e atores | Lucas Brito |
| 13/11/2024 | **2.00** | Finalização do detalhamento | David Paiva |


### 1. Resumo 
Como usuário não identificado, desejo ter a opção de criar uma conta.

### 2. Atores
- Visitante (usuário não cadastrado)

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
- 	Possuir um email existente para criação da conta.

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  Cadastre a conta criada pelo usuário no banco de dados.

### 5. Fluxos de evento

#### 5.1. Fluxo Principal

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Cadastrar" | --- |
| --- | 2. Redireciona usuário para página de cadastro |
| 3.  Informa os dados e cria uma senha | --- |
| --- | 4. Salva a conta no banco de dados |
| --- | 5. Redireciona para página de login |
| 6. Loga na conta criada | --- |
| 7. Navega pelo site | --- |

#### 5.2. Fluxo alternativo
##### erros nos dados informados

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Cadastrar" e é redirecionado para a página de cadastro. | --- |
| 2. Preenche o formulário com dados e clica em "Criar Conta".
| --- | 3. Se o email já estiver em uso ou for inválido, o sistema exibe uma mensagem de erro informando o conflito. |
| --- | 3.1 Se a senha for fraca (menos de 8 caracteres), exibe uma mensagem de erro recomendando uma senha mais forte. |
| 4. Corrige o(s) erro(s) e tenta novamente enviar o formulário. | --- |
| --- | 5  Sistema salva a conta e redireciona para a página de login.


### 6. Dicionário de dados
Email	| Email do usuário para contato e login	| String (válido)
Senha	| Senha de acesso da conta	|  String (mín. 8 caracteres)
Nome	| Nome completo do usuário	|  String (1-100 caracteres)
Telefone (opcional)	| Número de contato do usuário | String (formato: +XX)

### 7. Protótipos de UI
![image](https://github.com/user-attachments/assets/38910fe3-6b9c-4dc5-abab-790d0562e2a7)


