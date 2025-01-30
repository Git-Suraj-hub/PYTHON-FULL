import threading
import time
from concurrent.futures import ThreadPoolExecutor
# Create a sleap function

def func(a):
    time.sleep(a)
    print(f"Completed {a} seconds")
    return a
    
# run a function using simple program 

# time1 = time.perf_counter()

# func(10)
# func(5)
# func(1)
# func(3)

# time2 = time.perf_counter()
# print(f"The Total Time Completed On {time2-time1} Seconds")

#run a same program using threading

# time1 = time.perf_counter()  
# t1 = threading.Thread(target=func,args=[10])
# t2 = threading.Thread(target=func,args=[5])
# t3 = threading.Thread(target=func,args=[1])
# t4 = threading.Thread(target=func,args=[3])    
# t1.start()
# t2.start()
# t3.start()
# t4.start()

# t1.join()
# t2.join()
# t3.join()
# t4.join()


# time2 = time.perf_counter()
# print(f"the Total Time Completed Using Threading is {time2-time1}")

# in real life world 

def pooling():
    with ThreadPoolExecutor() as executor:
        # f1 = executor.submit(func,10)
        # f2 = executor.submit(func,5)
        # f3 = executor.submit(func,1)
        # f4 = executor.submit(func,3)
        
        # print(f1.result())
        # print(f2.result())
        # print(f3.result())
        # print(f4.result())
        
        l = [0,10,2,3]
        result = executor.map(func,l)
        for result in result:
            print(result)
            

pooling()