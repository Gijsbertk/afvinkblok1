import random


def main():
    aantal = roll()
    verwerk(aantal)


def verwerk(aantal):
    
    lijst = []
    for x in range(aantal):
        nummer = random.randint(1, 6)
        lijst.append(nummer)
    print(lijst)

        






def roll():
    aantal = int(input('Hoe vaak heb je gegooid?(je kan alleen een positieve invullen): '))
    return aantal




main()
