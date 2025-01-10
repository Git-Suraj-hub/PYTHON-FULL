import random
random_integer = random.randint(1, 100)
cout = 0

while True:
    x = int(input(" Guess The Number :"))
    if x==random_integer:
        print("Congratulation you guess Correct Number")
        print(f"{cout} attempt  to guess correct random number  ")
        break
    elif x>random_integer:
        print("you guess the random number is high !!!")
        cout+=1
    else :
        print("you guess the random number so low !!!")
        cout+=1

