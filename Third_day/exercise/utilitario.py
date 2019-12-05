__author__ = "Matheus Galhani"


def get_cabecalho():
    """
    Retorna o cabeçalho.
    :return:
    """
    return "Employee ID;Nome do funcionário;Idade;CPF;Equipe atual" \
           ";Meses nesta equipe;Feliz na equipe;Linguagens conhecidas;"


def write_file(name_file, kwargs):
    """
    Escreve um arquivo com os dados recebidos, o qual é uma lista de registros
    :param name_file:
    :param kwargs:
    :return:
    """
    file = open(name_file, 'w')
    try:
        file.write(f'{get_cabecalho()}\n')
        for data in kwargs:
            file.write(f'{data}\n')
    except Exception as e:
        print(f'Erro ao gerar o arquivo {name_file}')
        print(e)
    finally:
        file.close()


def read_file(name_file):
    """
    Le um arquivo e retorna a lista de dados
    :param name_file:
    :return:
    """
    file_content = []
    try:
        file = open(name_file, 'r')
        file_content = list(file)
        # Remove o cabeçalho
        file_content.__delitem__(0)
        file.close()
    except FileNotFoundError:
        print(f'O arquivo {name_file} que foi informado não existe')
    except Exception as e:
        print('Erro desconhecido!')
        print(e)

    return file_content


def get_lista_by_name(kwargs):
    """
    Retorna uma dicionario ordenada por nomes
    :param kwargs:
    :return:
    """
    new_lista = []
    for employee_id, instancia in kwargs.items():
        new_lista.append(f"{instancia.nome};{instancia.employee_id}")
    # A função sorted ordena uma lista
    lista_ordenada = sorted(new_lista)
    new_dict = {}
    for dados in lista_ordenada:
        """
            Como cadastrei nome;id para que fosse ordenado por nome
            vou splitar para criar uma lista, onde a posição 
            0 será o nome, e 1 será o employee_id
        """
        lista_valores = dados.split(";")
        employee_id = int(lista_valores[1])
        """
            Recupero o meu objeto (Employee) e armazeno no meu dicionário.
            Assim estou fazendo uma cópia do meu dicionário ordenado por nomes.
        """
        new_dict[employee_id] = kwargs[employee_id]
        """
            Uma curiosidade é que mesmo o new_dict tendo as chaves em posições 
            diferente de kwargs
            new_dict = {10: Employee_10, 9: Employee_9, 11: Employee_11}
            kwargs = {9: Employee_9, 10: Employee_10, 11: Employee_11}
            
            Se eu fosse comparar ele (new_dict == kwargs) isso seria True, pois
            ambos possuem as mesmas CHAVES E VALORES
        """
    return new_dict


def get_lista_by_meses(kwargs):
    """
    Retorna uma dicionario ordenada por meses
    :param kwargs:
    :return:
    """
    new_lista = []
    for employee_id, instancia in kwargs.items():
        new_lista.append(f"{instancia.meses_na_equipe};{instancia.employee_id}")
    lista_ordenada = sorted(new_lista)
    new_dict = {}
    for dados in lista_ordenada:
        lista_valores = dados.split(";")
        employee_id = int(lista_valores[1])
        new_dict[employee_id] = kwargs[employee_id]
    return new_dict


def get_lista_by_idade(kwargs):
    """
    Retorna uma dicionario ordenada por idade
    :param kwargs:
    :return:
    """
    new_lista = []
    for employee_id, instancia in kwargs.items():
        new_lista.append(f"{instancia.idade};{instancia.employee_id}")
    lista_ordenada = sorted(new_lista)
    new_dict = {}
    for dados in lista_ordenada:
        lista_valores = dados.split(";")
        employee_id = int(lista_valores[1])
        new_dict[employee_id] = kwargs[employee_id]
    return new_dict
