from multiprocessing import Pool

from util import FileUtil, PingUtil

NO_OF_PROCESS = 20

def getIPPingStatus(ip):
    flag = PingUtil.isIPReachable(ip);
    formattedOut = '%16s : %s' % (ip, flag)
    return formattedOut

def checkAllIpsByMultiprocessing(fileName):
    ips = FileUtil.readIPsFromFile(fileName)
    pool = Pool(processes=NO_OF_PROCESS)
    result = pool.map_async(getIPPingStatus, ips)
    pool.close()
    dataList = result.get()
    for i in dataList:
        print(i)