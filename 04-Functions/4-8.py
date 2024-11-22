def time_string(hours, minutes, time_format):
    if time_format == "12":
        period = "AM"
        if hours >= 12:
            period = "PM"
            if hours > 12:
                hours -= 12
        return f"{hours}:{minutes:02d} {period}"
    elif time_format == "24":
        return f"{hours:02d}:{minutes:02d}"
    else:
        return "Invalid time format"

# Example usage:
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
time_format = input("Enter time format (12/24): ")
print(time_string(hours, minutes, time_format))
