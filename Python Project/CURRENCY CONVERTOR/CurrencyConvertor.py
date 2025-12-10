with open('CurrencyConvertor.txt') as f:
    lines = f.readlines()

currency_dict = {}
for line in lines:
    parsed = line.strip().split("\t")
    if len(parsed) >= 2:  # Check if there are at least two elements
        currency_dict[parsed[0]] = parsed[1]
    else:
        print(f"Skipping line: {line.strip()} - Not enough elements")

amount = float(input("Enter an amount: "))
currency = input("Enter the name of the currency you want to convert to: ")

converted_amount = float(currency_dict[currency]) * amount
print(f"Your amount is {amount} and converting it to {currency} is equal to {converted_amount}")
