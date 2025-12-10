Question = ["Who Is the Owner Of Sasta K.B.C" ,"what Amount Of Winning Price Of Sasta K.B.C.","Which Company Laptop Use Of Owner Of Sasta K.B.C." ]
Answer = ["SURAJ SINGH MEHTA" , "1 Lakh " , "\Lenovo Ideapad Slim 3i"]
Amount = 0
for i in range(len(Question)):
    print(f"Q{i+1}) {Question[i]}")
    print("0) SURAJ SINGH MEHTA \n1) 1 Lakh \n2) Lenovo Ideapad Slim 3i")
    an = int(input("Enter a Coorect Option : "))
    
    if Answer[i] == Answer[an]:
        print("Correct answer ")
        Amount += 33333
    else:
        print("Wrong Anser ")
        Amount -= 33333
if Amount>0:
    print(f"you Won The Total Amount In Sasta K.B.C. is {Amount}")
else:
    print("You WOn Nothing Amount Thanks To Participate This Program \n Better Luck NExt Time")