###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = False
light_switch3 = True
bulbs_on = 0
if light_switch1 == True:
    bulbs_on += 1
if light_switch2 == True:
    bulbs_on += 1
if light_switch3 == True:
    bulbs_on += 1
print(f'There are {bulbs_on} bulbs light up')