__author__ = "Matheus Galhani"

# importando a classe
from Treinamento.Fourth_day.exercices.resolution2.Cliente import Cliente

# importando minhas funções
from Treinamento.Fourth_day.exercices.resolution2.util import write_file, conta_automatica, read_file

# importando pacote de data
from datetime import datetime

if __name__ == "__main__":
    menu_inicial = """
    1 - Cadastrar Novo cliente
    2 - Alterar Endereço do cliente
    3 - Contratar novo produto do banco
    4 - Cancelar produto do banco
    5 - Gerar um arquivo de Backup dos dados do banco
    6 - Ler o arquivo de Backup e recadastrar os dados
    7 - Relatório dos clientes que possuem 10 meses cadastrados
    8 - Relatório de todos os clientes de 18 até 25 anos
    0 - Sair
    Digite sua opção -> R: """
    busca_cliente = "Digite sua conta-digito R: "
    opcao = int(input(menu_inicial))
    kwarg_cliente = {}
    while opcao:
        if opcao == 1:
            agencia = int(input("Digite o código da agencia R: "))
            gerente = input("Digite o nome do gerente R: ")
            nome = input("Digite o seu nome R: ")
            nova_chave, numero_conta, digito = conta_automatica(kwarg_cliente)
            idade = int(input("Digite a sua idade R: "))
            cpf = input("Digite o seu cpf R: ")
            email = input("Digite o seu email R: ")
            endereco = input("Digite o seu endereço R: ")
            produtos = input("Digite o seu a lista de produtos contratados separados por , R: ")
            lista_produtos = produtos.split(",") if produtos else []
            data_cadastro = datetime.now()
            cliente = Cliente(agencia=agencia, gerente=gerente, nome=nome, nmr_conta=numero_conta,
                              digito=digito, idade=idade, cpf=cpf, email=email, endereco=endereco,
                              produtos=lista_produtos, data_cadastro=data_cadastro)
            kwarg_cliente[nova_chave] = cliente
            print(f"{cliente}")
        elif opcao == 2:
            conta = input(busca_cliente)
            if conta in kwarg_cliente:
                instancia_cliente = kwarg_cliente[conta]
                instancia_cliente.endereco = input("Digite seu novo endereço")
        elif opcao == 3:
            conta = input(busca_cliente)
            if conta in kwarg_cliente:
                instancia_cliente = kwarg_cliente[conta]
                new_produto = input("Digite o nome do produto desejado R:")
                instancia_cliente.adicionar_produto(new_produto)
        elif opcao == 4:
            conta = input(busca_cliente)
            if conta in kwarg_cliente:
                instancia_cliente = kwarg_cliente[conta]
                if instancia_cliente.produtos:
                    for indice in range(len(instancia_cliente.produtos)):
                        print(f"{indice} - {instancia_cliente.produtos[indice]}")
                    id_produto = int(input("Digite o id do produto para remover R:"))
                    instancia_cliente.remover_produto(id_produto)
                else:
                    print("Você ainda não possui um produto")
        elif opcao == 5:
            lista_relatorio = []
            for k, instancia_cliente in kwarg_cliente.items():
                lista_relatorio.append(instancia_cliente.get_dados())
            nome_arquivo = input("Digite o nome do seu arquivo para escrita: ")
            write_file(nome_arquivo, lista_relatorio)
        elif opcao == 6:
            nome_arquivo = input("Digite o nome do seu arquivo para leitura: ")
            lista_funcionarios = read_file(nome_arquivo)
            for data in lista_funcionarios:
                # recuperando dados
                data_list = data.split(";")
                gerente = data_list[0]
                agencia = int(data_list[1])
                nome = data_list[2]
                nmr_conta = int(data_list[3])
                digito = int(data_list[4])
                idade = int(data_list[5])
                cpf = data_list[6]
                email = data_list[7]
                endereco = data_list[8]
                produtos = data_list[9].strip('[]').replace('"', '').replace("'", "").replace(' ', '').split(',')
                data_cadastro = datetime.strptime(data_list[10], '%d/%m/%Y')
                nova_chave = f"{nmr_conta}-{digito}"
                if nova_chave not in kwarg_cliente:
                    cliente = Cliente(agencia=agencia, gerente=gerente, nome=nome,
                                      nmr_conta=nmr_conta, digito=digito, idade=idade, cpf=cpf,
                                      email=email, endereco=endereco, produtos=produtos,
                                      data_cadastro=data_cadastro)
                    kwarg_cliente[nova_chave] = cliente
                    print(f"{cliente}")
        elif opcao == 7:
            lista_relatorio = []
            for key, instancia_cliente in kwarg_cliente.items():
                if instancia_cliente.meses_cadastro() >= 10:
                    lista_relatorio.append(instancia_cliente.get_dados())
            nome_arquivo = input("Digite o nome do seu arquivo para escrita: ")
            write_file(nome_arquivo, lista_relatorio)
        elif opcao == 8:
            lista_relatorio = []
            for key, instancia_cliente in kwarg_cliente.items():
                if 18 <= instancia_cliente.idade <= 25:
                    lista_relatorio.append(instancia_cliente.get_dados())
            nome_arquivo = input("Digite o nome do seu arquivo para escrita: ")
            write_file(nome_arquivo, lista_relatorio)

        opcao = int(input(menu_inicial))
