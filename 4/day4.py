from collections import Counter
def part_one():
    res = 0
    with open("input") as f:
        for card in f.readlines():
            card_data = card.split(":")
            numbers_win, mynums = card_data[1].split("|")
            wining_n = list(set(numbers_win.split()) & set(mynums.split()))
            if wining_n:
                res += 2 ** (len(wining_n) - 1)
                
    print(res)

def part_two():
    res = 0
    cards = Counter()
    with open("input") as f:
        for card in f.readlines():
            card_data = card.split(":")
            card_n = int(card_data[0].split()[-1])
            numbers_win, mynums = card_data[1].split("|")
            wining_n = list(set(numbers_win.split()) & set(mynums.split()))
            cards[card_n] += 1 
            for c in (list(range(card_n + 1, len(wining_n) + int(card_n) + 1))):
                cards[c] += cards[card_n]
                
                
    print(sum(cards.values()))
        

part_two()