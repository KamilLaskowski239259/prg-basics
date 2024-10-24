number=int(input("Number: "))
if number>0:
    ok='positive'
elif number==0:
    ok="0"
elif number<0:
    ok='negative'
print(f'Nuber {number} is {ok}')