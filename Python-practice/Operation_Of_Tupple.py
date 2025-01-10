tup = (1,1,2,3,4)
# print(tup.count(1))

# print(tup.index(1))

# print(tup.index(3,0,len(tup)))

# print(tup.index(322))  // showing a error x(322) is not in your tupple
# tup[0] = 20   // this is not valid because tupple can't be changed if you want to change this tupple firstly you change this tuuple to list and then you will change easily and again you change to listg to tupple and all set 


tup = list(tup)  # change to tupple to list through list method
print(type(tup))
tup[0] = 10     #this is asccessble because this is list not a tuuple
tup = tuple(tup)
print(type(tup))
tup[0] = 10  # this is not ascceble because this is tupple not a list
print(tup)
