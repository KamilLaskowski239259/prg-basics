time_24 = input("Enter time (24-hour format, hh:mm): ")
hours = int(time_24[:2])
minutes = int(time_24[3:])
if hours == 0:
    hours_12 = 12
    period = "am"
elif hours < 12:
    hours_12 = hours
    period = "am"
elif hours == 12:
    hours_12 = 12
    period = "pm"
else:
    hours_12 = hours - 12
    period = "pm"
if minutes < 10:
    minutes_str = "0" + str(minutes)
else:
    minutes_str = str(minutes)
print(f"Time in 12-hour format: {hours_12}:{minutes_str}{period}")