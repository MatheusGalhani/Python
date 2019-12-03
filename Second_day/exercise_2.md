

# DXC - Python 2º dia
Com o programa que você criou, gere um programa interativo que receberá dados de clientes da DXC Technology através do menu interativo abaixo. 

O cadastro acima deverá ser feito através uma classe e o objeto deverá ser armazenado em um dicionário, cujo a chave será o ID. 

### Exemplo
```python
kwargs = {} # iniciando meu dicionario vazio
while ?:
    id = int(input("XXX"))
    nome = input("XXX")
    cpf = input("XXX")
    produtos = input("XXX")
    email = input("XXX")
    meu_objeto = MinhaClasse(id=id, nome=nome, CPF="12396547821", produtos=produtos, email=email)
    kwargs[id] = meu_objeto # adicionando a chave (valor de id) e colocando seu objeto

###### Alterar um dado
id_desejado = int(input("XXX"))

if id_desejado in kwargs: # validando se aquele id está cadastrado no dicionario
    objeto_cadastrado = kwargs[id_desejado] # recuperando o valor do objeto no dicionario, a partir da minha chave
    # objeto_cadastrado será do tipo MinhaClasse, tendo qualquer método criaod nele

```

### Menu de cadastro
```text
    1 - Cadastrar Novo Cliente
    2 - Alterar Dados do Cliente
    3 - Exibir quantidade de produtos contratados pelo cliente
    0 - Sair
```



