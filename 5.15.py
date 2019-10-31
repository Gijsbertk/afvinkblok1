def main():
    test1, test2, test3, test4, test5 = inputt()
    gemiddel = gemiddelde(test1, test2, test3, test4, test5)
    score(gemiddel)


def score(gemiddel):
    if gemiddel >= 90 and gemiddel <= 100:
        resultaat = 'A'
        print('Met een gemiddelde van',gemiddel,'heb je een',resultaat,'behaald')
    if gemiddel >= 80 and gemiddel <= 89:
        resultaat = 'B'
        print('Met een gemiddelde van',gemiddel,'heb je een',resultaat,'behaald')
    if gemiddel >= 70 and gemiddel <= 79:
        resultaat = 'C'
        print('Met een gemiddelde van',gemiddel,'heb je een',resultaat,'behaald')
    if gemiddel >= 60 and gemiddel <= 69:
        resultaat = 'D'
        print('Met een gemiddelde van',gemiddel,'heb je een',resultaat,'behaald')
    if gemiddel <= 59:
        resultaat = 'F'
        print('Met een gemiddelde van',gemiddel,'heb je een',resultaat,'behaald')       


def gemiddelde(test1, test2, test3, test4, test5):
    gemiddel = (test1 + test2 + test3 + test4 + test5) / 5
    return gemiddel


def inputt():
    test1 = float(input('Wat was je score?: '))
    test2 = float(input('Wat was je score?: '))
    test3 = float(input('Wat was je score?: '))
    test4 = float(input('Wat was je score?: '))
    test5 = float(input('Wat was je score?: '))
    return test1, test2, test3, test4, test5 




main()
