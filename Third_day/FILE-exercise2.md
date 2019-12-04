# DXC - Python 3º dia
Com o código que você criou no "FILE-exercise1" realize as seguintes funções interativas.

### Menu de cadastro
```text
    1 - Cadastrar Novo Funcionário
    2 - Alterar Dados do Funcionário
    3 - Gerar Relatório
    4 - Ler relatório
    0 - Sair
```

A opção de Ler relatório, deverá cadastrar o funcionário que não está cadastrado, ou seja, um employee não existe no dicionário.

### Exemplo
```text
  Relatório:
  Employee ID;Nome do funcionário;Idade;CPF;Equipe atual;Meses nesta equipe;Feliz na equipe;Linguagens conhecidas;
  6001236;Matheus Galhani;23;69532561453;Billing;4;S;[Python, JavaScript, Java, PL/SQL];
  6001235;Ricardo Alberto;25;78523147856;CRM;2;N;[C#, Python];
  
  Kwargs = {6001236: funcionario}
```
Veja que no exemplo acima eu só possuo a chave do funcionário 6001236, já o 6001235 não existe.
Nese caso devemos criar uma instancia da Classe Funcionarios, com os valores que lemos do relátorio e cadastra-lo (sem a necessidade de um input).

### Help 
```python
string = "6001235;Ricardo Alberto;25;78523147856;CRM;2;N;[C#, Python];"
lista = string.split(";")
#recuperando os valores. Basta acessar a posição exata da nossa lista
employee = lista[0]
nome = lista[1]
#transforma a string "[C#, Python]" em uma lista ["C#", "Python"]
linguagens = lista[7].strip('[]').replace('"', '').replace(' ', '').split(',')
kwargs[employee] = Funcionarios(employee=employee, nome=nome,...)

```

A opção de gerar relatório terá o seguinte menu:

### Menu Relatório:
```text
    1 - Proramadores Python
    2 - Funcionários a mais de 4 anos no mesmo cargo
    3 - Funcionários de até 23 anos
    4 - Lista de todos os funcionários ordenado por nome
    5 - Lista de todos os funcionários ordenado por tempo na mesma equipe
    6 - Lista de todos os funcionários ordenado por idade
    0 - Retornar ao menu inicial
```

Este relatório deve ser realizado e salvo e um arquivo. 

A lista dos itens 4 a 6 deverão ser criados através de um método recursivo.

