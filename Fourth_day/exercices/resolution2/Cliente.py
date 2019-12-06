from Treinamento.Fourth_day.exercices.resolution2.Banco import Banco
from datetime import datetime


class Cliente(Banco):
    def __init__(self, agencia, gerente, nome, nmr_conta, digito, idade, cpf, email, endereco, produtos, data_cadastro):
        """
        Criando um construtor e inicializando as variaveis
        :param agencia:
        :param gerente:
        :param nome:
        :param nmr_conta:
        :param digito:
        :param idade:
        :param cpf:
        :param email:
        :param endereco:
        :param produtos:
        :param data_cadastro:
        """
        Banco.__init__(self, agencia=agencia, gerente=gerente)
        self.nome = nome
        self.nmr_conta = nmr_conta
        self.digito = digito
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.endereco = endereco
        self.produtos = produtos
        self.data_cadastro = data_cadastro

    def __str__(self):
        """
        Mensagem padrão da classe
        :return:
        """
        return f"{Banco.__str__(self)} É um prazer sermos parceiros Sr(a). {self.nome}."

    def get_dados(self):
        """
        Retorna os dados para uso na extração
        :return:
        """
        # cadastrando uma variavel que vai pegar o valor Datetime e receber uma string
        cadastro = self.data_cadastro.strftime('%d/%m/%Y')
        return f"{self.gerente};{self.agencia};{self.nome};{self.nmr_conta};{self.digito};" \
            f"{self.idade};{self.cpf};{self.email};{self.endereco};{self.produtos};{cadastro};"

    def remover_produto(self, indice):
        """
        Remove o id do produto do usuário
        :param indice:
        :return:
        """
        try:
            self.produtos.__delitem__(indice)
        except IndexError:
            print("O ID do produto não existe")

    def adicionar_produto(self, novo_produto):
        """
        Adicionando um novo produto a minha lista
        :param novo_produto:
        :return:
        """
        self.produtos.append(novo_produto)

    def meses_cadastro(self):
        """
        Retorna a quantidade de meses
        :return:
        """
        day_string = datetime.now().strftime('%d/%m/%Y')
        data_fim = datetime.strptime(day_string, '%d/%m/%Y')
        data_inicio = self.data_cadastro
        # Calculo da quantidade de dias
        quantidade_dias = abs((data_fim - data_inicio).days)
        # Gerando quantidade em meses
        # utilizei o // para pegar o valor cheio da divisão.
        quantidade_meses = quantidade_dias // 30
        return quantidade_meses
