import random
dice=random.randint(1,6)
ok=dice in [1,6]
print(f'Dice rolled {dice}')
print(f'You have special number: {ok}')