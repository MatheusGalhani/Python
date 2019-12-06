from Treinamento.Fourth_day.exercices.resolution1.utilitarios import game_number_recursivo, game_number_interacao, \
    seleciona_nome, dias_terra, dict_to_list, alunos_aprovados

if __name__ == "__main__":
    mensagem, contador = game_number_recursivo(10, 0)
    print(mensagem)
    print(game_number_interacao(10))
    print(seleciona_nome(["Matheus", "Pedro", "Julia", "Raul", "Gustavo"]))
    print(dias_terra("30/08/1996"))
    print(dict_to_list({"nome": "Matheus", "idade": 23}))
    print(alunos_aprovados({1: ["Matheus", 10], 2: ["Pedro", 6], 3: ["Jorge", 5.5], 4: ["Giba", 7.5]}))
