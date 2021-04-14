import pyautogui as pyg
import time

def Write(line):
    pyg.write(line, interval=0.0001)
    pyg.press('enter')

time.sleep(5)
with open("MScript.txt") as file:
    for line in file:
        line = line.strip() #preprocess line
        Write(line)
        time.sleep(0.1)
