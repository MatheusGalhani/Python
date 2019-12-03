__author__ = "Matheus Galhani"


def validacao(idade, cpf, email, semestre_atual, qtd_semestre_total):
    """
        Este método serve para validar se posso cadastrar meu usuário
    """
    if idade < 18 or (
            semestre_atual + 2) >= qtd_semestre_total or "@" not in email or ".com" not in email.lower() or len(
        cpf) != 11 or cpf in (
            '11111111111', '22222222222', '33333333333', '44444444444', '55555555555', '66666666666', '77777777777',
            '88888888888',
            '99999999999', '00000000000') or cpf.__contains__("1234567"):
        return False
    return True


def chave(idade, nome, semestre_atual, qtd_semestre_total, linguagem):
    """
        Este método serve para validar a chave
    """
    if 18 <= idade <= 20 and nome == nome[::-1] or semestre_atual <= (qtd_semestre_total / 2):
        return "A"
    elif idade > 25 and semestre_atual >= (qtd_semestre_total / 2) and linguagem.lower() == 'python':
        return "B"
    else:
        return "C"


if __name__ == '__main__':
    option = 1
    candidatos = []
    while option:
        nome = input("Qual seu nome? -> R: ")
        idade = int(input("Qual sua idade? -> R: "))
        cpf = input("Qual seu cpf? -> R: ")
        email = input("Qual seu e-mail? -> R: ")
        faculdade_curso = input("Qual sua Faculdade/Curso? -> R: ")
        semestre_atual = int(input("Qual seu semestre atual? -> R: "))
        qtd_semestre_total = int(input("Qual a quantidade de semestres da faculdade? -> R: "))
        linguagem = input("Qual sua linguagem favorita? -> R: ")
        if validacao(idade=idade, cpf=cpf, email=email, semestre_atual=semestre_atual,
                     qtd_semestre_total=qtd_semestre_total):
            chave = chave(idade=idade, nome=nome, semestre_atual=semestre_atual,
                          qtd_semestre_total=qtd_semestre_total, linguagem=linguagem)
            novo_candidato = {'nome': nome, 'idade': idade, 'cpf': cpf, 'email': email,
                              'faculdade_curso': faculdade_curso, 'semestre_atual': semestre_atual,
                              'qtd_semestre_total': qtd_semestre_total, 'linguagem': linguagem, 'chave': chave}
            candidatos.append(novo_candidato)
            print("Cadastro Realizado")
        else:
            print('Você não está apto a se candidatar.')
        option = int(input('1 - Cadastrar Novo Integrante\n0 - Finalizar cadastros\nR: '))
    option = int(input('1 - Chave A\n2 - Chave B\n3 - Chave C\n0 - Sair do programa\nR: '))
    while option:
        for candidato in candidatos:
            nome = candidato['nome']
            idade = candidato['idade']
            faculdade_curso = candidato['faculdade_curso']
            linguagem = candidato['linguagem']
            if option == 1 and candidato['chave'] == "A":
                print(f'Candidato {nome} de {idade}, cursando {faculdade_curso}, gosta de programar em {linguagem}')
            elif option == 2 and candidato['chave'] == "B":
                print(f'Candidato {nome} de {idade}, cursando {faculdade_curso}, gosta de programar em {linguagem}')
            elif option == 3 and candidato['chave'] == "C":
                print(f'Candidato {nome} de {idade}, cursando {faculdade_curso}, gosta de programar em {linguagem}')
        option = int(input('1 - Chave A\n2 - Chave B\n3 - Chave C\n0 - Sair do programa\nR: '))
