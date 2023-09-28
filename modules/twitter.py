import pyautogui as pg
import time, keyboard, cv2
import numpy as np
import random
import datetime
import confirm
import ranMission




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
                button1_template = cv2.imread('../imgBug/tfnomore.png', cv2.IMREAD_GRAYSCALE)
                button2_template = cv2.imread('../imgFollow/twfb1.png', cv2.IMREAD_GRAYSCALE)
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
                    ranMission.main()

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
                        ranMission.main()
                        break # exit the loop
        time.sleep(2)
        start_time = time.time()
        while True:
            # Đọc và chuyển sang mảng dữ liệu NumPy với chế độ màu xám
            template = cv2.imread('../imgFollow/twt.jpg', cv2.IMREAD_GRAYSCALE)  
            
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
                    template2 = cv2.imread('../imgLogo/logo_tt.jpg', cv2.IMREAD_GRAYSCALE) 
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
                            template3 = cv2.imread('../imgFeeling/likeBtntw.jpg', cv2.IMREAD_GRAYSCALE) 
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
    
    confirm.confirmm()
        
        
        
if __name__ == "__main__":
    pass