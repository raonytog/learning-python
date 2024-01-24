# ideia a parte do curso

import pyautogui, keyboard
keyboard.wait('[')
while not keyboard.is_pressed(']'):
    pyautogui.doubleClick()
    
