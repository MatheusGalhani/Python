class PessoaFisica:
    def __init__(self, cpf):
        self.cpf = cpf

    def set_cpf(self, cpf):
        self.cpf = cpf

    def __str__(self):
        return f'CPF: {self.cpf}'


class PessoaJuridica:
    def __init__(self, cnpj):
        self.cnpj = cnpj

    def set_cnpj(self, cnpj):
        self.cnpj = cnpj

    def __str__(self):
        return f'CNPJ: {self.cnpj}'


class Cliente(PessoaFisica, PessoaJuridica):
    def __init__(self, cliente_id, name, documento, produtos, email):
        self.documento = documento
        if len(documento) == 11:
            PessoaFisica.__init__(self, cpf=documento)
        else:
            PessoaJuridica.__init__(self, cnpj=documento)
        self.cliente_id = cliente_id
        self.name = name
        self.produtos = produtos
        self.email = email

    def __str__(self):
        return f'ID: {self.cliente_id} -> Nome: {self.name}. Produtos desejados: {self.produtos}.'

    def set_name(self, name):
        self.name = name

    def set_cliente_id(self, cliente_id):
        self.cliente_id = cliente_id

    def set_produtos(self, produtos):
        self.produtos = produtos

    def set_email(self, email):
        self.email = email

    def get_documento(self):
        if len(self.documento) == 11:
            return PessoaFisica.__str__(self)
        else:
            return PessoaJuridica.__str__(self)

    def get_qtd_produtos(self):
        quantidade = len(self.produtos)
        return f'O cliente {self.name} tem {quantidade} produtos desejados.'

    def set_documento(self, documento):
        self.documento = documento
        if len(documento) == 11:
            self.set_cpf(documento)
        else:
            self.set_cnpj(documento)
