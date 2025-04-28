import keyboard
import pyautogui
import time

print("Press r to record positions, press any other key to break")
pos_list = []
loop = True

while loop:
    if keyboard.read_key() == 'r':
        print(pyautogui.position())
        pos_list.append(pyautogui.position())
        loop = True
    else:
        loop = False

print(pos_list)
print("filtering dupes")
pos_list = list(dict.fromkeys(pos_list))
print(pos_list)

## autoclick
print("Press q to start autoclicker")
keyboard.wait('q')
print("Autoclicker started.")

while True:
    for i in range(0, len(pos_list)):
        pyautogui.click((pos_list[i].x,pos_list[i].y)) # slot machine
    time.sleep(6)