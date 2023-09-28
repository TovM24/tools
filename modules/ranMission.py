import random
import datetime
import twitter
import facebook
import ig

def main(): 
    # Random
    random_time = random.randint(20, 30)
    # Đặt thời gian bắt đầu
    start_time = datetime.datetime.now()
    run_time = datetime.timedelta(seconds = random_time)
    
    while datetime.datetime.now() - start_time < run_time: 
        ranNum = random.randint(1, 3)
        if ranNum == 1:
            twitter.nested_loop_Twitter_fallow()
        elif ranNum == 2:
            facebook.nested_loop_Fb_fallow()
        elif ranNum == 3:
            ig.nested_loop_Insta_fallow()
      
      
if __name__ == "__main__":
    main()