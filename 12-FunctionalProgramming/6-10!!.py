# Data: Temperatures recorded in cities
data = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Using map() to separate cities and temperatures
cities = list(data.keys())
temperatures = list(data.values())

# Determine chart dimensions
max_temp = max(temperatures)
min_temp = min(temperatures)
chart_height = max_temp - min_temp + 5  # Extra space for better visibility

# Drawing the bar chart
print("Temperature Bar Chart")
print("----------------------")
print("Cities and Temperatures (°C)")
for i in range(chart_height, -1, -1):  # Create rows from top to bottom
    row = f"{i + min_temp:3} | "  # Label for y-axis
    for temp in temperatures:
        if temp >= i + min_temp:
            row += "█ "  # Add a bar segment
        else:
            row += "  "  # Leave space
    print(row)

# Add x-axis and labels
print("    " + "-" * (2 * len(cities) + 1))
print("     " + " ".join(cities))