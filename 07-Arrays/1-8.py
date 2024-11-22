computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
computer_games_sorted=sorted(computer_games)
number = 0
number2 = 1
while number < 10:
    print(f"{number2}. {computer_games_sorted[number]}")
    number+=1
    number2+=1
    