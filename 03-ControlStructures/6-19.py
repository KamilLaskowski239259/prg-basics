CompScience=input("Are you interested in computer science? (y/n): ")
Games=input("Do you like playing computer games? (y/n): ")
Insta=input("Do you have an Instagram account? (y/n): ")
if CompScience == 'y':
    question1=True
elif CompScience == 'n':
    question1=False

if Games == 'y':
    question2=True
elif Games == 'n':
    question2=False

if Insta == 'y':
    question3=True
elif Insta == 'n':
    question3=False

if question1==True:
    answer1='Yes'
else:
    answer1='No'

if question2==True:
    answer2='Yes'
else:
    answer2='No'

if question3==True:
    answer3='Yes'
else:
    answer3='No'
print("SURVEY RESULTS")
print(f"Interested in computer science: {answer1}")
print(f"Playing computer games: {answer2}")
print(f"Has an Instagram account: {answer3}")