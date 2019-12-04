__author__ = "Matheus Galhani"

from Treinamento.Second_day.exercise.Cliente import Cliente

if __name__ == '__main__':
    cliente_id = int(input("Digite o id do cliente: "))
    name = input("Digite o nome do cliente: ")
    documento = input("Digite o CPF/CNPJ do cliente: ")
    email = input("Digite o email do cliente: ")
    produtos = input("Digite os produtos desejados separados por virgula: ").split(",")
    cliente = Cliente(cliente_id=cliente_id, name=name, documento=documento, produtos=produtos, email=email)
    print(cliente)
    print(cliente.get_documento())
    print(cliente.get_qtd_produtos())
