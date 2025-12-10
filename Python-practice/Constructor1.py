class Student:
    def __init__(self, n="UNKNOWN", b="UNKNOWN"):
        if n == "UNKNOWN" and b == "UNKNOWN":
            print("Hey I AM DEFAULT CONSTRUCTOR")
        else:
            print("HEY I AM PARAMETERIZED CONSTRUCTOR")
        self.n = n
        self.b = b

    def info(self):
        if self.n=="UNKNOWN" and self.b =="UNKNOWN":
            print("you can't a request info because your data is not entered ")
        else:
            print(f"I AM {self.n} from {self.b}")

# Example usage:
s1 = Student() 
s1.info() # This will use the default values
s2 = Student("suraj","B.tech")
s2.info()