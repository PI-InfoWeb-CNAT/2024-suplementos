# Projeto Comercio Eletrônico - PowerUp

## Especificação do caso de uso - Manter conta

### Histórico da Revisão
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 30/04/2024 | **1.00** | Adicionar seção de resumo e atores | Pedro Edi |


### 1. Resumo 
Detalha o processo de como manter uma conta (CRUD).
### 2. Atores
- Moderador/Administrador 

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
-  Estar logado como Moderador ou Administrador.
-  Ter uma conta previamente registrada no sistema.

### 4.Pós-condições
Após a execução deste casos de uso, espera que o sistema:
-  Exibir, atualizar, criar ou excluir informações de contas dos usuários.

### 5. Fluxos de evento
- No fluxo principal, definir o passo a passo de como vai ocorrer o caso de uso da forma padrão.
- No fluxo alternativo, definir o passo a passo de como vai ocorrer o caso de uso em uma forma alternativa. Opcional.
- Exemplo abaixo de um caso de uso "Adicionar ao carrinho".

#### 5.1. Fluxo Principal
##### dentro do sistema

|  Moderador  | Sistema |
|:-------|:------- |
| 1. Acessa a seção de gerenciamento de contas no painel de administração. | --- |
| --- | 2. Sistema exibe a lista de contas existentes. |
| 3.  Seleciona uma conta para exibir ou editar informações. | --- |
| --- | 4. Exibe os detalhes da conta selecionada para visualização/edição. |
| 5.  Faz modificações ou opta por excluir/criar uma conta nova. |
| --- | 6. Salva as modificações ou cria/exclui a conta no banco de dados. |
| --- | 6. Usuário Continua Navegando. |



### 6. Dicionário de dados
Nome | Nome completo do usuário	| String (1-100 caracteres)
Email	| Email para contato e login | String (formato válido)
Status da Conta	| Estado da conta (Ativo/Inativo)	| Boolean
Tipo de Conta	| Tipo de permissão (Admin/Usuário)	| String

### 7. Protótipos de UI
Tela de Gerenciamento de Contas
Campos: Nome, Email, Status, Tipo de Conta.
Botões: "Salvar", "Excluir Conta", "Criar Nova Conta".
Feedbacks: Mensagens de erro para campos inválidos ou operações de sucesso.



