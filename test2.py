import pyautogui as pg
import time, keyboard, cv2
import numpy as np
import random
import datetime
import io 
import pyperclip
import array



def confirm():
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


def nested_loop_Twitter_fallow():
    pg.click(557,47)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pg.typewrite("https://wwww.like4like.org/user/earn-twitter.php")
    pg.press('enter')
    pg.moveTo(1090, 500)
    time.sleep(1)
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):  # if key 'esc' is pressed 
            print("Exiting the program...")
            break  # finishing the loop
        start_time = time.time()
        while True:
                button1_template = cv2.imread('tfnomore.png', cv2.IMREAD_GRAYSCALE)
                button2_template = cv2.imread('twfb1.png', cv2.IMREAD_GRAYSCALE)
                screenshot = np.array(pg.screenshot())
                # Chuyển ảnh chụp màn hình sang màu xám 
                gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
                # Dùng để so sánh button1_template với gray_screenshot để tìm kiếm vị trí của mẫu ảnh trên ảnh chụp màn hình
                button1_result = cv2.matchTemplate(gray_screenshot, button1_template, cv2.TM_CCOEFF_NORMED)
                # Dùng để so sánh button2_template với gray_screenshot để tìm kiếm vị trí của mẫu ảnh trên ảnh chụp màn hình
                button2_result = cv2.matchTemplate(gray_screenshot, button2_template, cv2.TM_CCOEFF_NORMED)
                button1_min_val, button1_max_val, button1_min_loc, button1_max_loc = cv2.minMaxLoc(button1_result)
                button2_min_val, button2_max_val, button2_min_loc, button2_max_loc = cv2.minMaxLoc(button2_result)
                if button1_max_val >= 0.8:
                    x, y = button1_max_loc
                    w, h = button1_template.shape[::-1]
                    x += w // 2
                    y += h // 2
                    print("Twitter Earnings No More Button Found")
                    time.sleep(0.5)
                    nested_loop_Fb_fallow()

                elif button2_max_val >= 0.8:
                    # x và y là tọa độ của góc trái trên cùng của nút
                    x, y = button2_max_loc
                    # lấy kích thước của mẫu ảnh rồi đảo ngược thứ tự phần tử
                    w, h = button2_template.shape[::-1]
                    # Điều chỉnh tọa độ vào tâm nút
                    x += w // 2
                    y += h // 2
                    print("Twitter Earing Button Found")
                    time.sleep(1)
                    pg.click(x, y)
                    # pg.moveTo(1090, 500)
                    time.sleep(1)
                    break                   
                else:
                    print("Buttons are Not Found Please Check The Images Or check The Program")
                    time.sleep(0.1)
                    elapsed_time = time.time() - start_time
                    print(start_time)
                    print(elapsed_time)
                    if elapsed_time >= 20:
                        print("Elapsed time exceeded 20 seconds, exiting the loop")
                        nested_loop_Fb_fallow()
                        break # exit the loop
        time.sleep(2)
        start_time = time.time()
        while True:
            # Đọc và chuyển sang mảng dữ liệu NumPy với chế độ màu xám
            template = cv2.imread('twt.jpg', cv2.IMREAD_GRAYSCALE)  
            
            # chụp màn hình lại vf chuyển sang dữ liệu mảng NumPy
            screenshot = np.array(pg.screenshot())
            # Chuyển đổi ảnh chụp màn hình sang màu xám 
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            
            # gray_screenshot: Là ảnh màn hình đã chụp ở chế độ màu xám, là một mảng NumPy.
            # template: Là mẫu ảnh cần so sánh, cũng ở chế độ màu xám, là một mảng NumPy được đọc từ tệp twt.jpg.
            # cv2.TM_CCOEFF_NORMED: Đây là một phương pháp so sánh mẫu cụ thể. cv2.TM_CCOEFF_NORMED sử dụng hệ số tương quan tối đa chuẩn hóa để tìm kiếm mẫu
            # So sánh mẫu với ảnh chụp màn hình ở chế độ màu xám
            result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if max_val >= 0.8:
                # Tọa độ của góc trên bên trái khu vực trùng khớp tốt nhất  
                x, y = max_loc
                # lấy kích thước của mẫu ảnh rồi đảo ngược thứ tự các phần tử
                w, h = template.shape[::-1]
                x += w // 2
                y += h // 2
                print("Twitter Fallow Button Found")
                time.sleep(0.5)
                pg.click(x, y)
                time.sleep(1)
                pg.hotkey("alt", "tab")
                confirm()      
                pg.hotkey("alt", "tab")
                
                
                ###########################################################################################
                
                # Random
                random_time = random.uniform(15, 20)
                # Đặt thời gian bắt đầu
                start_time = datetime.datetime.now()
                run_time = datetime.timedelta(seconds = random_time)
                
                while datetime.datetime.now() - start_time < run_time: 
                    template2 = cv2.imread('logo_tt.jpg', cv2.IMREAD_GRAYSCALE) 
                    screenshot2 = np.array(pg.screenshot())
                    gray_screenshot2 = cv2.cvtColor(screenshot2, cv2.COLOR_BGR2GRAY)
                    result2 = cv2.matchTemplate(gray_screenshot2, template2, cv2.TM_CCOEFF_NORMED)
                    min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)
                    
                    # click vào logo
                    if max_val2 >= 0.8:
                        x, y = max_loc2
                        w, h = template2.shape[::-1] 
                        x += w // 2
                        y += h // 2
                        print("Twitter logo Button Found")
                        pg.click(x, y)
                        time.sleep(1)
                    
                    # Kéo   
                    scroll_count = 3
                    for _ in range(scroll_count):
                        pg.scroll(-110)
                        time.sleep(1)
                        pg.scroll(-100)
                        time.sleep(0.5)
                        
                        # Like
                        random_time3 = random.uniform(2, 6)
                        start_time3 = datetime.datetime.now()
                        run_time3 = datetime.timedelta(seconds = int(random_time3))
                        while datetime.datetime.now() - start_time3 < run_time3:
                        # while True:
                            template3 = cv2.imread('likeBtntw.jpg', cv2.IMREAD_GRAYSCALE) 
                            screenshot3 = np.array(pg.screenshot())
                            gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                            result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                            min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
                            if max_val3 >= 0.8:
                                x, y = max_loc3
                                w, h = template3.shape[::-1] 
                                x += w // 2
                                y += h // 2
                                print("Twitter like Button Found")
                                time.sleep(0.5)
                                pg.click(x, y)
                                time.sleep(1)
                                # Kéo
                                for _ in range(scroll_count):
                                    pg.scroll(-150)
                                    time.sleep(0.5)
                                    break
                            else: 
                                for _ in range(scroll_count):
                                    pg.scroll(-150)
                                    time.sleep(0.5)
                                    break           
                
                ################################################################################################
                
                # pg.moveTo(1090, 500)
                pg.hotkey("ctrl", "w")
                # nested_loop_Twitter_fallow()
                break # exit the loop
            else:
                print("Twitter Fallow Button Not Found")
                time.sleep(0.01)
                elapsed_time = time.time() - start_time
                print(elapsed_time, "Second and If not Found In 30 Seconds Closing The Loop")
                if elapsed_time >= 3:
                    print("Elapsed time exceeded 30 seconds, exiting the loop")
                    pg.hotkey("ctrl", "w")
                    break # exit the loop     
        confirm()   
        
        
        
