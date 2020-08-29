
import platform,socket,re,uuid,json,psutil,logging,os
info = {}
f = open("testfile.txt","a")
def setSystemInfo():
    try:
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    except Exception as e:
        logging.exception(e)
    return info

def print_sysinfo():
    #Checking if the log file is empty. We only input the system information if the log file is empty
    filesize = os.path.getsize("logs.txt")
    if filesize == 0:
        for i,j in info.items():
            f.write(i+ " "+ j+"\n")
            # print(i+" "+j+"\n")


if __name__ == "__main__":
    setSystemInfo()
    print_sysinfo()