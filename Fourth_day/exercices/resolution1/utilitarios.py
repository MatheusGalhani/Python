__author__ = "Matheus Galhani"

from random import randint
from datetime import datetime


def game_number_recursivo(numero, qtd_execucao):
    """

    :param numero: Número inputado pelo usuário
    :param qtd_execucao: Quantidade de execuções
    :return:
    """
    numero_aleatorio = randint(1, 20)
    if numero_aleatorio != numero:
        qtd_execucao += 1
        mensagem, qtd_execucao = game_number_recursivo(numero, qtd_execucao)
    return f"Você precisou de {qtd_execucao} tentativas para acertar o número aleatório", qtd_execucao


def game_number_interacao(numero):
    """

    :param numero: Número inputado pelo usuário
    :return:
    """
    qtd_execucao = 0
    numero_aleatorio = 0
    while numero_aleatorio != numero:
        numero_aleatorio = randint(1, 20)
        qtd_execucao += 1
    return f"Você precisou de {qtd_execucao} tentativas para acertar o número aleatório"


def seleciona_nome(lista_nomes):
    """
    Retorna 3 nomes da lista
    :param lista_nomes:
    :return:
    """
    lista_sortidos = []
    lista_indice = []
    maximo = len(lista_nomes) - 1
    while len(lista_sortidos) != 3:
        numero_aleatorio = randint(0, maximo)
        if numero_aleatorio not in lista_indice:
            lista_indice.append(numero_aleatorio)
            lista_sortidos.append(lista_nomes[numero_aleatorio])
    return lista_sortidos


def dias_terra(data_aniversario_string):
    """
    Calcula quantidade de dias
    :param data_aniversario_string:
    :return:
    """
    # Data inicial
    data_inicio = datetime.strptime(data_aniversario_string, '%d/%m/%Y')

    # Data final
    day_string = datetime.now().strftime('%d/%m/%Y')
    print(f'Hoje é dia {day_string}')
    # Transforma uma string em datetime
    data_fim = datetime.strptime(day_string, '%d/%m/%Y')

    # Calculo da quantidade de dias
    quantidade_dias = abs((data_fim - data_inicio).days)
    return f"Você tem {quantidade_dias} dias na terra."


def dict_to_list(kwargs):
    """
    Transforma um dicionario em lista [[chave, valor], [chave, valor]]
    :param kwargs:
    :return:
    """
    lista = []
    for k, v in kwargs.items():
        lista.append([k, v])
    return lista


def alunos_aprovados(kwargs):
    """
    Retorna dicionario de alunos aprovados
    :param kwargs:
    :return:
    """
    new_kwargs = {}
    for key, value in kwargs.items():
        if value[1] >= 6:
            new_kwargs[key] = value
    return new_kwargs
