def main():
    test1, test2, test3, test4, test5 = inputt() #roept functie aan en returned variabele en verwerkt de return
    gemiddel = gemiddelde(test1, test2, test3, test4, test5) #roept functie aan en returned variabele en verwerkt de return
    score(gemiddel) #roept functie aan en verwerkt de return


def score(gemiddel):  #variabelen worden verwerkt in functie 
    if gemiddel >= 90 and gemiddel <= 100: #vergelijkt gemiddelde met een if statement
        resultaat = 'A' #als if statement true is dan wordt deze variabelen deze waarde gegeven 
        print('Met een gemiddelde van',gemiddel,'heb je een',resultaat,'behaald') #print de variabele en score
    if gemiddel >= 80 and gemiddel <= 89: #vergelijkt gemiddelde met een if statement
        resultaat = 'B' #als if statement true is dan wordt deze variabelen deze waarde gegeven
        print('Met een gemiddelde van',gemiddel,'heb je een',resultaat,'behaald') #print de variabele en score
    if gemiddel >= 70 and gemiddel <= 79:  #vergelijkt gemiddelde met een if statement
        resultaat = 'C' #als if statement true is dan wordt deze variabelen deze waarde gegeven 
        print('Met een gemiddelde van',gemiddel,'heb je een',resultaat,'behaald') #print de variabele en score
    if gemiddel >= 60 and gemiddel <= 69:  #vergelijkt gemiddelde met een if statement
        resultaat = 'D' #als if statement true is dan wordt deze variabelen deze waarde gegeven 
        print('Met een gemiddelde van',gemiddel,'heb je een',resultaat,'behaald') #print de variabele en score
    if gemiddel <= 59: #als de gemiddelde lager is dan 59 wordt is het altijd true
        resultaat = 'F' #als if statement true is dan wordt deze variabelen deze waarde gegeven 
        print('Met een gemiddelde van',gemiddel,'heb je een',resultaat,'behaald') #print de variabele en score      


def gemiddelde(test1, test2, test3, test4, test5): #variabelen worden verwerkt in functie 
    gemiddel = (test1 + test2 + test3 + test4 + test5) / 5 #berekent gemiddlede van de scores
    return gemiddel #retured de variabele


def inputt():
    test1 = float(input('Wat was je score?: ')) # vraagt voor input score
    test2 = float(input('Wat was je score?: ')) # vraagt voor input score
    test3 = float(input('Wat was je score?: ')) # vraagt voor input score
    test4 = float(input('Wat was je score?: ')) # vraagt voor input score
    test5 = float(input('Wat was je score?: ')) # vraagt voor input score
    return test1, test2, test3, test4, test5 # returned de variabelen




main()
#auteur: Gijsbert Keja
