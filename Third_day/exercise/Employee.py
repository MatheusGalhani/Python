__author__ = "Matheus Galhani"


class Employee:
    def __init__(self, employee_id, nome, idade, cpf, equipe_atual, meses_na_equipe, feliz, linguagens):
        """
        Construtor da classe
        :param employee_id:
        :param nome:
        :param idade:
        :param cpf:
        :param equipe_atual:
        :param meses_na_equipe:
        :param feliz:
        :param linguagens:
        """
        self.employee_id = employee_id
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.equipe_atual = equipe_atual
        self.meses_na_equipe = meses_na_equipe
        self.feliz = feliz
        self.linguagens = linguagens

    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        self.idade = idade

    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_equipe_atual(self, equipe_atual):
        self.equipe_atual = equipe_atual

    def set_meses_na_equipe(self, meses_na_equipe):
        self.idade = meses_na_equipe

    def set_feliz(self, feliz):
        self.feliz = feliz

    def set_linguagens(self, linguagens):
        self.linguagens = linguagens

    def get_dados_extracao(self):
        """
        Retorna o dado do meu funcionário para gerar o relátorio
        :return:
        """
        return f"{self.employee_id};{self.nome};{self.idade};{self.cpf};{self.equipe_atual};{self.meses_na_equipe};{self.feliz};{self.linguagens};"

    def __str__(self):
        """
        Retorna uma mensagem de boas vindas
        :return:
        """
        return f"Seja bem-vindo {self.employee_id} - {self.nome}."
