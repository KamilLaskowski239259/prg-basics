categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
max_value = max(expenses)
max_index=expenses.index(max_value)
print(categories[max_index]+" "+str(expenses[max_index]))
