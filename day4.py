
def main() -> int:

    file = open("input.txt")
    lines = file.readlines()
    file.close()

    games = []
    cards = {}

    for line in lines:

        id,numbers = line.split(":")
        winners,own = numbers.split("|")
        winners,own,id = winners.strip().split(), own.strip().split(), int(id.split()[1])
        matches = 0

        if not id in cards.keys():
            cards[id] = 1
        else:
            cards[id] += 1

        for n in own:
            if n in winners: matches+=1
        
        games.append(2**matches//2)

        for card in range(id+1, id+matches+1):

            if not card in cards.keys():
                cards[card] = cards[id]

            else:
                cards[card] += cards[id]
    
    return sum(games),sum(cards.values())

if __name__ == "__main__":
    print(main())
