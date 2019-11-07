# Naam: Gijsbert Keja
# Datum: 31-10-19
# Versie:

# Voel je vrij om de variabelen/functies andere namen te geven als je 
# die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein 
# proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de 
# tijd.

  
    
def lees_inhoud(bestands_naam):
    """Schrijf hier je eigen code die het fasta bestand inleest en deze 
    splitst in headers en sequenties.
    Lever twee strings:
        - header = string, header van fasta
        - seq = string met daarin de sequentie behorend bij de header
    Hieronder vind je de return nodig om deze twee lijsten op te leveren
    """
   
    bestand = open(bestands_naam).readlines()[0:] #opent bestand en leest het helemaal
    bestand = "".join(bestand) #maakt alles itereerbaar
    
    
    split = bestand.split("\n", 1) # split het bestand op gegeven waarde

    header = split[0] #var krijgt waarde
    seq = split[1] #var krijgt waarde
    seq = "".join(seq).replace("\n","")  #maakt alles itereerbaar en vervangt dat op \n
    print (seq) #print var 
    print ("") #print witregel
    print (header) #print var
        
    return header, seq #returned var

    
def is_dna(seq): 
    """Deze functie bepaalt of de sequentie (een element uit seqs)
    DNA is.
    Indien ja, return True
    Zo niet, return False
    """
    #bekijken of het een dna sequentie is
    tel = seq.count ("A") + seq.count ("T") + seq.count ("C") + seq.count ("G") # telt alle waarde bij elkaar op 
    if tel == len(seq): #kijkt of staetment true is 
        print (True) #print var
    else:
        print (False)  #print var

def knipt(seq):
    """Bij deze functie kan je een deel van de code die je de afgelopen 
    2 afvinkopdrachten geschreven hebt herbruiken
    Deze functie bepaald of een restrictie enzym in de sequentie 
    (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je 
    alleen maar printjes maken.
    """
    
    #bekijken of het een knipenzym heeft
    Ddell = "CTGAG" #var krijgt waarde
    if seq.find(Ddell) != -1: #kijkt of statement true is
        print ("Ddell knipt er in") #print de haakejs
    else: #als satement niet true is 
        print ("Ddell knipt er niet in") #print de haakejs


def main():
    # Voer hier de bestandsnaam van het juiste bestand in, of hernoem 
    # je bestand
     
    # Hier onder vind je de aanroep van de lees_inhoud functie, 
    # die gebruikt maakt van de bestand variabele als argument. 
    # De resultaten van de functie, de lijst met headers en de lijst 
    # met sequenties, sla je op deze manier op in twee losse resultaten.


    # schrijf hier de rest van de code nodig om de aanroepen te doen
    header, seq = lees_inhoud("lamaseq.fasta") #returned var en ropet def aan
    is_dna(seq) #verwerkt var en roept def aan
    knipt(seq) # vewerkt var en roept def aan
    
main()
