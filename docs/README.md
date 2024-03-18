# Documento de visão

## Comércio Eletrônico

### Histórico da Revisão 
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 03/03/2024 | **1.00** | Versão Inicial  | David Paiva, Diego Luiz, Lucas Brito e Pedro Edi |

## 1. Objetivo do Projeto 
Este projeto tem objetivo de desenvolver um site que implemente as funcionalidades de uma loja de suplementos on-line.
 
## 2. Descrição do problema 
|:-|:-|
| **_O problema_**    | O lojista que atua no comércio convencional, na área de suplementação, deseja resolver o problema da falta de controle de validade do estoque em sua loja física  |
| **_afetando_**      | o lojista e os clientes                  |
| **_cujo impacto é_**| o descarte de produtos por falta de controle de validade e consequente queda nos lucros                                    |
| **_uma boa solução seria_** | a criação de um site de suplementos da loja física para obter o controle da validade do estoque |

## 3. Descrição dos usuários
| Nome | Descrição | Responsabilidades |
|:- |:- |:- |
| Cliente  | Usuário cadastrado no site | Visualizar os produtos; pesquisar produtos; comprar produtos; adicionar produtos ao carrinho; avaliar produtos adquiridos; cancelar pedido; solicitar devolução do produto. |
| Visitante   | Usuário não cadastrado no site | Visualizar produtos; pesquisar produtos.  |
| Moderador | Administrador do site | Adicionar e remover produtos; gerenciar os pedidos.

## 4. Descrição do ambiente dos usuários 
O comércio eletrônico tem dois tipos de usuários. O tipo administrador representa o gestor da loja e seus colaboradores e o usuário, seja ele anônimo ou já cadastrado. 

O administrador acessará o site a partir do ambiente físico da loja ou em casa e fará a configuração dos produtos a serem vendidos e realizará a logística de atendimento dos pedidos coletados pelo site, registrando a informação de situação de envio dos pedidos. 

O usuário irá acessar o site utilizando  um computador ou celular e realizará a visualização dos produtos vendidos na loja e realizará a compra, caso deseje. As tarefas executadas pelos clientes, como uma compra, devem ser possíveis 24 horas por dia, durante os 7 dias da semana.

O site precisará da utilização de internet, fato que pode limitar o acesso ao sistema dependendo da qualidade do sinal disponível.


## 5. Principais necessidades dos usuários
Considerando o pronto de vista do lojista, administrador do site, sua principal necessidade é controlar a validade do estoque de sua loja. Portanto, tem a necessidade de um site para a realização desse controle, além de conseguir alcançar mais pessoas e faturar mais.

Considerando o pronto de vista do cliente, ele deseja ter acesso a um site com interface amigável que permita obter informações sobre os produtos comercializados e, caso identifique que estes atendam às suas necessidades, ele possa montar sua relação de compra confirmando a aquisição. Após essa etapa ele desejará visualizar o processo de entrega dos produtos adquiridos.

## 6. Alternativas concorrentes
Entre as alternativas concorrentes existem as outras lojas de suplementos presentes no mercado atual: Growth, Max Titanium, Integralmédica, Darkness, etc.

## 7.	Visão geral do produto
Esse projeto consiste em um site voltado para vendas de produtos que pretende funcionar de forma rápida e eficiente para ser utilizado nos navegadores (browsers), disponibilizando um ambiente acessível a diversos tipos de usuários e possuindo um design confortável e responsivo. Para tal, o site irá disponibilizar diferentes mecanismos de busca permitindo que o usuário encontre de forma eficiente o que ele precisa. Após a aquisição, o usuário poderá acompanhar o produto comprado, avaliar produtos da loja e marcar produtos como favoritos. 

## 8.	Requisitos funcionais
| Código | Nome | Descrição |
|:---  |:--- |:--- |
| F01	| Criar conta | Permite que um visitante se cadastre e crie sua conta para poder comprar produtos.
| F02	| Efetuar login	| Permite que um cliente entre na sua conta.
| F03	| Gerenciar conta	| Habilita o cliente a consultar e editar seus dados de perfil.
| F04	| Adicionar e remover produtos	| O administrador tem à sua disponibilidade a função de adicionar e remover produtos
| F05	| Consultar pedidos realizados e não enviados.	| O administrador pode acessar os dados de vendas de produtos do site que foram realizados pelos clientes e que ainda não foram remetidos.
| F06	| Pesquisar produto	| Permite que o cliente coloque o nome de algum produto específico e, ao enviar, apareça os produtos correspondentes à sua pesquisa.
| F07	| Visualizar produtos	| O usuário visualiza os produtos disponíveis filtrando de acordo com suas necessidades e também de acordo com o produto.
| F08	| Adicionar ou remover produtos ao carrinho	| O usuário pode escolher mais de um produto para realizar a compra e inserir no carrinho.
| F09	| Realizar a compra | Os clientes podem confirmar a compra dos produtos adicionados em seu carrinho, gerando assim um pedido.
| F10	| Realizar o cancelamento de pedido solicitado	| Os clientes podem solicitar o cancelamento de um pedido realizado desde que ainda não tenha sido enviado.
| F11	| Verificar as compras realizadas	| Os clientes podem verificar seu histórico de compra na loja.
| F12	| Verificar o andamento do pedido	| Os clientes podem acompanhar o andamento da entrega dos pedidos realizados.
| F13	| Avaliar o Produto	| Os clientes podem avaliar os produtos realizando um comentário e atribuindo uma nota.
| F14	| Devolver o produto	| Permite que o cliente solicite a devolução do produto, causada por erro no envio ou algo semelhante. 

## 9.	Requisitos não-funcionais
| Código | Nome | Descrição | Categoria | Classificação |
|:---  |:--- |:--- |:--- |:--- |
| NF01	| Tecnologias utilizadas no desenvolvimento 	| O site deverá ser feito utilizando HTML, CSS e JS no front-end. No back-end deverá ser utilizado Python com Django e o banco de dados será o PostgreSQL. | Usabilidade	| Obrigatório
| NF02	| Design responsivo	| O site apresentará responsividade, deixando-o mais confortável para o usuário | Usabilidade	| Obrigatório
| NF03	| Acesso somente com internet	| É necessário um acesso contínuo à Internet para poder acessar os dados do site e suas funcionalidades, como comprar produtos.	| Disponibilidade	| Obrigatório
| NF04	| Criptografia de Dados	| Senhas do usuário devem ser gravadas de forma criptografada no banco de dados	| Segurança	| Obrigatório
| NF05	| Facilidade de Uso	| O sistema deve apresentar uma interface amigável, para que o cliente consiga utilizá-lo facilmente e consiga efetuar suas funcionalidades sem precisar de nenhum tipo de manual.	| Usabilidade	| Obrigatório
