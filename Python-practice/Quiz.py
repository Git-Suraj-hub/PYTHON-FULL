value = input("Enter a Value between 1 to 100 or type 'quit' to exit: ")

if value.lower() == "quit":
    print("Exiting the program.")
else:
    try:
        a = int(value)
        if a <= 1 or a >= 101:
            raise ValueError("Your number is not between 1 to 100")
        else:
            print(f"You entered a valid number: {a}")
    except ValueError as e:
        print(e)
