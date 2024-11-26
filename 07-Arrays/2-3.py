# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
sum_column_0=sum(row[0] for row in monthly_expenses)
sum_column_1=sum(row[1] for row in monthly_expenses)
sum_column_2=sum(row[2] for row in monthly_expenses)
sum_week1=sum(monthly_expenses[0])
sum_week2=sum(monthly_expenses[1])
sum_week3=sum(monthly_expenses[2])
sum_week4=sum(monthly_expenses[3])
total=sum_column_0+sum_column_1+sum_column_2
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',sum_column_0)
print('Transport:',sum_column_1)
print('Utilities:',sum_column_2)
print('Week 1:',sum_week1)
print('Week 2:',sum_week2)
print('Week 3:',sum_week3)
print('Week 4:',sum_week4)
print('---------------')
print('TOTAL:',total)