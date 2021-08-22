# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip3 install pytesseract

from PIL import Image
import pytesseract
import pyautogui
import time

def main():
    while True:
        time.sleep(0.3)
        img = pyautogui.screenshot(region=[1497,850,400,80])
        words = pytesseract.image_to_string(img)
        # print(words)
        # print(words.startswith('Fishing Bobber splashes'))
        # print('Fishing Bobber splashes' in words)
        if ('Fishing Bobber splashes' in words):
            x,y = pyautogui.position()
            pyautogui.click(x,y,button='right')
            time.sleep(2)
            pyautogui.click(x,y,button='right')
    # get mouse position
    # while 1:
        # x,y=pyautogui.position()
        # print(x,y)
    
if __name__ == '__main__':
    main()