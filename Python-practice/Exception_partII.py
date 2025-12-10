# import math
# try:
#     result = math.exp(1000)
# except ZeroDivisionError as e:
#     print(e)
# except OverflowError as e:
#     print(e)
# finally:
#     result = 10 / 0


# try:
#     result = math.exp(1000)  # Exponential function with a large argument
# except OverflowError as e:
#     print(e)

# import sys
# import math

# # sys.float_info.max = 1.79e+308  # Maximum float value

# try:
#     # math.sqrt(-1.0)
#     result = 10 / 0  # This doesn't raise a FloatingPointError by default
# except FloatingPointError as e:
#     print(e)


# my_list = [1, 2, 3]

# try:
#     element = my_list[5]
# except IndexError as e:
#     print("Error:",e)
#     e = "list is out of range"
#     print(e)


# a = 5

# if a % 2 != 0:
# 	raise Exception("The number shouldn't be an odd integer")           #raise exception 


# s = 'apple'

# try:
#     num = int(s)
# except ValueError as e:
#     raise ValueError("String can't be changed into integer")



