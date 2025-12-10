class student:
    collage_name = "MEWAR UNIVERSITY"
    def __init__(self,name):
        self.name = name
        self.roll =1
    def show(self):
        print(f"the student name is {self.name} of {self.collage_name} student and his/her roll no is {self.roll}")
        
s1 = student("suraj")
student.collage_name = "MEWAR"
s2 = student("Vibhanshu")
s2.roll = 2
s2.collage_name="mewar" # only change instance variable not a whole class variable
s1.show()
s2.show()
