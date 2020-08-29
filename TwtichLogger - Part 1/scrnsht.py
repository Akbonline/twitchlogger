'''
1. Create a function to capture the screenshots
2. Create a Process
3. update every x interval

'''
from pyautogui import screenshot
from multiprocessing import Process
import time
import keyboard

class Scrnsht:

    def __init__(self):   #Adding a hotkey to killall the process, created a Process, Started the screenshot object
        keyboard.add_hotkey("esc", self.stop_scrnshts)
        self.P = Process(target= self.start_scrnshts)
        self.myScreenshot = screenshot()

    def start(self):            #Start the process
        self.P.start()

    def start_scrnshts(self):   #Creating an infinite loop and pausing for 5 seconds every time...
        i = 0
        while True:
            self.myScreenshot.save(str(i)+ '.png')          #Storing the screenshot
            time.sleep(5)
            i+=1

    def stop_scrnshts(self):
        self.P.terminate()
    
if __name__ == "__main__":
    S = Scrnsht()
    S.start()