###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
sum_even = 0

# Calculate the sum of even numbers
i=1 
while i <= N:
    if i % 2 == 0:
        sum_even += i

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")