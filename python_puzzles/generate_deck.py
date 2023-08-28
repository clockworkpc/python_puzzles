def generate_card(key, suit, colour):
    hsh = {"key": key, "suit": suit, "colour": colour}
    return hsh


def generate_suit(keys, suit, colour):
    ary = []
    for key in keys:
        ary.append(generate_card(key, suit, colour))
    return ary


def card_names():
    name_ary = []

    for i in range(1, 11):
        name_ary.append(str(i))
    for k in ["jack", "queen", "king"]:
        name_ary.append(k)

    return name_ary


def main():
    cards = []
    names = card_names()

    clubs = generate_suit(names, "clubs", "black")
    hearts = generate_suit(names, "hearts", "red")
    spades = generate_suit(names, "spades", "black")
    diamonds = generate_suit(names, "diamonds", "red")

    blacks = []
    reds = []

    for card in clubs:
        blacks.append(card)
        cards.append(card)

    for card in hearts:
        reds.append(card)
        cards.append(card)

    for card in spades:
        blacks.append(card)
        cards.append(card)

    for card in diamonds:
        reds.append(card)
        cards.append(card)

    deck = {
        "clubs": clubs,
        "hearts": hearts,
        "spades": spades,
        "diamonds": diamonds,
        "reds": reds,
        "blacks": blacks,
        "cards": cards,
    }

    return deck
