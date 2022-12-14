import subprocess
import pyautogui
import time
import random
from time import sleep
while True :
    for i in range(1,5):
        subprocess.Popen('notepad')
        subprocess.Popen('calc')
        x= random.randrange(0, 900, 1) 
        y= random.randrange(0, 900, 1)
        pyautogui.moveTo(x, y) 
        loc = time.localtime() 
        result = time.strftime("%I:%M:%S %p", loc)
        time.sleep(0.1) 
                
                                                 
