class Animal:
    def __init__(self, name, mass):
        self.name = name 
        self.mass = mass
    
    def move(self, count):
        print(f"{count} {self.name} going")
    
    def jump(self,):
        print(f"it is jumping its mass is {self.mass} ")

class vegan_animal(Animal):
    
    def __init__(self, name, mass, methan):
        self.methan = methan
        self.name = name 
        self.mass = mass
    


        def eat_grass(self):
            print(f"{self.name} is eating grass")
        
        def move (self, count):
            print(f"{count} {self.name} is walk")



animal1 = Animal("cat", 900)
animal1.move(count = 1)
animal1.jump()


vegan_animal1 = vegan_animal ('cow', 100, 900)

vegan_animal1.eat_grass()
vegan_animal1.move (3)