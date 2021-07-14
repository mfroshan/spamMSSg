import pyautogui
from time import sleep


def spam(msg,maxMsg):
  

    pyautogui.click(x=100, y=200)


    for i in range(maxMsg):
        pyautogui.write(msg)
        pyautogui.press("enter")
        print(f"count: {i}" )
        # if ya want a delay
        sleep(0)

msg = input("enter yo msg:")
n = int(input("Enter how many times:"))

spam(msg, n)
