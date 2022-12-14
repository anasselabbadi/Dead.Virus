import subprocess
import pyautogui
import time
import random
pyautogui.FAILSAFE = False
pyautogui.KEYBOARD_KEYS
from time import sleep
subprocess.Popen('notepad')
pyautogui.hotkey('Caps',presses=2)
pyautogui.hotkey('/',presses=1)
pyautogui.write('loop',interval=0.5)
pyautogui.press('enter', presses=1)
pyautogui.write('start',interval=0.5)
pyautogui.press('enter', presses=1)
pyautogui.write('goto loop',interval=0.5)
pyautogui.hotkey('Ctrl','s',presses=1)
pyautogui.write('DV;bat',interval=0.5)
pyautogui.press('enter', presses=1)
for i in range (1,2):
    pyautogui.hotkey('win',presses=1)
    pyautogui.write('DV;bat',interval=0.5)
    pyautogui.press('enter', presses=1)
    while True :
        for i in range(1,5):
            subprocess.Popen('notepad')
            subprocess.Popen('calc')
            x= random.randrange(0, 900, 1) 
            y= random.randrange(0, 900, 1)
            pyautogui.moveTo(x,y) 
            loc = time.localtime() 
            result = time.strftime("%I:%M:%S %p", loc)
            time.sleep(0.1) 
                
                                                 
