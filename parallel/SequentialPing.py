from util import FileUtil, PingUtil


def checkAllIpsSequentially(fileName):
    ips = FileUtil.readIPsFromFile(fileName)
    for ip in ips:
        pingIP(ip)


def pingIP(ip):
    flag = PingUtil.isIPReachable(ip);
    formattedOut = '%16s : %s' % (ip, flag)
    print(formattedOut)
