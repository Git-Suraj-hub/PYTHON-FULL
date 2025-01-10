x =int(input("Enter a number :"))
match x:
    case 0:
        print("X is zero")
    case 1: 
        print("x is Zero")
    case _ if x>=4:
        print("x is greater than 4")
    case _ if x>=100:
        print("x is greaster than and equal to 100")
    case 5:
        print(" x is equal to 5")
    case _:
        print("x is not equal to zero and one ")


