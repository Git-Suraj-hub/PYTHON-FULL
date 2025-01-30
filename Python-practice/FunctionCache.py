import functools
import time

@functools.lru_cache(maxsize=None)
def add(a, b):
    time.sleep(4)
    return a + b

# Testing the function
print(f"the sum of 2 and 3 is {add(2, 3)}")
print(f"the sum of 5 and 3 is {add(5, 3)}")
print(f"the sum of 4 and 3 is {add(4, 3)}")
# This call should be faster as the result is cached
print(f"the sum of 2 and 3 is {add(2, 3)}")
print(f"the sum of 6 and 10 is {add(6, 10)}")
# This call should be faster as the result is cached
print(f"the sum of 4 and 3 is {add(4, 3)}")
