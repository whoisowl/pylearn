class Animal():
    zoo_name = "Tehran Zoo"

    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

    def info(self):
        print(f"{self.zoo_name}, name: {self.name}, species: {self.species}, age: {self.age}")

    def __str__(self):
        return f"{self.name} ({self.species}), age: {self.age}"


class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"the {self.name} tweets and flaps its {self.wing_span}cm wings")


leo = Animal("leo", "lion", 5, "roar")
leo.make_sound()
leo.info()
print(leo)

parrot = Bird("polly", "parrot", 2, "squawk", 30)
parrot.make_sound()
parrot.info()
print(parrot)