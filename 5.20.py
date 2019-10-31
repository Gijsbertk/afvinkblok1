import random


def main():
    quiz()


def quiz():
    nummer = random.randint(1, 20)
    print(nummer)
    ask = int(input('Wel getal denkt u dat het is?: '))
    while nummer > ask:
        print('Getal is te hoog probeer opnieuw')
        ask = int(input('Wel getal denkt u dat het is?: '))
    while nummer < ask:
        print('Getal is te laag probeer opnieuw')
        ask = int(input('Wel getal denkt u dat het is?: '))
    while nummer == ask:
        print('U heeft het juiste getal geraden, het getal was dus',nummer)
        print('U begint weer opnieuw')
        nummer = random.randint(1, 20)
        ask = int(input('Wel getal denkt u dat het is?: '))
              
    




main()
