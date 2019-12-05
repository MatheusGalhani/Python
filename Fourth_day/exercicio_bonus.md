# DXC - Python 4º dia - Bônus

Neste exercicio vamos criar uma plataforma para um banco.

Para isso iremos começar criando 2 classes

* Classe: Banco
````text
Código da agência (int)
Gerente (string)
````

* Classe: Cliente (deverá extender Banco)
````text
Nome (string)
Número da conta (int unico de 5 digitos gerado automaticamente)
Digito da conta (int 0-9 gerado automaticamente)
Idade (int)
CPF (string)
Email (string)
Endereço completo (string)
Produtos adiquiridos (lista)
Data de cadastro (date)

````

Seu programa deverá ter um menu interativo que deverá seguir o seguinte modelo
````text
1 - Cadastrar Novo cliente
2 - Alterar Endereço do cliente
3 - Contratar novo produto do banco
4 - Cancelar produto do banco
5 - Gerar um arquivo de Backup dos dados do banco
6 - Ler o arquivo de Backup e recadastrar os dados
7 - Relatório dos clientes que possuem 10 meses cadastrados
8 - Relatório de todos os clientes de 18 até 25 anos
0 - Sair
````

Este desafio deverá estar cadastrando cada cliente em um dicionario, onde a chave será uma string "{Número da conta}-{Digito da conta}"

````text
clientes_banco = {"14235-3": cliente_matheus}
````