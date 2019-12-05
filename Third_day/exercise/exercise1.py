__author__ = "Matheus Galhani"

# importando a classe
from Treinamento.Third_day.exercise.Employee import Employee

if __name__ == '__main__':
    employee_id = 1
    nome = input("Digite seu nome: R -> ")
    idade = int(input("Digite sua idade: R -> "))
    cpf = input("Digite seu cpf: ")
    equipe_atual = input("Digite sua equipe atual: R -> ")
    meses_na_equipe = int(input(f"Digite a quantidade de meses que você esta em {equipe_atual}: R -> "))
    feliz = input("Você está feliz na sua equipe? S - Sim/ N - Não: R -> ")
    linguagens = input("Digite as linguagens que você conhece separado por ,: R -> ").split(",")
    employee = Employee(employee_id=employee_id, nome=nome, idade=idade, cpf=cpf, equipe_atual=equipe_atual,
                        meses_na_equipe=meses_na_equipe, feliz=feliz, linguagens=linguagens)
