facebok = True
Twitter = False
Instagram = True

if (facebok and Twitter) or (facebok and Instagram) or (Twitter and Instagram) == True:
    print("You are a good influencer! ")
else:
    print("You are NOT a good influencer! ")
