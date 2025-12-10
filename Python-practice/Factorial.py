import pandas as pd

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def trail(n):
    zero = 0
    while n > 0:
        c = n % 10
        if c == 0:
            zero += 1
            n = n // 10
        else:
            break
    return zero

if __name__ == "__main__":
    data = {"Number": [], "Factorial": [], "Trailing Zeroes": []}
    try:
        while True:
            num = input("Enter A Number and press 'q' to quit: ")
            if num == "q":
                break
            num = int(num)
            
            c = factorial(num)
            print(f"The factorial of {num} is {c}")
            d = trail(c)
            print(f"The number {c} has {d} trailing zeroes.")
            
            # Append data to the list
            data["Number"].append(num)
            data["Factorial"].append(c)
            data["Trailing Zeroes"].append(d)
            
    except ValueError:
        print("Your input is not an integer.")
    
    # Create DataFrame
    df = pd.DataFrame(data)
    print(df)
