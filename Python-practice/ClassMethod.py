class Student:
    university = "MEWAR UNIVERSITY"
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"the student name is {self.name} and colleg name {self.university}")
    @classmethod
    def CHange(self,name):
        self.university = name
        
s1 = Student("suraj")
s1.show()
print(f"the university Name is {Student.university}")
s2 = Student("Manish")
s2.show()
s2.CHange("SANGAM UNIVERSITY")
s2.show()
print(f"the university Name is {Student.university}")


        