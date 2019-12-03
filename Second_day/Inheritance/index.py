__author__ = "Matheus Galhani"

from Treinamento.Second_day.Inheritance.inheritance import User

if __name__ == '__main__':
    email = "matheus.galhani@dxc.com"  # input("Digite seu email: ")
    name = "Matheus Galhani"  # input("Digite seu nome: ")
    initials = "MG"  # input("Digite suas iniciais: ")
    age = 23  # int(input("Digite sua idade: "))
    user = User(email=email, name=name, initials=initials, age=age)
    print(user)
