import pyautogui as pg
import time, keyboard, cv2
import numpy as np
import random
import datetime
import pyperclip

import confirm
import ranMission


def nested_loop_Fb_fallow():
    ################################################################
    pg.click(557,47)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pg.typewrite("https://wwww.like4like.org/user/earn-facebook-subscribes.php")
    pg.press('enter')
    pg.moveTo(1090, 500)
    
    
    ################################################################
    time_ranInt = random.randint(2, 4)
    time.sleep(time_ranInt)
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):  # if key 'esc' is pressed 
            print("Exiting the program...")
            break  # finishing the loop
        time_ranInt = random.randint(2, 5)
        time.sleep(time_ranInt)
        start_time = time.time()
        
        ############################################################
        while True:
            button1_template = cv2.imread('tfnomore.png', cv2.IMREAD_GRAYSCALE)
            button2_template = cv2.imread('instafollow1.png', cv2.IMREAD_GRAYSCALE)
            screenshot = np.array(pg.screenshot())
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            button1_result = cv2.matchTemplate(gray_screenshot, button1_template, cv2.TM_CCOEFF_NORMED)
            button2_result = cv2.matchTemplate(gray_screenshot, button2_template, cv2.TM_CCOEFF_NORMED)
            button1_min_val, button1_max_val, button1_min_loc, button1_max_loc = cv2.minMaxLoc(button1_result)
            button2_min_val, button2_max_val, button2_min_loc, button2_max_loc = cv2.minMaxLoc(button2_result)
            
            ########################################################
            
            if button1_max_val >= 0.8:
                x, y = button1_max_loc
                w, h = button1_template.shape[::-1]
                x += w // 2
                y += h // 2
                print("Instagram Earnings No More Found")
                time.sleep(0.5)
                ranMission.main()
            elif button2_max_val >= 0.8:
                x, y = button2_max_loc
                w, h = button2_template.shape[::-1]
                x += w // 2
                y += h // 2
                print("Instagram Earing Button Found")
                time.sleep(1)
                pg.click(x, y)
                pg.moveTo(1090, 500)
                time.sleep(1)
                break                   
            else:
                print("Buttons are Not Found Please Check The Images Or check The Program")
                time.sleep(0.1)
                elapsed_time = time.time() - start_time
                print(elapsed_time)
                if elapsed_time >= 30:
                    print("Elapsed time exceeded 20 seconds, exiting the loop")
                    ranMission.main()
                    break
                
    #################################################################
        start_time = time.time()  
        time.sleep(4)    
        while True:
                time_ranInt = random.randint(6, 9)
                time.sleep(time_ranInt)
                button1_template = cv2.imread('likePageFb.jpg', cv2.IMREAD_GRAYSCALE)
                screenshot = np.array(pg.screenshot())
                gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
                button1_result = cv2.matchTemplate(gray_screenshot, button1_template, cv2.TM_CCOEFF_NORMED)
                button1_min_val, button1_max_val, button1_min_loc, button1_max_loc = cv2.minMaxLoc(button1_result)
                
                ################################################################
                
                if button1_max_val >= 0.8:
                    x, y = button1_max_loc
                    w, h = button1_template.shape[::-1]
                    x += w // 2
                    y += h // 2
                    print("Fb Follow Button Found")
                    time_ranInt = random.randint(6, 9)
                    print(time_ranInt)
                    time.sleep(time_ranInt)
                    pg.click(x, y)
                    time.sleep(2)
                    pg.hotkey("alt", "tab")
                    confirm()      
                    pg.hotkey("alt", "tab")
                    time.sleep(1)

                    template2 = cv2.imread('logo_fb.jpg', cv2.IMREAD_GRAYSCALE)
                    screenshot2 = np.array(pg.screenshot())
                    gray_screenshot2 = cv2.cvtColor(screenshot2, cv2.COLOR_BGR2GRAY)
                    result2 = cv2.matchTemplate(gray_screenshot2, template2, cv2.TM_CCOEFF_NORMED)
                    min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)
                    
                    ################## click vào logo
                    if max_val2 >= 0.8:
                        x, y = max_loc2
                        w, h = template2.shape[::-1] 
                        x += w // 2
                        y += h // 2
                        print("Fb logo Button Found")
                        time_ranInt = random.randint(1, 3)
                        print(time_ranInt)
                        time.sleep(time_ranInt)
                        pg.click(x, y)
                        time_ranInt = random.randint(1, 3)
                        time.sleep(time_ranInt)

                    # Random thời gian 
                    random_time = random.uniform(15, 20)
                    start_time = datetime.datetime.now()
                    run_time = datetime.timedelta(seconds = random_time)
                    
                    while datetime.datetime.now() - start_time < run_time: 
                        ######################### Kéo   
                        time_ranInt = random.randint(5, 8)
                        time_ranReverse = random.randint(-300, -240)
                        for _ in range(time_ranInt):
                            pg.scroll(time_ranReverse)
                            time.sleep(1)
                            time_ranReverse = random.randint(-250, -200)
                            pg.scroll(time_ranReverse)
                            time_ranInt = random.randint(2, 4)
                            time.sleep(time_ranInt)


                            time_ranInt = random.randint(1, 6) # 1 ==> 8
                            if time_ranInt == 1: 
                                #thích  
                                time_ranInt = random.randint(2, 6)
                                random_time3 = time_ranInt
                                start_time3 = datetime.datetime.now()
                                run_time3 = datetime.timedelta(seconds = random_time3)
                                while datetime.datetime.now() - start_time3 < run_time3:
                                # while True:
                                    template3 = cv2.imread('likeBtnfb.jpg', cv2.IMREAD_GRAYSCALE) 
                                    screenshot3 = np.array(pg.screenshot())
                                    gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                    result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                    min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
                                    if max_val3 >= 0.8:
                                        x, y = max_loc3
                                        w, h = template3.shape[::-1] 
                                        x += w // 2
                                        y += h // 2
                                        print("Fb like Button Found")
                                        time.sleep(2)
                                        pg.click(x, y)
                                        time.sleep(1)
                                        # Kéo
                                        time_ranInt = random.randint(5, 8)
                                        time_ranReverse = random.randint(-300, -240)
                                        for _ in range(time_ranInt):
                                            pg.scroll(time_ranReverse)
                                            time.sleep(1)
                                            time_ranReverse = random.randint(-250, -200)
                                            pg.scroll(time_ranReverse)
                                            time_ranInt = random.randint(2, 4)
                                            time.sleep(time_ranInt)
                                            break
                                    else: 
                                        time_ranInt = random.randint(5, 8)
                                        time_ranReverse = random.randint(-300, -240)
                                        for _ in range(time_ranInt):
                                            pg.scroll(time_ranReverse)
                                            time.sleep(1)
                                            time_ranReverse = random.randint(-250, -200)
                                            pg.scroll(time_ranReverse)
                                            time_ranInt = random.randint(2, 4)
                                            time.sleep(time_ranInt)
                                            break  
                            elif time_ranInt == 2: 
                                #yêu thích 
                                time_ranInt = random.randint(2, 6)
                                random_time3 = time_ranInt
                                start_time3 = datetime.datetime.now()
                                run_time3 = datetime.timedelta(seconds = random_time3)
                                while datetime.datetime.now() - start_time3 < run_time3:
                                # while True:
                                    template3 = cv2.imread('likeBtnfb.jpg', cv2.IMREAD_GRAYSCALE) 
                                    screenshot3 = np.array(pg.screenshot())
                                    gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                    result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                    min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
                                    if max_val3 >= 0.8:
                                        x, y = max_loc3
                                        w, h = template3.shape[::-1] 
                                        x += w // 2
                                        y += h // 2
                                        print("Fb like Button Found")
                                        time.sleep(2)
                                        pg.moveTo(x, y)
                                        time_ranInt = random.randint(2, 4)
                                        time.sleep(time_ranInt)
                                        x -= 10
                                        y -= 40
                                        pg.click(x, y)

                                        time.sleep(0.5)
                                        pg.hotkey("esc") 

                                        time_ranInt = random.randint(2, 4)
                                        time.sleep(time_ranInt)

                                        # Kéo
                                        time_ranInt = random.randint(5, 8)
                                        time_ranReverse = random.randint(-300, -240)
                                        for _ in range(time_ranInt):
                                            pg.scroll(time_ranReverse)
                                            time.sleep(1)
                                            time_ranReverse = random.randint(-250, -200)
                                            pg.scroll(time_ranReverse)
                                            time_ranInt = random.randint(2, 4)
                                            time.sleep(time_ranInt)
                                            break
                                    else: 
                                        time_ranInt = random.randint(5, 8)
                                        time_ranReverse = random.randint(-300, -240)
                                        for _ in range(time_ranInt):
                                            pg.scroll(time_ranReverse)
                                            time.sleep(1)
                                            time_ranReverse = random.randint(-250, -200)
                                            pg.scroll(time_ranReverse)
                                            time_ranInt = random.randint(2, 4)
                                            time.sleep(time_ranInt)
                                            break  
                            elif time_ranInt == 3: 
                                #thương thương
                                time_ranInt = random.randint(2, 6)
                                random_time3 = time_ranInt
                                start_time3 = datetime.datetime.now()
                                run_time3 = datetime.timedelta(seconds = random_time3)
                                while datetime.datetime.now() - start_time3 < run_time3:
                                # while True:
                                    template3 = cv2.imread('likeBtnfb.jpg', cv2.IMREAD_GRAYSCALE) 
                                    screenshot3 = np.array(pg.screenshot())
                                    gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                    result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                    min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
                                    if max_val3 >= 0.8:
                                        x, y = max_loc3
                                        w, h = template3.shape[::-1] 
                                        x += w // 2
                                        y += h // 2
                                        print("Fb like Button Found")
                                        time.sleep(2)
                                        pg.moveTo(x, y)
                                        time_ranInt = random.randint(2, 4)
                                        time.sleep(time_ranInt)
                                        x += 35
                                        y -= 40
                                        pg.click(x, y)

                                        time.sleep(0.5)
                                        pg.hotkey("esc") 

                                        time_ranInt = random.randint(2, 4)
                                        time.sleep(time_ranInt)

                                        # Kéo
                                        time_ranInt = random.randint(5, 8)
                                        time_ranReverse = random.randint(-300, -240)
                                        for _ in range(time_ranInt):
                                            pg.scroll(time_ranReverse)
                                            time.sleep(1)
                                            time_ranReverse = random.randint(-250, -200)
                                            pg.scroll(time_ranReverse)
                                            time_ranInt = random.randint(2, 4)
                                            time.sleep(time_ranInt)
                                            break
                                    else: 
                                        time_ranInt = random.randint(5, 8)
                                        time_ranReverse = random.randint(-300, -240)
                                        for _ in range(time_ranInt):
                                            pg.scroll(time_ranReverse)
                                            time.sleep(1)
                                            time_ranReverse = random.randint(-250, -200)
                                            pg.scroll(time_ranReverse)
                                            time_ranInt = random.randint(2, 4)
                                            time.sleep(time_ranInt)
                                            break  
                            elif time_ranInt == 4: 
                                #thương thương
                                time_ranInt = random.randint(2, 6)
                                random_time3 = time_ranInt
                                start_time3 = datetime.datetime.now()
                                run_time3 = datetime.timedelta(seconds = random_time3)
                                while datetime.datetime.now() - start_time3 < run_time3:
                                # while True:
                                    template3 = cv2.imread('likeBtnfb.jpg', cv2.IMREAD_GRAYSCALE) 
                                    screenshot3 = np.array(pg.screenshot())
                                    gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                    result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                    min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
                                    if max_val3 >= 0.8:
                                        x, y = max_loc3
                                        w, h = template3.shape[::-1] 
                                        x += w // 2
                                        y += h // 2
                                        print("Fb like Button Found")
                                        time.sleep(2)
                                        pg.moveTo(x, y)
                                        time_ranInt = random.randint(2, 4)
                                        time.sleep(time_ranInt)
                                        x += 70
                                        y -= 40
                                        pg.click(x, y)

                                        time.sleep(0.5)
                                        pg.hotkey("esc") 

                                        time_ranInt = random.randint(2, 4)
                                        time.sleep(time_ranInt)

                                        # Kéo
                                        time_ranInt = random.randint(5, 8)
                                        time_ranReverse = random.randint(-300, -240)
                                        for _ in range(time_ranInt):
                                            pg.scroll(time_ranReverse)
                                            time.sleep(1)
                                            time_ranReverse = random.randint(-250, -200)
                                            pg.scroll(time_ranReverse)
                                            time_ranInt = random.randint(2, 4)
                                            time.sleep(time_ranInt)
                                            break
                                    else: 
                                        time_ranInt = random.randint(5, 8)
                                        time_ranReverse = random.randint(-300, -240)
                                        for _ in range(time_ranInt):
                                            pg.scroll(time_ranReverse)
                                            time.sleep(1)
                                            time_ranReverse = random.randint(-250, -200)
                                            pg.scroll(time_ranReverse)
                                            time_ranInt = random.randint(2, 4)
                                            time.sleep(time_ranInt)
                                            break  
                            elif time_ranInt == 5: 
                                #thương thương
                                time_ranInt = random.randint(2, 6)
                                random_time3 = time_ranInt
                                start_time3 = datetime.datetime.now()
                                run_time3 = datetime.timedelta(seconds = random_time3)
                                while datetime.datetime.now() - start_time3 < run_time3:
                                # while True:
                                    template3 = cv2.imread('likeBtnfb.jpg', cv2.IMREAD_GRAYSCALE) 
                                    screenshot3 = np.array(pg.screenshot())
                                    gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                    result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                    min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
                                    if max_val3 >= 0.8:
                                        x, y = max_loc3
                                        w, h = template3.shape[::-1] 
                                        x += w // 2
                                        y += h // 2
                                        print("Fb like Button Found")
                                        time.sleep(2)
                                        pg.moveTo(x, y)
                                        time_ranInt = random.randint(2, 4)
                                        time.sleep(time_ranInt)
                                        x += 105
                                        y -= 40
                                        pg.click(x, y)

                                        time.sleep(0.5)
                                        pg.hotkey("esc") 

                                        time_ranInt = random.randint(2, 4)
                                        time.sleep(time_ranInt)

                                        # Kéo
                                        time_ranInt = random.randint(5, 8)
                                        time_ranReverse = random.randint(-300, -240)
                                        for _ in range(time_ranInt):
                                            pg.scroll(time_ranReverse)
                                            time.sleep(1)
                                            time_ranReverse = random.randint(-250, -200)
                                            pg.scroll(time_ranReverse)
                                            time_ranInt = random.randint(2, 4)
                                            time.sleep(time_ranInt)
                                            break
                                    else: 
                                        time_ranInt = random.randint(5, 8)
                                        time_ranReverse = random.randint(-300, -240)
                                        for _ in range(time_ranInt):
                                            pg.scroll(time_ranReverse)
                                            time.sleep(1)
                                            time_ranReverse = random.randint(-250, -200)
                                            pg.scroll(time_ranReverse)
                                            time_ranInt = random.randint(2, 4)
                                            time.sleep(time_ranInt)
                                            break  
                            elif time_ranInt == 6: 
                                #thương thương
                                time_ranInt = random.randint(2, 6)
                                random_time3 = time_ranInt
                                start_time3 = datetime.datetime.now()
                                run_time3 = datetime.timedelta(seconds = random_time3)
                                while datetime.datetime.now() - start_time3 < run_time3:
                                # while True:
                                    template3 = cv2.imread('thuongthuong.jpg', cv2.IMREAD_GRAYSCALE) 
                                    screenshot3 = np.array(pg.screenshot())
                                    gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                    result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                    min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
                                    if max_val3 >= 0.8:
                                        x, y = max_loc3
                                        w, h = template3.shape[::-1] 
                                        x += w // 2
                                        y += h // 2
                                        print("Fb like Button Found")
                                        time.sleep(2)
                                        pg.moveTo(x, y)
                                        time_ranInt = random.randint(2, 4)
                                        time.sleep(time_ranInt)
                                        x += 140
                                        y -= 40
                                        pg.click(x, y)
                                        time.sleep(0.5)
                                        pg.hotkey("esc") 

                                        time_ranInt = random.randint(2, 4)
                                        time.sleep(time_ranInt)

                                        # Kéo
                                        time_ranInt = random.randint(5, 8)
                                        time_ranReverse = random.randint(-300, -240)
                                        for _ in range(time_ranInt):
                                            pg.scroll(time_ranReverse)
                                            time.sleep(1)
                                            time_ranReverse = random.randint(-250, -200)
                                            pg.scroll(time_ranReverse)
                                            time_ranInt = random.randint(2, 4)
                                            time.sleep(time_ranInt)
                                            break
                                    else: 
                                        time_ranInt = random.randint(5, 8)
                                        time_ranReverse = random.randint(-300, -240)
                                        for _ in range(time_ranInt):
                                            pg.scroll(time_ranReverse)
                                            time.sleep(1)
                                            time_ranReverse = random.randint(-250, -200)
                                            pg.scroll(time_ranReverse)
                                            time_ranInt = random.randint(2, 4)
                                            time.sleep(time_ranInt)
                                            break 
                        
                        # Kéo
                        time_ranInt = random.randint(5, 8)
                        time_ranReverse = random.randint(-300, -240)
                        for _ in range(time_ranInt):
                            pg.scroll(time_ranReverse)
                            time.sleep(1)
                            time_ranReverse = random.randint(-250, -200)
                            pg.scroll(time_ranReverse)
                            time_ranInt = random.randint(2, 4)
                            time.sleep(time_ranInt)
                            break

                    
                    pg.moveTo(1090, 500)
                    pg.hotkey("ctrl", "w")
                    break # exit the loop
                elif button2_max_val >= 0.8:
                    x, y = button2_max_loc
                    w, h = button2_template.shape[::-1]
                    x += w // 2
                    y += h // 2
                    print("Insta Unfallow Button Found")
                    time.sleep(1)
                    pg.click(x, y)
                    pg.moveTo(1090, 500)
                    time.sleep(1)
                    pg.hotkey("ctrl", "w")
                    break # exit the loop
                else:
                    print("Insta Fallow Unfallow Button Not Found")
                    time.sleep(0.1)
                    elapsed_time = time.time() - start_time
                    print(elapsed_time)
                    if elapsed_time >= 20:
                        print("Elapsed time exceeded 20 seconds, exiting the loop")
                        pg.hotkey("ctrl", "w")
                        break # exit the loop

        confirm.confirmm()