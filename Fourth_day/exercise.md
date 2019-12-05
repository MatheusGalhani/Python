# DXC - Python 4º dia

Neste exercicio você deverá criar um arquivo chamado de "utilitarios.py" e um arquivo chamado de "index.py"

* No seu arquivo "utilitarios" iremos criar os seguintes métodos.

### Método Número Aleatório - Utilizando método recursivo
Este método deverá receber um número X que o usuário deverá informar através do input.
Este método será recursivo e o ponto final será quando o número randomico for igual ao que ele digitou.

````text
numero digitado (1 até 20) => 15
Chamando a função recursiva...
número aleatório = 10
Chamando a função recursiva...
número aleatório = 15

Você precisou de 2 tentativas para acertar o número aleatório

````

### Método Número Aleatório - Utilizando interação (for ou while)
Este método deverá ter as mesmas entradas e saidas do anterior, porém utilizando um laço de repetição

### Método para selecionar 3 nomes
Neste método você irá receber uma lista de nomes que será inputada pelo usuário, sendo que está lista tem que possuir ao menos 3 registros.

No seu método deverá ser implementado um método que selecionará 3 nomes de forma aleatória, sendo que não poderá pegar o mesmo indice mais de uma vez.

````text
nomes = ["Matheus", "Pedro", "Julia", "Raul", "Gustavo"]
retorno da função = ["Julia", "Matheus", "Raul"]
````

### Método para informar a seu tempo de vida
Neste método você receberá a data de nascimento e deve retornar ao usuário quantos dias está vivo

````text
data_nascimento = 30/08/2019
retorno = Você tem X dias na terra.
````

### Método para transformar um dicionario em listas
Neste método você receberá um dicionário e retornara para ele uma lista

````text
dicionario = {"nome": "Matheus", "idade": 23}
retorno = [["nome", "Matheus"], ["idade", 23]]
````

### Método para retornar a lista dos usuários aprovados
Neste método você receberá um dicionário e retornara para ele uma dicionario com os alunos que passaram no treinamento (nota 6 ou mais)

````text
dicionario = {1: ["Matheus", 10], 2: ["Pedro", 6], 3: ["Jorge": 5.5], 4: ["Giba": 7.5]}
retorno = {1: ["Matheus", 10], 2: ["Pedro", 6], 4: ["Giba": 7.5]}
````

* No seu arquivo "index" deveremos realizar as chamadas de todos os métodos criamos anteriormente.
