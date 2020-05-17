from concurrent.futures.thread import ThreadPoolExecutor

from util import PingUtil

NO_OF_PROCESS = 300

def getIPPingStatus(ip):
    flag = PingUtil.isIPReachable(ip)
    formattedOut = '%16s : %s' % (ip, flag)
    return formattedOut

def checkAllIpsByMultiThreading(fileName):
    from util import FileUtil
    ips = FileUtil.readIPsFromFile(fileName)
    executor = ThreadPoolExecutor(NO_OF_PROCESS)
    results = executor.map(getIPPingStatus, ips)
    dataList = list(results)
    for i in dataList:
        print(i)