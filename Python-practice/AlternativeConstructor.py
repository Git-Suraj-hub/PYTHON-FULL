class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def convert(cls, c):
        name, age = c.split("-")
        return cls(name, int(age))
        
    def show(self):
        print(f"The student name is {self.name} and he/she is {self.age} years old")

s1 = Student("suraj", 19)
s1.show()
s2 = Student.convert("Manish-18")
s2.show()
