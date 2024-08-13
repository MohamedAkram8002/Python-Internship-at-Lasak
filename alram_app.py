import time
from datetime import datetime, timedelta

def set_alarm(alarm_time):
    try:
        # Convert the alarm time to a datetime object
        alarm_time_obj = datetime.strptime(alarm_time, "%H:%M")
        now = datetime.now()
        
        # If the alarm time is for the next day, adjust the alarm time accordingly
        if alarm_time_obj.time() <= now.time():
            alarm_time_obj = alarm_time_obj + timedelta(days=1)
        
        # Calculate the difference in time
        time_diff = alarm_time_obj - now
        print(f"Alarm set for {alarm_time_obj.strftime('%H:%M')} which is in {time_diff}.")
        
        # Sleep until the alarm time
        time.sleep(time_diff.total_seconds())
        
        # Trigger the alarm
        print("Wake up! It's time!")
        
    except ValueError:
        print("Invalid time format. Please use HH:MM (24-hour format).")

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM in 24-hour format): ")
    set_alarm(alarm_time)


