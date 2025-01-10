import random

def coin_toss():
    # Generate a random number: 0 or 1
    result = random.randint(0, 1)
    if result == 0:
        return "Heads"
    else:
        return "Tails"

# Toss the coin and print the result
print("Coin Toss Result:", coin_toss())
