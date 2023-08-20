# Converting 12 hour time to 24 hour time

def convert_time(hour, minutes, period):
    hour_str = str(hour)
    minute_str = str(minutes)
    if (hour < 1 or hour > 12) or (minutes < 0 or minutes > 59) or (period != "am" and period != "pm"): 
        print(""""
              enter valid time
              Hours : 1 -12
              Minutes: 0 - 59
              Period: am/pm only
              """)  
    else:
        if minutes < 10:
            minute_str = "0" + minute_str
            
        if period == 'am' and hour == 12:
            hour = 0
            hour_str = "00"
            print(f"time is {hour_str}{minute_str}")
        elif period == "am" and hour < 10:
            hour_str = "0" + hour_str
            print(f"time is {hour_str}{minute_str}")
        elif period == "am" and hour > 9:
            print(f"time is {hour}{minute_str}")
        elif period == 'pm' and hour != 12:
            hour += 12
            print(f"time is {hour}{minute_str}")
        elif period == 'pm' and hour == 12:
            hour = 12
            print(f"time is {hour}{minute_str}")  
convert_time(10, 15, "am")            