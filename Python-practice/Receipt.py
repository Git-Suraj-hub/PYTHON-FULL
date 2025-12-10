import pandas as pd

nameList = []
dic = {}

while True:
    name = input("Enter A Customer Name and press 'q' if no more customer: ")
    if name == "q":
        break
    nameList.append(name)
    y = int(input(f"How Many Items Did {name} Buy: "))
    dic[name] = {}
    total = 0
    for i in range(y):
        item = input("Enter An Item Name: ")
        price = int(input("Enter An Item Price: "))
        dic[name][item] = price
        total += price
    dic[name]['total'] = total

print(nameList)
print(dic)

dic1 = {name: dic[name] for name in nameList}
print("Final Dictionary:", dic1)

# Create DataFrame
df = pd.DataFrame(dic1).transpose()
print(df)
