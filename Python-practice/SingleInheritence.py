class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print(f"The Animal Name is {self.name}")
        
class Dog(Animal):
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def __str__(self):
        return (f"The Dog Name Is {self.name}")
    def Sound(self):
        print(f"The Sound Of Dog IS {self.sound}")
class Cat(Animal):
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def __str__(self):
        return (f"The Cat Name Is {self.name}")
    def Sound(self):
        print (f"The Sound Of Cat IS {self.sound}")
    def Eat(self):
        print(f"Cat Favorite Food Is Milk ANd Rat")

a = Animal("Mahendra")
print(a)
a.sound()
b = Dog("Tomy","Bark")
print(b)
print(type(b))
b.Sound()
c = Cat("Munny","Meow")
print(c)
c.Sound()
c.Eat()