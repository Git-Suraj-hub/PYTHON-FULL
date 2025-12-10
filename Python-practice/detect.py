a = "suraj                                                   singh"
while(1):
    if a.find('  ') !=-1:
        print('DOUBLE SPACE DETECTED')
        c = a.replace("  "," ")
        a =c
        print(a)
        print("DOUBLE SPACE CONVERTED TO SINGLE SPACE")
    else:
        print("NO DOUBLE SPACE DETECTED !!!!")
        break