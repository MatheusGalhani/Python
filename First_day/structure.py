__author__ = "Matheus Galhani"


def input_method():
    """
        Este método serve para apresentar como se utiliza métodos de entradas
    """
    name = input("Qual seu nome? -> R: ")
    quest = input("Qual é sua dúvida? -> R: ")
    color = input("Qual sua cor favorita? -> R: ")
    # https://docs.python.org/2.4/lib/typesseq-strings.html

    print("O " + name + " perguntou " + quest + ", e sua cor favorita é " + color + ".")

    print("O %s perguntou %s, "
          "e sua cor favorita é %s." % (name, quest, color))

    print("Outra maneira. O {} perguntou {},"
          " e sua cor favorita é {}.".format(name, quest, color))
    print(f"Outra maneira. O {name} perguntou {quest}, e sua cor favorita é {color}.")


def strings():
    """
        Este método serve para apresentar como se utiliza métodos de validações
    """
    text1 = 'Um texto'
    text2 = "Um texto"
    text3 = """Um texto"""
    print(text1)
    print(text2)
    print(text3)
    print(text1[::-1])  # Inverter uma String
    print(text1[:-1])  # Ignorar último caracter
    print(text1[2:])  # Ler da 2ª posição para frente
    print(text1[3:7])  # Ler da 3 a 7 posição
    print(text1.upper())
    print(text1.lower())


def condition():
    """
        Este método serve para apresentar como se utiliza métodos de validações
    """
    matheus = 1.74
    gustavo = 1.85

    if matheus > gustavo:
        print("Matheus é maior que Gustavo")
    elif matheus == gustavo:
        print("Matheus e Gustavo tem a mesma altura")
    else:
        print("Matheus é menor que Gustavo")

    print("#".ljust(80, '#'))
    boolean = True
    number = 1
    string = "Content"

    string2 = ""
    string3 = None
    number2 = 0
    if boolean:
        print("Ok bolean")
    if number:
        print("Ok number")
    if number2:
        print("Ok number2?")
    if string:
        print("Ok string")
    if string2:
        print("Ok string2")
    if string3:
        print("Ok string3")

    print(len(string2))  # Quantidade de caracteres


def for_method():
    """
        Este método serve para apresentar como se utiliza laços de repetições
    """
    min_value = 2
    max_value = 5
    for i in range(max_value):
        print(i)
    print("#".ljust(80, '#'))
    for i in range(min_value, max_value):
        print(i)
    print("#".ljust(80, '#'))
    i = 0
    while i < max_value:
        print(i)
        i += 1


def list_method():
    """
        Este método serve para apresentar como se utiliza lista/array
    """
    names = ['Matheus Galhani', 'Rodrigo Picchi', 'Ana Claudia']
    print("#".ljust(80, '#'))
    print("Exibição com for object")
    for name in names:
        print('Participante %s' % name)
    print("#".ljust(80, '#'))
    print("Exibição com with")
    i = 0
    while i != len(names):
        print('Participante %s' % names[i])
        i += 1
    print("#".ljust(80, '#'))


def dictionary():
    """
        Este método serve para apresentar como se utiliza dicionario
    """
    kwargs = {'Name': 'Matheus Galhani', 'Favorite_Language': 'Python'}
    print(kwargs.keys())
    print(kwargs.items())
    print('O %s gosta de programar em %s.' % (kwargs['Name'], kwargs['Favorite_Language']))
    print("#".ljust(80, '#'))
    for key in kwargs.keys():
        print('%s: %s' % (key, kwargs[key]))
    print("#".ljust(80, '#'))
    for key, value in kwargs.items():
        print('%s: %s' % (key, value))


def lambda_method():
    """
        Este método serve para apresentar como se utiliza lambda
    """

    def multiplication_difficult(x):
        """
        :param x: -> Numero para calculo
        :return: -> Retorna o dobro do numero x
        """
        return x * 2

    print(multiplication_difficult(6))
    print("#".ljust(80, '#'))
    multiplication = lambda x: x * 2
    print(multiplication(6))
    print("#".ljust(80, '#'))
    full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
    print(full_name('guido', 'van rossum'))


def for_comprehension():
    """
        Este método serve para apresentar como se utiliza um for de forma comprimida
    """
    kwargs = {'MatheusGalhani': 23, 'GuilhermeSantos': 24, 'MariaRita': 18, 'MartaSilva': 20, 'MarceloCruz': 25,
              'BrunaAguiar': 21, 'PedroGomes': 19, 'RicardoCorreia': 22, 'BrunoAssunção': 20}

    lista_nomes = [k for k, v in kwargs.items() if v > 20]
    print(f'Lista de usuários 20+: {lista_nomes}')


def parameters(name, lastname, age=1):
    """
        Este método serve para apresentar como se utiliza uma função com parametros
        e seus valroes default
    """
    print(f'Seja bem vindo(a) {lastname}, {name}. Idade: {age} ano(s)')


if __name__ == '__main__':
    # input_method()
    # strings()
    # condition()
    # for_method()
    # list_method()
    # dictionary()
    # lambda_method()
    # for_comprehension()
    parameters('Matheus', 'Galhani', 23)
    parameters('Nayara', 'Cristina')
    parameters(lastname='Pedro', name='Gomes', age=33)
