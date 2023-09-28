import pyautogui as pg
import time, keyboard, cv2
import numpy as np


def confirmm():
    start_time = time.time()
    while True:
        template = cv2.imread('confirm.png', cv2.IMREAD_GRAYSCALE)
        screenshot = np.array(pg.screenshot())
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= 0.8:
            x, y = max_loc
            w, h = template.shape[::-1]
            x += w // 2
            y += h // 2
            print("Confirm Button Found")
            pg.moveTo(x,y)
            time.sleep(0.5)
            pg.click(x, y)
            time.sleep(1)
            pg.moveTo(1090, 500)
            break # exit the loop
        else:
            print("Confirm Button Not Found")
            time.sleep(0.01)
            elapsed_time = time.time() - start_time
            print(elapsed_time, "Second and If not Found In 30 Seconds Closing The Loop")
            if elapsed_time >= 4:
                print("Elapsed time exceeded 30 seconds, exiting the loop")
                break # exit the loop  