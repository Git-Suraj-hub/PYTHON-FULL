def Fib():
    a,b=0,1
    while True:
        yield a
        a,b = b,a+b
    
a= Fib()

for i in range(10):
    next(a)
    