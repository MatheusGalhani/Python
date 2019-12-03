__author__ = "Matheus Galhani"


class Animal:

    def __init__(self, name, paws=2, age=1):
        self.name = name
        self.paws = paws
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_paws(self, paws):
        self.paws = paws

    def set_age(self, age):
        self.age = age

    def __str__(self):
        return f'Meu animal é um {self.name}, ele tem {self.paws} pata(s) e tem {self.age} ano(s)'
