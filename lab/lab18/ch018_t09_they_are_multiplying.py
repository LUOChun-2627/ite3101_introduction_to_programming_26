class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def description(self):
        print(self.name)
        print(self.age)


sloth = Animal("Sid", 4)
ocelot = Animal("Ozzy", 2)
print(hippo.health, sloth.health, ocelot.health)
