# Converting 12 hour time to 24 hour time

def convert_time(hour, minutes, period):
    hour_str = str(hour)
    minute_str = str(minutes)
    if (hour < 1 or hour > 12) or (minutes < 0 or minutes > 59) or (period != "am" and period != "pm"): 
        print("enter valid time")  
    else:
        if period == 'am' and hour == 12:
            hour = 0
            hour_str = "00"
            print(f"time is {hour_str}:{minutes}:{period}")
        elif period == 'pm' and hour != 12:
            hour += 12
            print(f"time is {hour}:{minutes}:{period}")
        elif period == 'pm' and hour == 12:
            hour = 12
            print(f"time is {hour}:{minutes}:{period}")   
        elif len(minute_str) != 2:
            minute_str = "0" + minute_str
            print(minute_str)
            print(f"time is {hour}:{minute_str}:{period}") 

                     
    
convert_time(1, 0, "pm")