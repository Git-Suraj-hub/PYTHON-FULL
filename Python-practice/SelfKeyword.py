class Person:
    name = "UNKNOWN"
    occupation = "UNKNOWN"

    def info(self):
        print(f"{self.name} is a {self.occupation}")
Person1 = Person()
Person1.name = "suraj"
Person1.occupation = "HR"
Person1.info()