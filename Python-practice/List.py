l = [3,5,6,"SURAJ"]
# print(l)
# print(type(l))

# print(l)
# print(l[:])
# print(l[0:])
# print(l[1:])                    // printing the list
# print(l[1:len(l)])
# print(l[1:5:10])    // example of not overflow in list
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[100])   // out of index error

# for i in range(len(l)):
#     print(l[i])


# for i in range(0,len(l)):         // print the list using for loop
#     print(l[i])


# for i in range(0,len(l),1):   // jump the elemnt by one
#     print(l[i])

# if "SURAJ" in l:
#     print("YES")               
# else:
#     print("No")

# if "SU" in "SURAJ":                       // check the list element avaiable on our list or not
#     print("YES")
# else:
#     print("NO")

# if ("SUR") in l[3]:
#     print("YES")
# else:
#     print("NO")

# if ("SUR") in "suraj":
#     print("YES")
# else:
#     print("NO")

# ********     LIST COMPREHENSION ************ 

# lst   =[i**2 for i in range(1,11)]
# print(lst)

# also we add a condition in list


# lst1   =[i**2 for i in range(1,11) if i%2==0 ]
# print(lst1)


# lst3 = ["ola" , "oval" , "om" , "namah" , "siv"]
# l =[i for i in lst3 if "o" in i]
# print(l)

# lst4  = [1,2,4,5,7,8]
# l = [i for i in lst4 if i>=2]
# print(l)

# lst3 = ["ola" , "oval" , "om" , "namah" , "siv"]
# l =[i for i in lst3 if (len(i))>=3]
# print(l)