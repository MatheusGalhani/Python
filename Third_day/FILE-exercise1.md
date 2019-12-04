# DXC - Python 3º dia
Crie um programa que receberá dados dos funcionarios da DXC Technology. Nesta cadastro deverá ser armazenados os seguintes campos:
* Employee ID (Identificador único automático)
* Nome do funcionário (string)
* Idade (int)
* CPF (string)
* Equipe atual (string)
* Meses nesta equipe (int)
* Feliz na equipe (string)
* Linguagens conhecidas (lista)

O cadastro acima deverá ser feito através uma classe e o objeto deverá ser armazenado em um dicionário, cujo a chave será o Employee ID.

A classe deverá um método de exibição que será usado na geração do relatório, o qual irá retornar os dados formatados no seguite formato.

### Cabeçalho:
```text
Employee ID;Nome do funcionário;Idade;CPF;Equipe atual;Meses nesta equipe;Feliz na equipe;Linguagens conhecidas;
```
### Retorno do método:
```text
6001236;Matheus Galhani;23;69532561453;Billing;4;S;[Python, JavaScript, Java, PL/SQL];
```
### Exemplo de um relatório:
```text
Employee ID;Nome do funcionário;Idade;CPF;Equipe atual;Meses nesta equipe;Feliz na equipe;Linguagens conhecidas;
6001236;Matheus Galhani;23;69532561453;Billing;4;S;[Python, JavaScript, Java, PL/SQL];
```

