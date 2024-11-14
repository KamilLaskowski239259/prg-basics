def f(amount_to_pay):
    coins = 0
    coins += amount_to_pay // 5
    amount_to_pay %= 5
    coins += amount_to_pay // 2
    amount_to_pay %= 2
    coins += amount_to_pay
    return coins
amount = int(input("Amount to pay: "))
result = f(amount)
print(f"f({amount}) returns {result}")