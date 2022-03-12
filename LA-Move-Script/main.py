import pyautogui
import random
import time
pyautogui.FAILSAFE = True
screen = pyautogui.size()

while True:
    # Move mouse around the center of the screen to random places at random speeds and rightclick
    x_coord = random.randrange(((screen[0] / 2) - 400), ((screen[0] / 2) + 400))
    y_coord = random.randrange((screen[1] / 2) - 200, (screen[1] / 2) + 200)
    move_duration = random.randrange(2, 6)
    pyautogui.moveTo(x_coord, y_coord, duration=move_duration)
    pyautogui.click(button="right")

    # Press a random skill key at random intervals
    time.sleep(random.randint(1,3))
    match random.randint(1,8):
        case 1:
            pyautogui.typewrite("q")
        case 2:
            pyautogui.typewrite("w")
        case 3:
            pyautogui.typewrite("e")
        case 4:
            pyautogui.typewrite("r")
        case 5:
            pyautogui.typewrite("a")
        case 6:
            pyautogui.typewrite("s")
        case 7:
            pyautogui.typewrite("d")
        case 8:
            pyautogui.typewrite("f")