def nested_loop_Fb_fallow():
    pg.click(557,47)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pg.typewrite("https://wwww.like4like.org/user/earn-facebook-subscribes.php")
    pg.press('enter')
    pg.moveTo(1090, 500)
    time_ranInt = random.randint(2, 4)
    time.sleep(time_ranInt)
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):  # if key 'esc' is pressed 
            print("Exiting the program...")
            break  # finishing the loop
        time_ranInt = random.randint(2, 5)
        time.sleep(time_ranInt)
        start_time = time.time()
        while True:
            button1_template = cv2.imread('tfnomore.png', cv2.IMREAD_GRAYSCALE)
            button2_template = cv2.imread('instafollow1.png', cv2.IMREAD_GRAYSCALE)
            screenshot = np.array(pg.screenshot())
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            button1_result = cv2.matchTemplate(gray_screenshot, button1_template, cv2.TM_CCOEFF_NORMED)
            button2_result = cv2.matchTemplate(gray_screenshot, button2_template, cv2.TM_CCOEFF_NORMED)
            button1_min_val, button1_max_val, button1_min_loc, button1_max_loc = cv2.minMaxLoc(button1_result)
            button2_min_val, button2_max_val, button2_min_loc, button2_max_loc = cv2.minMaxLoc(button2_result)
            if button1_max_val >= 0.8:
                x, y = button1_max_loc
                w, h = button1_template.shape[::-1]
                x += w // 2
                y += h // 2
                print("Instagram Earnings No More Found")
                time.sleep(0.5)
                # nested_loop_Insta_fallow()
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
                    # nested_loop_Insta_fallow() 
                    break
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

                    # Random
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


                            time_ranInt = random.randint(1, 8) # 1 ==> 8
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
                            elif time_ranInt == 7:
                                template3 = cv2.imread('commentBtnfb.jpg', cv2.IMREAD_GRAYSCALE)
                                screenshot3 = np.array(pg.screenshot())
                                gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)  

                                if max_val3 >= 0.8:
                                    x, y = max_loc3
                                    w, h = template3.shape[::-1] 
                                    x += w // 2
                                    y += h // 2
                                    print("FB comment Button Found")
                                    time.sleep(0.5)
                                    pg.click(x, y)
                                    time.sleep(2)
                                    
                                    # Khởi tạo một mảng rỗng để lưu trữ dữ liệu từ tệp văn bản
                                    data_array = []
                                    with open('comment.txt', mode = "r", encoding = "utf-8") as file:
                                        for line in file:
                                            # Loại bỏ khoảng trắng và ký tự xuống dòng (newline character) nếu cần
                                            line = line.strip()
                                            # Thêm dòng vào mảng
                                            data_array.append(line)
                                    file.close()
                                    
                                    random_comment = random.randint(0, 11472)
                                    comment_text = data_array[random_comment]
                                    pyperclip.copy(comment_text)
                                    pg.hotkey("ctrl", "v")
                                    
                                    time_ranInt = random.randint(2, 4)
                                    time.sleep(time_ranInt)
                                    pg.hotkey("enter") 

                                    time_ranInt = random.randint(2, 4)
                                    time.sleep(time_ranInt)
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
                            elif time_ranInt == 8:
                                time_ranInt = random.randint(2, 6)
                                random_time3 = time_ranInt
                                start_time3 = datetime.datetime.now()
                                run_time3 = datetime.timedelta(seconds = random_time3)
                                while datetime.datetime.now() - start_time3 < run_time3:
                                # while True:
                                    template3 = cv2.imread('shareBtnfb.jpg', cv2.IMREAD_GRAYSCALE) 
                                    screenshot3 = np.array(pg.screenshot())
                                    gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                    result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                    min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
                                    if max_val3 >= 0.8:
                                        x, y = max_loc3
                                        w, h = template3.shape[::-1] 
                                        x += w // 2
                                        y += h // 2
                                        print("Fb share Button Found")
                                        time.sleep(2)
                                        pg.click(x, y)
                                        time.sleep(1)

                                        template4 = cv2.imread('shareBtnop.jpg', cv2.IMREAD_GRAYSCALE) 
                                        screenshot4 = np.array(pg.screenshot())
                                        gray_screenshot4 = cv2.cvtColor(screenshot4, cv2.COLOR_BGR2GRAY)
                                        result4 = cv2.matchTemplate(gray_screenshot4, template4, cv2.TM_CCOEFF_NORMED)
                                        min_val4, max_val4, min_loc4, max_loc4 = cv2.minMaxLoc(result4)
                                        if max_val4 >= 0.8:
                                            x, y = max_loc4
                                            w, h = template4.shape[::-1] 
                                            x += w // 2
                                            y += h // 2
                                            print("Fb share option Button Found")
                                            time.sleep(2)
                                            pg.click(x, y)
                                            time.sleep(1)
                                            pg.hotkey("esc") 
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

        confirm()   
        
        
