lijst = []

def main():
    b_open()
    gemiddelde()
    hoog()

def b_open():
    bestand = open("SC_expression.csv")
    bestand.readline()
    
    for regel in range(6071):
        regel = bestand.readline()
        regel = regel.strip()
        regel = regel.split(",")
        list_.append(regel)



def hoog():
    kolom = int(input ("Welke kolom wil je hebben?"))
    for getal in range(len(list_)):
        waarde = float (list_[getal][kolom])
        if waarde > 50 or waarde == 50:
            print (list_[getal][0])
        



def gemiddelde():
    kolom = int(input ("Welke kolom wil je hebben?"))
    gem = 0
    for getal in range(len(list_)):
        gem += float (list_[getal][kolom])
          
    gem = gem / len(list_)
    print (gem)

main()
