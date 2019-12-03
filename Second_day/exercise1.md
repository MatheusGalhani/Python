# DXC - Python 2º dia
Crie uma classe para um cliente da DXC Technology. Nesta cadastro deverá ser armazenados os seguintes campos:
* ID (inteiro)
* Nome do cliente (string)
* CPF/CNPJ (string)
* Produtos desejados (lista)
* Email (string)

### Help Produtos desejados
```python
lista_string = input("") # usuario deverá digitar 1,2,3...
minha_lista = lista_string.split(",") # transforma a string em lista, separando por virgula
```

Lembrando que CPF deverá ser usado em uma classe de pessoa física e CNPJ em uma classe de pessoa juridíca.

A classe de clientes deverá ter métodos para alterar os paramêtros cadastrados inicialmente, alem de possuir um método exibindo uma mensagem de quantos produtos o cliente contratou da DXC.

O método de exibição da quantidade de produtos deverá retornar a seguinte mensage.

```text
    O cliente NOME_CLIENTE tem X produtos desejados.
```

Para validar a quantidades de produtos, pode-se utilizar a função 
```python
minha_lista = [1, 2, 3]
len(minha_lista)
```

Crie também um método de exibição do cliente, que deverá retornar o seguinte texto

```text
    ID: ID_CLIENTE -> Nome: NOME_CLIENTE. Produtos desejados: PRODUTOS_DESEJADO
```

Prints que deverão ser utilizados:

```python
    meu_objeto = MinhaClasse(id=1, nome="Nome", CPF="12396547821", produtos=[1,2,3], email="teste@teste.com")
    print(meu_objeto.metodo_exibe_cliente())
    meu_objeto.novo_nome("Nome Novo")
    print(meu_objeto.metodo_exibe_cliente())
    print(meu_objeto.metodo_qtd_produtos())
```