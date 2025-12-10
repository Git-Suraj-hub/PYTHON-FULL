import time
obj = time.localtime()
print(obj)
obj1 = time.gmtime()
print(obj1)
string = "Tue, 03 Aug 2021 10:45:08"
obj2 = time.strptime(string, "%a, %d %b %Y %H:%M:%S")
print(obj2)