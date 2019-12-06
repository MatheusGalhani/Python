class Banco:
    def __init__(self, agencia, gerente):
        """
        Criando um construtor e inicializando as variaveis
        :param agencia:
        :param gerente:
        """
        self.agencia = agencia
        self.gerente = gerente

    def __str__(self):
        """
        Mensagem padrão da classe
        :return:
        """
        return f'Seja bem-vindo a agência {self.agencia}.'
