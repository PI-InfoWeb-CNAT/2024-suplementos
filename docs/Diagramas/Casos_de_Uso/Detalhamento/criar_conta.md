# Projeto Comercio Eletrônico - PowerUp

## Especificação do caso de uso - Criar conta

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 30/04/2024 | **1.00** | Adição da seção de resumo e atores | David Paiva |


### 1. Resumo 
Como usuário não identificado, desejo ter a opção de criar uma conta.

### 2. Atores
- Visitante (usuário não cadastrado)

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
- 	Possuir um email existente para criação da conta

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  Permitir navegação e usar os serviços de compra do site

### 5. Fluxos de evento

#### 5.1. Fluxo Principal
##### dentro da página de login

|  Ator  | Sistema |
|:-------|:------- |
| 1. Usuário clica botão "criar conta" | --- |
| --- | 2. Sistema redireciona usuário para página criar conta |
| 3.  Usuário informa os dados e cria uma senha | --- |
| --- | 4. Sistema salva a conta no banco de dados |
| --- | 5. Sistema redireciona para página de login novamente |
| 6. Usuário loga na conta criada | --- |
| 7. Usuário navega pelo site | --- |

#### 5.2. Fluxo alternativo
##### fora da página de login

|  Ator  | Sistema |
|:-------|:------- |
| 1. Clica no botão "Criar Conta" e é redirecionado para a página de cadastro. | --- |
| 2. Preenche o formulário com dados e clica em "Criar Conta".
| --- | 3. Se o email já estiver em uso ou for inválido, o sistema exibe uma mensagem de erro informando o conflito. |
| --- | 3.1 Se a senha for fraca (menos de 8 caracteres ou sem complexidade), exibe uma mensagem de erro recomendando uma senha mais forte. |
| 4. Corrige o(s) erro(s) e tenta novamente enviar o formulário. | --- |
| --- | 5  sistema salva a conta e redireciona para a página de login.


### 6. Dicionário de dados
Email	| Email do usuário para contato e login	| String (válido)
Senha	| Senha de acesso da conta	|  String (mín. 8 caracteres)
Nome	| Nome completo do usuário	|  String (1-100 caracteres)
Telefone (opcional)	| Número de contato do usuário | String (formato: +XX)

### 7. Protótipos de UI
Tela de Cadastro
Campos: Nome, Email, Senha, Confirmação de Senha.
Botões: "Criar Conta", "Voltar para Login".
Feedbacks: Mensagens de erro para email inválido, senha fraca ou senha e confirmação de senha diferentes.
Tela de Login
Campos: Email, Senha.
Botões: "Entrar", "Esqueceu a Senha?", "Criar Conta".
Feedbacks: Mensagem para login incorreto.


