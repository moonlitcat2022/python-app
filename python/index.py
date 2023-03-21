import time

def timer_start(length_of_timer):
    seconds_sence_start = 0
    while length_of_timer > seconds_sence_start:
        time.sleep(1)
        seconds_sence_start = seconds_sence_start + 1
        print(seconds_sence_start)
timer_start(int(input()))

#input funtion here 
