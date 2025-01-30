class sub:
    def __init__(self,a,b,c):
        self.a = a;
        self.b = b;
        self.c = c;
    def __str__(self):
        return f"{self.a}i + {self.b}j + {self.c}k"
    def __add__(self,x):
        # return sub(self.a+x.a , self.b+x.b , self.c+x.c)
        return f"{self.a + x.a}i + {self.b + x.b}j + {self.c-x.c}k"
a = sub(1,2,3)
print(a)
b = sub(4,5,6)
print(b)
print(a+b) 
print(type(a+b))
