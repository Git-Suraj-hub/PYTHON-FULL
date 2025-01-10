# a = int(input("Enter A Number : "));
# def fact(a):
#     if(a==0 or a==1):
#         return 1
#     else:
#       return a*fact(a-1)
# print(f"the factorial of {a} is : {fact(a)}");


def fib(n):
    if n <= 0:
        return 0
    elif n == 1: 
        return 1
    else:
        return (fib(n-1) + fib(n-2))

n = int(input("Enter a Number : "))
for i in range(n):
    print(fib(i))



