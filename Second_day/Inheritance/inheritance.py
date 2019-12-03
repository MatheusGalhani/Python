__author__ = "Matheus Galhani"


class People:
    def __init__(self, name=None, initials=None, age=0):
        self.name = name
        self.initials = initials
        self.age = age

    def __str__(self):
        return f'{self.name} ({self.initials}), {self.age} ano(s)'


class User(People):
    def __init__(self, email=None, name=None, initials=None, age=0):
        People.__init__(self, name=name, initials=initials, age=age)
        self.email = email

    def __str__(self):
        return f'Cadastro do usuário {People.__str__(self)} -> email: {self.email}'