def nested_loop_Insta_fallow():
    pg.click(557,47)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pg.typewrite("https://wwww.like4like.org/user/earn-instagram-follow.php")
    pg.press('enter')
    pg.moveTo(1090, 500)
    time_ranInt = random.randint(2, 4)
    time.sleep(time_ranInt)
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):  # if key 'esc' is pressed 
            print("Exiting the program...")
            break  # finishing the loop
        time_ranInt = random.randint(2, 5)
        time.sleep(time_ranInt)
        start_time = time.time()
        while True:
            button1_template = cv2.imread('tfnomore.png', cv2.IMREAD_GRAYSCALE)
            button2_template = cv2.imread('instafollow1.png', cv2.IMREAD_GRAYSCALE)
            screenshot = np.array(pg.screenshot())
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            button1_result = cv2.matchTemplate(gray_screenshot, button1_template, cv2.TM_CCOEFF_NORMED)
            button2_result = cv2.matchTemplate(gray_screenshot, button2_template, cv2.TM_CCOEFF_NORMED)
            button1_min_val, button1_max_val, button1_min_loc, button1_max_loc = cv2.minMaxLoc(button1_result)
            button2_min_val, button2_max_val, button2_min_loc, button2_max_loc = cv2.minMaxLoc(button2_result)
            if button1_max_val >= 0.8:
                x, y = button1_max_loc
                w, h = button1_template.shape[::-1]
                x += w // 2
                y += h // 2
                print("Instagram Earnings No More Found")
                time.sleep(0.5)
                nested_loop_Twitter_fallow()
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
                    nested_loop_Twitter_fallow() 
                    break
        start_time = time.time()  
        time.sleep(4)    
        while True:
                time_ranInt = random.randint(6, 9)
                time.sleep(time_ranInt)
                button1_template = cv2.imread('igFl.jpg', cv2.IMREAD_GRAYSCALE)
                screenshot = np.array(pg.screenshot())
                gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
                button1_result = cv2.matchTemplate(gray_screenshot, button1_template, cv2.TM_CCOEFF_NORMED)
                button1_min_val, button1_max_val, button1_min_loc, button1_max_loc = cv2.minMaxLoc(button1_result)
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

                    # Logo
                    template2 = cv2.imread('igLg.jpg', cv2.IMREAD_GRAYSCALE)
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
                        print("ig logo Button Found")
                        time_ranInt = random.randint(1, 3)
                        print(time_ranInt)
                        time.sleep(time_ranInt)
                        pg.click(x, y)
                        time_ranInt = random.randint(1, 3)
                        time.sleep(time_ranInt)
                        
                    time_ranInts = random.randint(1, 2) # 1 ==> 3
                    if time_ranInts == 1: 
                        # Random
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


                                time_ranInt = random.randint(1, 3) # 1 ==> 3
                                if time_ranInt == 1: 
                                    template3 = cv2.imread('igC.jpg', cv2.IMREAD_GRAYSCALE)
                                    screenshot3 = np.array(pg.screenshot())
                                    gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                    result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                    min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)  

                                    if max_val3 >= 0.8:
                                        x, y = max_loc3
                                        w, h = template3.shape[::-1] 
                                        x += w // 2
                                        y += h // 2
                                        print("FB comment Button Found")
                                        time.sleep(0.5)
                                        pg.moveTo(x, y)
                                        time_ranInt = random.randint(2, 3)
                                        time.sleep(time_ranInt)
                                        x -= 40
                                        pg.click(x, y)
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
                                        
                                elif time_ranInt == 2: 
                                    template3 = cv2.imread('igC.jpg', cv2.IMREAD_GRAYSCALE)
                                    screenshot3 = np.array(pg.screenshot())
                                    gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                    result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                    min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)  

                                    if max_val3 >= 0.8:
                                        x, y = max_loc3
                                        w, h = template3.shape[::-1] 
                                        x += w // 2
                                        y += h // 2
                                        print("FB comment Button Found")
                                        time.sleep(0.5)
                                        pg.click(x, y)
                                        time.sleep(2)
                                        
                                        template4 = cv2.imread('igCT.jpg', cv2.IMREAD_GRAYSCALE)
                                        screenshot4 = np.array(pg.screenshot())
                                        gray_screenshot4 = cv2.cvtColor(screenshot4, cv2.COLOR_BGR2GRAY)
                                        result4 = cv2.matchTemplate(gray_screenshot4, template4, cv2.TM_CCOEFF_NORMED)
                                        min_val4, max_val4, min_loc4, max_loc4 = cv2.minMaxLoc(result4)  
                                        if max_val4 >= 0.8:
                                            x, y = max_loc4
                                            w, h = template4.shape[::-1] 
                                            x += w // 2
                                            y += h // 2
                                            print("ig comment Button Found")
                                            time.sleep(0.5)
                                            pg.click(x, y)
                                            time.sleep(2)
                                        
                                            # Khởi tạo một mảng rỗng để lưu trữ dữ liệu từ tệp văn bản
                                            data_array = []
                                            with open('comment.txt', mode = "r", encoding = "utf-8") as file:
                                                for line in file:
                                                    # Loại bỏ khoảng trắng và ký tự xuống dòng (newline character) nếu cần
                                                    line = line.strip()
                                                    # Thêm dòng vào mảng
                                                    data_array.append(line)
                                            file.close()
                                            
                                            random_comment = random.randint(0, 11472)
                                            comment_text = data_array[random_comment]
                                            pyperclip.copy(comment_text)
                                            pg.hotkey("ctrl", "v")
                                            
                                            time_ranInt = random.randint(2, 4)
                                            time.sleep(time_ranInt)
                                            pg.hotkey("enter") 

                                            time_ranInt = random.randint(4, 6)
                                            time.sleep(time_ranInt)
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
                                elif time_ranInt == 3:
                                    #save
                                    time_ranInt = random.randint(2, 6)
                                    random_time3 = time_ranInt
                                    start_time3 = datetime.datetime.now()
                                    run_time3 = datetime.timedelta(seconds = random_time3)
                                    while datetime.datetime.now() - start_time3 < run_time3:
                                    # while True:
                                        template3 = cv2.imread('igS.jpg', cv2.IMREAD_GRAYSCALE) 
                                        screenshot3 = np.array(pg.screenshot())
                                        gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                        result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                        min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
                                        if max_val3 >= 0.8:
                                            x, y = max_loc3
                                            w, h = template3.shape[::-1] 
                                            x += w // 2
                                            y += h // 2
                                            print("ig like Button Found")
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
                    elif time_ranInts == 2: 
                        template3 = cv2.imread('igReels.jpg', cv2.IMREAD_GRAYSCALE)
                        screenshot3 = np.array(pg.screenshot())
                        gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                        result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                        min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)  

                        if max_val3 >= 0.8:
                            x, y = max_loc3
                            w, h = template3.shape[::-1] 
                            x += w // 2
                            y += h // 2
                            print("FB comment Button Found")
                            time.sleep(0.5)
                            pg.click(x, y)
                            time.sleep(2)
                        
                            # Kéo
                            time_ranInt = random.randint(5, 8)
                            time_ranReverse = random.randint(-300, -240)
                            for _ in range(time_ranInt):
                                pg.scroll(time_ranReverse)
                                time.sleep(1)
                                time_ranReverse = random.randint(-250, -200)
                                pg.scroll(time_ranReverse)
                                time_ranReverse = random.randint(-250, -200)
                                pg.scroll(time_ranReverse)
                                
                                #thích  
                                template3 = cv2.imread('igC.jpg', cv2.IMREAD_GRAYSCALE)
                                screenshot3 = np.array(pg.screenshot())
                                gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)  

                                if max_val3 >= 0.8:
                                    x, y = max_loc3
                                    w, h = template3.shape[::-1] 
                                    x += w // 2
                                    y += h // 2
                                    print("FB comment Button Found")
                                    time.sleep(0.5)
                                    pg.moveTo(x, y)
                                    time_ranInt = random.randint(2, 3)
                                    time.sleep(time_ranInt)
                                    y -= 60
                                    pg.click(x, y)
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
                            
                            time_ranReverse = random.randint(-250, -200)
                            pg.scroll(time_ranReverse)
                            time_ranInt = random.randint(2, 4)
                            time.sleep(time_ranInt)
                            
                            #thích  
                            time_ranInt = random.randint(2, 6)
                            random_time3 = time_ranInt
                            start_time3 = datetime.datetime.now()
                            run_time3 = datetime.timedelta(seconds = random_time3)
                            while datetime.datetime.now() - start_time3 < run_time3:
                            # while True:
                                template3 = cv2.imread('igL.jpg', cv2.IMREAD_GRAYSCALE) 
                                screenshot3 = np.array(pg.screenshot())
                                gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
                                if max_val3 >= 0.8:
                                    x, y = max_loc3
                                    w, h = template3.shape[::-1] 
                                    x += w // 2
                                    y += h // 2
                                    print("ig like Button Found")
                                    time.sleep(2)
                                    pg.click(x, y)
                                    time.sleep(1)

                    
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

        confirm()  
        
        
