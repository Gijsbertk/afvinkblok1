def main():
    kilometer = vraag() #roept funcite aan
    miles = kilometer * 0.6214 #berekent aantal mijlen
    print('Je hebt',miles,'mijlen afgelegd') #print het aantal mijlen
    
        

def vraag():
    kilometer = int(input('Hoeveel kilometer heb je gereden?: ')) #vraagt voor de aantal kilometers
    return kilometer # returned variabele




main()
