__author__ = "Matheus Galhani"


def find_new_employees(kwargs):
    """
    This function returns 4 lists to save to a file.
    :param kwargs: -> List of dictations with employee data.
    :return:
    """
    devs = []
    testers = []
    young = []
    old = []
    for employee in kwargs:
        if employee['Dev']:
            devs.append(employee)
        else:
            testers.append(employee)

        if employee['age'] <= 25:
            young.append(employee)
        else:
            old.append(employee)
    return devs, testers, young, old


def write_file(name_file, kwargs):
    file = open(name_file, 'w')
    try:
        for data in kwargs:
            name = data['name']
            age = data['age']
            nickname = data['nickname']
            function_employee = 'Developer' if data['Dev'] else 'Tester'
            file.write(f'{name} é um {function_employee}, chamado de {nickname}, {age} anos.\n')
    except:
        print(f'Erro ao gerar o arquivo {name_file}')
    finally:
        file.close()


def read_file(name_file):
    try:
        file = open(name_file, 'r')
        file_content = list(file)
        for data in file_content:
            print(data)
        file.close()
    except FileNotFoundError:
        print(f'O arquivo {name_file} que foi informado não existe')
    except Exception as e:
        print('Erro desconhecido!')
        print(e)


if __name__ == '__main__':
    dataset = [{'name': 'Matheus Galhani', 'age': 23, 'nickname': 'Galhani', 'Dev': True},
               {'name': 'Pedro Arthur', 'age': 30, 'nickname': 'Pedrin', 'Dev': False},
               {'name': 'Amanda Santos', 'age': 18, 'nickname': 'Amandinha', 'Dev': True},
               {'name': 'Henrique Lupo', 'age': 17, 'nickname': 'Rico', 'Dev': True},
               {'name': 'Barbara Simões', 'age': 22, 'nickname': 'Babi', 'Dev': True},
               {'name': 'Diego Porto', 'age': 35, 'nickname': 'DuPorto', 'Dev': False},
               {'name': 'Mauricio Gimenez', 'age': 19, 'nickname': 'Boy', 'Dev': True},
               {'name': 'João Paulo', 'age': 23, 'nickname': 'JP', 'Dev': True},
               {'name': 'Caio Menezes', 'age': 22, 'nickname': 'Menor', 'Dev': True},
               {'name': 'Julio Cesar', 'age': 24, 'nickname': 'Romano', 'Dev': True},
               {'name': 'Robson Cruz', 'age': 21, 'nickname': 'Robinho', 'Dev': False},
               {'name': 'Manuela Domeniconi', 'age': 13, 'nickname': 'MD', 'Dev': True},
               {'name': 'Pietro Rodrigues', 'age': 36, 'nickname': 'Pet', 'Dev': True},
               {'name': 'Ricardo Junior', 'age': 17, 'nickname': 'RJ', 'Dev': False},
               {'name': 'Bruno Assunção', 'age': 24, 'nickname': 'Bruninho', 'Dev': False},
               {'name': 'Sabrina Mello', 'age': 20, 'nickname': 'Sasa', 'Dev': True},
               {'name': 'Hugo Martins', 'age': 25, 'nickname': 'Soneca', 'Dev': False},
               {'name': 'Michel Mello', 'age': 29, 'nickname': 'M.M', 'Dev': True}]
    new_devs, new_testers, young_employees, old_employees = find_new_employees(dataset)
    # write_file('Devs.txt', new_devs)
    # write_file('Testers.txt', new_testers)
    # write_file('Young_employees.txt', young_employees)
    # write_file('Old_employees.txt', old_employees)
    # read_file('Devs.txt')
    # read_file('Old_employees.txt')
