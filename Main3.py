from timeit import default_timer as timer

from parallel.SequentialPing import checkAllIpsSequentially
from parallel.MultiThreadingPing import checkAllIpsByMultiThreading
from parallel.MulitprocessingPing import checkAllIpsByMultiprocessing

FILE_NAME = "testData/ipaddress-50.txt"

def executeSequentiall():
    checkAllIpsSequentially(FILE_NAME)

def executeMultiThreded():
    checkAllIpsByMultiThreading(FILE_NAME)

def executeMultiprocessing():
    checkAllIpsByMultiprocessing(FILE_NAME)


if __name__ == '__main__':
    start = timer()

    # executeMultiprocessing() # 13.2449947  seconds
    executeMultiThreded() # 4.3145787  seconds
    # executeSequentiall() # 163.009457  seconds

    end = timer()
    result = end - start
    print("Total Time Taken: ", result, " seconds")
