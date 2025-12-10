from urllib.request import urlretrieve
import multiprocessing
import concurrent.futures
import time

def download_file_simple(url, filename):
    try:
        urlretrieve(url, f"{filename+1}.jpeg")
        return (f"Successfully downloaded {filename+1}")
    except Exception as e:
        print(f"An error occurred: {e}")
# t1 = time.perf_counter()
# # download Using Simple Function
# url = "https://picsum.photos/2000/3000"
# for i in range(10):
#     download_file_simple(url,i)
# t2 = time.perf_counter()

# print(f"Total Time to download all images is : {t2-t1}")

# Download using Multiprocessing

if __name__ == '__main__':
    # t1 = time.perf_counter()
     url = "https://picsum.photos/2000/3000"
    # # for i in range(10):
    # #     download_file_simple(url, f"{i}.jpeg")
    # proc = []
    # for i in range(10):
    #     a = multiprocessing.Process(target=download_file_simple,args=[url,i])
    #     a.start()
    #     proc.append(a)
    # for i in proc:
    #     i.join()
    # t2= time.perf_counter()
    # print(f"Total time to download this image is {t2-t1}")
     t1 = time.perf_counter()

     with concurrent.futures.ProcessPoolExecutor() as executor:
         l1 = [i for i in range(10)]
         l2 = [url for i in range(10)]
         result = executor.map(download_file_simple,l2,l1)
         for r in result:
             print(r)
     t2= time.perf_counter()
     print(f"Total time to download this image is {t2-t1}")