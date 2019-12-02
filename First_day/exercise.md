# DXC - Python 1º dia
Crie um programa que recebe uma lista de dados sobre candiadatos que se cadastraram para entrar na DXC Technology. Nesta lista de cadastro deverá ser armazenados os seguintes campos:
* Nome (string)
* CPF (string)
* Idade (int)
* Email (string)
* Faculdade/Curso (string)
* Semestre atual (int)
* Quantidade de semestres da faculdade (int)
* Linguagem favorita (string)
* Chave de classificação => Calculado automaticamente

Para que o cadastro possa ser cadastrado existe um critério de aceitação, a qual deve ser exibido uma mensagem caso o mesmo não puder ser cadastrado na vaga de estagio. Caso todos os pré-requisitos forem atentidos, deve-se retornar uma menssagem de "Cadastro no processo seletivo realizado com sucesso. Você está na chave de classificação X"

Os critérios para cadastro são:
* Ser maior de idade
* O CPF possuir 11 digitos e os mesmos não serem números repetidos ou sequenciais (111, 123)
* O email possuir @ e .com
* Não estar no último ano de faculdade, ou seja, semestre atual + 2 não pode ser maior ou igual a quantidade de semestres da faculdade


A chave de classificação será dividida em 3 grupos A, B, C:
#### Chave A:
* 18 a 20 anos
* Nome Palindromo
* Cursando a metade ou menos do total de semestres da faculdade

#### Chave B
* 25 ou mais anos
* Cursando a metade ou mais do total de semestres da faculdade
* Linguagem favorita seja Python

#### Chave C
* Não atenda os requisitos da chave A e B


Após finalizar o cadastro de todos os integrantes através menu1, exibir o menu2 que irá exibir os dados dos candidatos de acordo com a sua chave de classificação. Sendo que a informação deverá ser exibida da seguinte maneira:
```text
    Candidato INFORMAR_NOME de INFORMAR_IDADE, cursando INFORMAR_FACULDADE/CURSO, gosta de programar em INFORMAR_LINGUAGEM_PREFERIDA 
```

#### Menu1
```text
    1 - Cadastrar Novo Integrate
    0 - Finalizar cadastros
```

#### Menu2
```text
    1 - Chave A
    2 - Chave B
    3 - Chave C
    0 - Sair do programa
```
