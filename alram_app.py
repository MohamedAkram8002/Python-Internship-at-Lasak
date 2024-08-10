import datetime
import time

def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}")
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            break
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the time for the alarm (HH:MM:SS): ")
    set_alarm(alarm_time)
