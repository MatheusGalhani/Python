__author__ = "Matheus Galhani"

from Treinamento.Second_day.exercise.Cliente import Cliente

if __name__ == '__main__':
    menu = """
    1 - Cadastrar Novo Cliente
    2 - Alterar Dados do Cliente
    3 - Exibir quantidade de produtos contratados pelo cliente
    0 - Sair
    Digite sua opção -> R: """
    opcao = int(input(menu))
    kwargs = {}
    while opcao:
        if opcao == 1:
            cliente_id = int(input("Digite o id do cliente: "))
            name = input("Digite o nome do cliente: ")
            documento = input("Digite o CPF/CNPJ do cliente: ")
            email = input("Digite o email do cliente: ")
            produtos = input("Digite os produtos desejados separados por virgula: ").split(",")
            cliente = Cliente(cliente_id=cliente_id, name=name, documento=documento, produtos=produtos,
                              email=email)
            kwargs[cliente_id] = cliente
        elif opcao == 2:
            cliente_id = int(input("Digite o id do cliente: "))
            if cliente_id in kwargs:
                name = input("Digite o novo nome do cliente: ")
                documento = input("Digite o novo CPF/CNPJ do cliente: ")
                email = input("Digite o novo email do cliente: ")
                produtos = input("Digite os novos produtos desejados separados por virgula: ").split(",")
                instancia_cliente = kwargs[cliente_id]
                instancia_cliente.set_name(name)
                instancia_cliente.set_documento(documento)
                instancia_cliente.set_email(email)
                instancia_cliente.set_produtos(produtos)
            else:
                print(f"O cliente {cliente_id} ainda não foi cadastrado")
        elif opcao == 3:
            cliente_id = int(input("Digite o id do cliente: "))
            if cliente_id in kwargs:
                instancia_cliente = kwargs[cliente_id]
                print(instancia_cliente.get_qtd_produtos())
            else:
                print(f"O cliente {cliente_id} ainda não foi cadastrado")

        opcao = int(input(menu))
