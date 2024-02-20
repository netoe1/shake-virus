import pyautogui
import random

limits = pyautogui.size()

def shakeMouse():
    pyautogui.moveTo(random.randint(limits.height),random.randint(limits.width),1)

def main():
    print('Shaking....')
    while(1 == 1):
        shakeMouse()
