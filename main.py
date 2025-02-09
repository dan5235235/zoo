import random

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = random.randint(1, 10)

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        return f"{self.name} поїв(ла). Рівень голоду: {self.hunger}"

    def __str__(self):
        return f"{self.species} {self.name} (Голод: {self.hunger})"


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        return f"{animal.name} тепер у {self.name}!"

    def feed_all(self):
        return [animal.eat() for animal in self.animals]

    def __str__(self):
        return f"Зоопарк {self.name} містить {len(self.animals)} тварин:\n" + \
               "\n".join(str(animal) for animal in self.animals)


zoo = Zoo("Дикий Світ")
a1 = Animal("Лев", "Лев")
a2 = Animal("Зося", "Зебра")
a3 = Animal("Рік", "Жираф")

print(zoo.add_animal(a1))
print(zoo.add_animal(a2))
print(zoo.add_animal(a3))

print(zoo)

print("\nГодуємо тварин...")
for message in zoo.feed_all():
    print(message)

print("\nСтан після годування:")
print(zoo)