def nested_loop_Insta_likes():
    pg.click(557,47)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pg.typewrite("https://wwww.like4like.org/user/earn-instagram-like.php")
    pg.press('enter')
    pg.moveTo(1090, 500)
    time_ranInt = random.randint(2, 4)
    time.sleep(time_ranInt)
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):  # if key 'esc' is pressed 
            print("Exiting the program...")
            break
        time_ranInt = random.randint(2, 5)
        time.sleep(time_ranInt)
        start_time = time.time()
        while True:
            button1_template = cv2.imread('tfnomore.png', cv2.IMREAD_GRAYSCALE)
            button2_template = cv2.imread('igLBtn.png', cv2.IMREAD_GRAYSCALE)
            screenshot = np.array(pg.screenshot())
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            button1_result = cv2.matchTemplate(gray_screenshot, button1_template, cv2.TM_CCOEFF_NORMED)
            button2_result = cv2.matchTemplate(gray_screenshot, button2_template, cv2.TM_CCOEFF_NORMED)
            button1_min_val, button1_max_val, button1_min_loc, button1_max_loc = cv2.minMaxLoc(button1_result)
            button2_min_val, button2_max_val, button2_min_loc, button2_max_loc = cv2.minMaxLoc(button2_result)
            if button1_max_val >= 0.8:
                x, y = button1_max_loc
                w, h = button1_template.shape[::-1]
                x += w // 2
                y += h // 2
                print("Instagram Earnings No More Found")
                time.sleep(0.5)
                nested_loop_Twitter_fallow()
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
                    nested_loop_Twitter_fallow() 
                    break
        start_time = time.time()  
        time.sleep(4)    
        while True:
                time_ranInt = random.randint(6, 9)
                time.sleep(time_ranInt)
                button1_template = cv2.imread('igSBtn.jpg', cv2.IMREAD_GRAYSCALE)
                screenshot = np.array(pg.screenshot())
                gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
                button1_result = cv2.matchTemplate(gray_screenshot, button1_template, cv2.TM_CCOEFF_NORMED)
                button1_min_val, button1_max_val, button1_min_loc, button1_max_loc = cv2.minMaxLoc(button1_result)
                if button1_max_val >= 0.8:
                    x, y = button1_max_loc
                    w, h = button1_template.shape[::-1]
                    x += w // 2
                    y += h // 2
                    print("Fb Follow Button Found")
                    time_ranInt = random.randint(6, 9)
                    print(time_ranInt)
                    time.sleep(time_ranInt)
                    pg.moveTo(x, y)
                    time.sleep(1)
                    pg.click(x, y)
                    time.sleep(2)
                    pg.hotkey("alt", "tab")
                    confirm()      
                    pg.hotkey("alt", "tab")
                    time.sleep(1)

                    # Logo
                    template2 = cv2.imread('igLg.jpg', cv2.IMREAD_GRAYSCALE)
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
                        print("ig logo Button Found")
                        time_ranInt = random.randint(1, 3)
                        print(time_ranInt)
                        time.sleep(time_ranInt)
                        pg.click(x, y)
                        time_ranInt = random.randint(1, 3)
                        time.sleep(time_ranInt)
                        
                    time_ranInts = random.randint(1, 2) # 1 ==> 3
                    if time_ranInts == 1: 
                        # Random
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


                                time_ranInt = random.randint(1, 3) # 1 ==> 3
                                if time_ranInt == 1: 
                                    template3 = cv2.imread('igC.jpg', cv2.IMREAD_GRAYSCALE)
                                    screenshot3 = np.array(pg.screenshot())
                                    gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                    result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                    min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)  

                                    if max_val3 >= 0.8:
                                        x, y = max_loc3
                                        w, h = template3.shape[::-1] 
                                        x += w // 2
                                        y += h // 2
                                        print("FB comment Button Found")
                                        time.sleep(0.5)
                                        pg.moveTo(x, y)
                                        time_ranInt = random.randint(2, 3)
                                        time.sleep(time_ranInt)
                                        x -= 40
                                        pg.click(x, y)
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
                                        
                                elif time_ranInt == 2: 
                                    template3 = cv2.imread('igC.jpg', cv2.IMREAD_GRAYSCALE)
                                    screenshot3 = np.array(pg.screenshot())
                                    gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                    result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                    min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)   

                                    if max_val3 >= 0.8:
                                        x, y = max_loc3
                                        w, h = template3.shape[::-1] 
                                        x += w // 2
                                        y += h // 2
                                        print("FB comment Button Found")
                                        time.sleep(0.5)
                                        pg.click(x, y)
                                        time.sleep(2)
                                        
                                        template4 = cv2.imread('igCT.jpg', cv2.IMREAD_GRAYSCALE)
                                        screenshot4 = np.array(pg.screenshot())
                                        gray_screenshot4 = cv2.cvtColor(screenshot4, cv2.COLOR_BGR2GRAY)
                                        result4 = cv2.matchTemplate(gray_screenshot4, template4, cv2.TM_CCOEFF_NORMED)
                                        min_val4, max_val4, min_loc4, max_loc4 = cv2.minMaxLoc(result4)  
                                        if max_val4 >= 0.8:
                                            x, y = max_loc4
                                            w, h = template4.shape[::-1] 
                                            x += w // 2
                                            y += h // 2
                                            print("ig comment Button Found")
                                            time.sleep(0.5)
                                            pg.click(x, y)
                                            time.sleep(2)
                                        
                                            # Khởi tạo một mảng rỗng để lưu trữ dữ liệu từ tệp văn bản
                                            data_array = []
                                            with open('comment.txt', mode = "r", encoding = "utf-8") as file:
                                                for line in file:
                                                    # Loại bỏ khoảng trắng và ký tự xuống dòng (newline character) nếu cần
                                                    line = line.strip()
                                                    # Thêm dòng vào mảng
                                                    data_array.append(line)
                                            file.close()
                                            
                                            random_comment = random.randint(0, 11472)
                                            comment_text = data_array[random_comment]
                                            pyperclip.copy(comment_text)
                                            pg.hotkey("ctrl", "v")
                                            
                                            time_ranInt = random.randint(2, 4)
                                            time.sleep(time_ranInt)
                                            pg.hotkey("enter") 

                                            time_ranInt = random.randint(4, 6)
                                            time.sleep(time_ranInt)
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
                                elif time_ranInt == 3:
                                    #save
                                    time_ranInt = random.randint(2, 6)
                                    random_time3 = time_ranInt
                                    start_time3 = datetime.datetime.now()
                                    run_time3 = datetime.timedelta(seconds = random_time3)
                                    while datetime.datetime.now() - start_time3 < run_time3:
                                    # while True:
                                        template3 = cv2.imread('igS.jpg', cv2.IMREAD_GRAYSCALE) 
                                        screenshot3 = np.array(pg.screenshot())
                                        gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                        result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                        min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
                                        if max_val3 >= 0.8:
                                            x, y = max_loc3
                                            w, h = template3.shape[::-1] 
                                            x += w // 2
                                            y += h // 2
                                            print("ig like Button Found")
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
                    elif time_ranInts == 2: 
                        template3 = cv2.imread('igReels.jpg', cv2.IMREAD_GRAYSCALE)
                        screenshot3 = np.array(pg.screenshot())
                        gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                        result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                        min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)  

                        if max_val3 >= 0.8:
                            x, y = max_loc3
                            w, h = template3.shape[::-1] 
                            x += w // 2
                            y += h // 2
                            print("FB comment Button Found")
                            time.sleep(0.5)
                            pg.click(x, y)
                            time.sleep(2)
                        
                            # Kéo
                            time_ranInt = random.randint(5, 8)
                            time_ranReverse = random.randint(-300, -240)
                            for _ in range(time_ranInt):
                                pg.scroll(time_ranReverse)
                                time.sleep(1)
                                time_ranReverse = random.randint(-250, -200)
                                pg.scroll(time_ranReverse)
                                time_ranReverse = random.randint(-250, -200)
                                pg.scroll(time_ranReverse)
                                
                                #thích  
                                time_ranInt = random.randint(2, 6)
                                random_time3 = time_ranInt
                                start_time3 = datetime.datetime.now()
                                run_time3 = datetime.timedelta(seconds = random_time3)
                                while datetime.datetime.now() - start_time3 < run_time3:
                                    # while True:
                                    template3 = cv2.imread('igL.jpg', cv2.IMREAD_GRAYSCALE) 
                                    screenshot3 = np.array(pg.screenshot())
                                    gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                    result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                    min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
                                    if max_val3 >= 0.8:
                                        x, y = max_loc3
                                        w, h = template3.shape[::-1] 
                                        x += w // 2
                                        y += h // 2
                                        print("ig like Button Found")
                                        time.sleep(2)
                                        pg.click(x, y)
                                        time.sleep(1)
                                break
                            
                            time_ranReverse = random.randint(-250, -200)
                            pg.scroll(time_ranReverse)
                            time_ranInt = random.randint(2, 4)
                            time.sleep(time_ranInt)
                            
                            #thích  
                            time_ranInt = random.randint(2, 6)
                            random_time3 = time_ranInt
                            start_time3 = datetime.datetime.now()
                            run_time3 = datetime.timedelta(seconds = random_time3)
                            while datetime.datetime.now() - start_time3 < run_time3:
                            # while True:
                                template3 = cv2.imread('igL.jpg', cv2.IMREAD_GRAYSCALE) 
                                screenshot3 = np.array(pg.screenshot())
                                gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
                                result3 = cv2.matchTemplate(gray_screenshot3, template3, cv2.TM_CCOEFF_NORMED)
                                min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
                                if max_val3 >= 0.8:
                                    x, y = max_loc3
                                    w, h = template3.shape[::-1] 
                                    x += w // 2
                                    y += h // 2
                                    print("ig like Button Found")
                                    time.sleep(2)
                                    pg.click(x, y)
                                    time.sleep(1)

                    
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

        confirm()   


pg.click(557,47)
# nested_loop_Twitter_fallow()
nested_loop_Fb_fallow()
# nested_loop_Insta_fallow()




# nested_loop_Insta_likes()