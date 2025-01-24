class Parent:
    def __init__(self):
        print("I AM PARENT CLASS")
    def show(self):
        print("The owner is god")
class Child(Parent):
    def __init__(self):
        print("I AM CHILD CLASS")
        super().show()
        super().__init__()
        
c1 = Child()