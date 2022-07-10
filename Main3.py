from timeit import default_timer as timer

from parallel.SequentialPing import checkAllIpsSequentially
from parallel.MultiThreadingPing import checkAllIpsByMultiThreading
from parallel.MulitprocessingPing import checkAllIpsByMultiprocessing

FILE_NAME = "testData/ipaddress-512.txt"

def executeSequentiall():
    checkAllIpsSequentially(FILE_NAME)

def executeMultiThreaded():
    checkAllIpsByMultiThreading(FILE_NAME)

def executeMultiprocessing():
    checkAllIpsByMultiprocessing(FILE_NAME)


if __name__ == '__main__':
    ip_addr_range_1 = input ('first ip range to scan\n')
    ip_addr_range_2 = input ('second ip range to scan\n')
    excluded_ip_addr = input('What last octet do you want to exclude in the scan?\n')

    print ("excluding " + ip_addr_range_1 + "." + excluded_ip_addr)
    print ("excluding " + ip_addr_range_2 + "." + excluded_ip_addr)
    start = timer()
    
    # executeMultiprocessing() # 14.33898959698854  seconds
    executeMultiThreaded() # 10.679292550019454  seconds
    # executeSequentiall() # 163.009457  seconds

    end = timer()
    result = end - start
    print("Total Time Taken: ", result, " seconds")
