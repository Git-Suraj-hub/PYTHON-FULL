class Student:
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo
    def ShowDetails(self):
        print(f"the student Name is {self.name} and MUR is {self.rollNo}")

class Programmer(Student):
     def __init__(self, name, rollNo):
        super().__init__(name, rollNo)
        print(f"The Favorite Language is Python ")
s1 = Programmer("SURAJ SINGH MEHTA","MUR2300415")
s1.ShowDetails()