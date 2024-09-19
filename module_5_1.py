# Модуль 5.1
# "Атрибуты и методы объекта."
# Задача "Developer - не только разработчик"

class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor >= 1 and new_floor <= number_of_floors:
            print("Тек. этаж:", i)
            i += 1
        else:
            print("Такого этажа не существует")
for i in range(1, new_floor+1)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
