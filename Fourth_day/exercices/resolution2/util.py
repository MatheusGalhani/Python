from random import randint


def get_cabecalho():
    return "Gerente;Agencia;Nome;Nmr_Conta;Digito;" \
           "Idade;CPF;Email;Endereco;Produto;Cadastro;"


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


def conta_automatica(kwargs):
    """
    Cria uma conta para meu cliente
    :param kwargs:
    :return:
    """
    digito = randint(0, 9)
    numero_conta = randint(10000, 99999)
    nova_chave = f"{numero_conta}-{digito}"
    while nova_chave in kwargs:
        numero_conta = randint(10000, 99999)
        nova_chave = f"{numero_conta}-{digito}"
    return nova_chave, numero_conta, digito
