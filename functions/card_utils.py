def hide(card_number):
    # card_number jako string, np. "5290312400019022"
    # ma zwrócić: 2 pierwsze + gwiazdki + 4 ostatnie
    return card_number[:2] + "*" * (len(card_number) - 6) + card_number[-4:]