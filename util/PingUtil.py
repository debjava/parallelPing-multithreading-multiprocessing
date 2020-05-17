import subprocess
from subprocess import DEVNULL
import platform

PING_COMMAND = 'ping'
PING_COUNT = '1'


def isIPReachable(ipAddress):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    pingCmdArgs = [PING_COMMAND, param, PING_COUNT, ipAddress]
    
    process = subprocess.Popen(pingCmdArgs, stdout=DEVNULL, stderr=DEVNULL)
    out, error = process.communicate()
    responseCode = process.returncode
    return (responseCode == 0)


def isIPReachableVerbose(ipAddress):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = [PING_COMMAND, param, PING_COUNT, ipAddress]
    return subprocess.call(command) == 0
    
    
def formatIPReachability(ipAddress, status):
    formattedOut = '%16s : %b' % (ipAddress, status)
    return formattedOut

