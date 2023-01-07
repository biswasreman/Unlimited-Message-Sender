import pyautogui
import time 
time.sleep(4)
fun = 0
while fun <= 100:
    pyautogui.typewrite("Advance Happy New Year " + str(fun))
    pyautogui.press("enter")
    fun = fun + 1

