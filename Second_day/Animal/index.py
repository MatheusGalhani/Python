__author__ = "Matheus Galhani"

from Treinamento.Second_day.Animal.animal import Animal

if __name__ == '__main__':
    dog = Animal(name="Cachorro", paws=4, age=5)
    cat = Animal("Gato", 4)
    rabbit = Animal(name="Coelho", age=2)
    print(dog)
    print(cat)
    cat.set_age(4)
    print(cat)
    print(rabbit)
