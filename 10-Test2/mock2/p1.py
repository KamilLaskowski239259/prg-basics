cards= {
    'A':10,
    'K':10,
    'Q':10,
    'J':10,
    'T':10,
    '9':9,
    '8':8,
    '7':7,
    '6':6,
    '5':5,
    '4':4,
    '3':3,
    '2':2,
}
def f(player1,player2):
    player1_sum = sum(cards[card] for card in player1)
    player2_sum = sum(cards[card] for card in player2)
    return player1_sum > player2_sum
    
print(f('9532','K8'))