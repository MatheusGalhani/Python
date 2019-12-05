__author__ = "Matheus Galhani"

# importando a classe
from Treinamento.Third_day.exercise.Employee import Employee

# importando minhas funções
from Treinamento.Third_day.exercise.utilitario import write_file, read_file, get_lista_by_name, get_lista_by_idade, \
    get_lista_by_meses

if __name__ == '__main__':
    menu = """
    1 - Cadastrar Novo Funcionário
    2 - Alterar Dados do Funcionário
    3 - Gerar Relatório
    4 - Ler relatório
    0 - Sair
    Digite sua opção -> R: """
    menu_relatorio = """
    1 - Programadores Python
    2 - Funcionários a mais de 4 anos no mesmo cargo
    3 - Funcionários de até 23 anos
    4 - Lista de todos os funcionários ordenado por nome
    5 - Lista de todos os funcionários ordenado por tempo na mesma equipe
    6 - Lista de todos os funcionários ordenado por idade
    7 - (Extra) Backup
    0 - Retornar ao menu inicial
    Digite sua opção -> R: """
    employee_id = 1
    kwargs = {}
    option = int(input(menu))
    while option:
        if option == 1:
            print(f"Seu número de registro é {employee_id}")
            nome = input("Digite seu nome: R -> ")
            idade = int(input("Digite sua idade: R -> "))
            cpf = input("Digite seu cpf: ")
            equipe_atual = input("Digite sua equipe atual: R -> ")
            meses_na_equipe = int(input(f"Digite a quantidade de meses que você esta em {equipe_atual}: R -> "))
            feliz = input("Você está feliz na sua equipe? S - Sim/ N - Não: R -> ")
            linguagens = input("Digite as linguagens que você conhece separado por ,: R -> ").split(",")
            employee = Employee(employee_id=employee_id, nome=nome, idade=idade, cpf=cpf, equipe_atual=equipe_atual,
                                meses_na_equipe=meses_na_equipe, feliz=feliz, linguagens=linguagens)
            kwargs[employee_id] = employee
            employee_id += 1
            print("Dados salvos com sucesso.")
        elif option == 2:
            employee_id = int(input("Digite o Employee ID: R -> "))
            if employee_id in kwargs:
                instancia = kwargs[employee_id]
                nome = input("Digite seu novo nome: R -> ")
                idade = int(input("Digite sua nova idade: R -> "))
                cpf = input("Digite seu novo cpf: ")
                equipe_atual = input("Digite sua equipe atual: R -> ")
                meses_na_equipe = int(input(f"Digite a quantidade de meses que você esta em {equipe_atual}: R -> "))
                feliz = input("Você está feliz na sua equipe? S - Sim/ N - Não: R -> ")
                linguagens = input("Digite as linguagens que você conhece separado por ,: R -> ").split(",")
                instancia.set_nome(nome)
                instancia.set_idade(idade)
                instancia.set_cpf(cpf)
                instancia.set_equipe_atual(equipe_atual)
                instancia.set_meses_na_equipe(meses_na_equipe)
                instancia.set_feliz(feliz)
                instancia.set_linguagens(linguagens)
                print("Dados alterados com sucesso.")
            else:
                print(f"Funcionario {employee_id} não cadastrado")
        elif option == 3:
            opcao_relatorio = int(input(menu_relatorio))
            while opcao_relatorio:
                nome_arquivo = input("Digite o nome do seu arquivo para escrita: ")
                lista_relatorio = []
                if opcao_relatorio in (1, 2, 3, 7):
                    for key, instancia in kwargs.items():
                        if opcao_relatorio == 1 and 'Python' in instancia.linguagens:
                            lista_relatorio.append(instancia.get_dados_extracao())
                        elif opcao_relatorio == 2 and instancia.meses_na_equipe >= 48:
                            lista_relatorio.append(instancia.get_dados_extracao())
                        elif opcao_relatorio == 3 and instancia.idade <= 23:
                            lista_relatorio.append(instancia.get_dados_extracao())
                        elif opcao_relatorio == 7:
                            lista_relatorio.append(instancia.get_dados_extracao())
                elif opcao_relatorio == 4:
                    dicionario_ordenado = get_lista_by_name(kwargs)
                    for key, instancia in dicionario_ordenado.items():
                        lista_relatorio.append(instancia.get_dados_extracao())
                elif opcao_relatorio == 5:
                    dicionario_ordenado = get_lista_by_meses(kwargs)
                    for key, instancia in dicionario_ordenado.items():
                        lista_relatorio.append(instancia.get_dados_extracao())
                elif opcao_relatorio == 6:
                    dicionario_ordenado = get_lista_by_idade(kwargs)
                    for key, instancia in dicionario_ordenado.items():
                        lista_relatorio.append(instancia.get_dados_extracao())
                write_file(nome_arquivo, lista_relatorio)
                opcao_relatorio = int(input(menu_relatorio))
        elif option == 4:
            nome_arquivo = input("Digite o nome do seu arquivo para leitura: ")
            lista_funcionarios = read_file(nome_arquivo)
            for data in lista_funcionarios:
                # recuperando dados
                data_list = data.split(";")
                employee_id = int(data_list[0])
                nome = data_list[1]
                idade = int(data_list[2])
                cpf = data_list[3]
                equipe_atual = data_list[4]
                meses_na_equipe = int(data_list[5])
                feliz = data_list[6]
                linguagens = data_list[7].strip('[]').replace('"', '').replace("'", "").replace(' ', '').split(',')
                if employee_id not in kwargs:
                    employee = Employee(employee_id=employee_id, nome=nome, idade=idade, cpf=cpf,
                                        equipe_atual=equipe_atual, meses_na_equipe=meses_na_equipe, feliz=feliz,
                                        linguagens=linguagens)
                    kwargs[employee_id] = employee
                    print(f"O Funcionario {employee_id} - {nome} foi recadastrado no sistema.")
            # Populo a minha variavel com o tamanho de funcionarios da minha lista + 1
            employee_id = len(lista_funcionarios) + 1
        option = int(input(menu))
