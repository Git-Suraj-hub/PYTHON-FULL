class Claculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self,a,b):
        return a + b
    @staticmethod
    def sub(a,b):
        return a-b
c1 = Claculator(1,2)
add = c1.add(2,3)
sub = c1.sub(2,3)
sub1 = Claculator.sub(3,3)
print(add,sub,sub1)