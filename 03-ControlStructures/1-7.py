###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
bonus = basic_salary * 0.15
is_bonus = input("Do you have a bonus(Yes/No): ")


if is_bonus == "Yes":
    total_salary = basic_salary + bonus
    print(f'Basic salary: {basic_salary}')
    print(f'Bonus included? {is_bonus}')
    print(f'Total salary: {total_salary}')
else:
    print(basic_salary)