a = [10,1,12,23,25]
target = 100
temp = True
for j,i in enumerate(a,start=1):
    if i == target:
        print(f"Element Is Found at {j} position")
        temp = False
        break
    
if temp == True:
    print("Element Not Found !!!")