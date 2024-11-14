def f(card_number):
    first_two=card_number[:2]
    last_four=card_number[-4:]
    middle_part= '*' * (len(card_number)-6)
    masked_card_number=first_two+middle_part+last_four
    return masked_card_number
print(f("5290312400019022"))