#afvink6 git opdracht
seq = "ACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCC" #var met waarde

#opent het document.
from tkinter import filedialog
from tkinter import *

def main():
    seq = openbestand()
    enzymen(seq)
    match()
    match2()
    zoek()
    
    
    

def openbestand():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))



    #leest het document in en slaat de eerste regel over omdat dat de benaming is.    
    bestand = open(root.filename).readlines()[1:]
    #zet het bestand weer leesbaar als een string en haalt daarna all enters(\n) eruit en verplaatst het met ("").
    seq = "".join(bestand).replace("\n","")
    return seq
        




def match2(): #functie
    o = "" #lege var
    index = 0 #var met waarde 0

    B = [] # var met lege lijst 
    bestand = open ("enzymen.txt") #opent bestabd
    for regel in bestand: #itereert dmv bestand 
        enzym, seq = regel.split() #split bestand 
        seqenzym = seq.replace("^","") # #vervangt dakje
        B.append(seqenzym) #schrijft de var na aleke ietratie toe 


        for eiwit in B: #itereert dmv var
            while index < len(seq): # iteert de seq 
                index = seq.find(seqenzym, index) # zoek in de var 
            if index == -1: #kijkt of statement true is  
                break # voert uit wanneer stement true is 
            o = o+" " * (index - len(o)) + str(seqenzym) # geeft var een neiwue waarde bij elke iteratie 
            index += len(seqenzym) #voegt waarde toe na elke iteratie
        
       print (seq) #print var
       print (o) #print var 
       return eiwit, seq         



def enzymen(seq): #functie 
    knipenzymen = [] #lege lijst 
    bestand = open ("enzymen.txt") # openend bestand
    for regel in bestand: #itereert dmv var 
        enzym_name, seq = regel.split() #split bij iteratie 
        seqenzym = seq.replace("^","") #vervangt bij iteratie 
        knipenzymen[enzym_name] = seqenzym #geeft per iteratie nieuwe waarde 
    return knipenzymen # returned var 
    

def zoek(seq, eiwit, enzym): # verwerkt return en functie
    o = "" #leeg var
    index = 0 #var met warde 0 
    plaats = [] #var met list
    while index < len(seq): #itereert 
        index = seq.find(eiwit, index) #zoekt 
        if index == -1: #kijkt of statement true is  
              break #voert uit als statement true is 
         o = o+" " * (index - len(o)) + str(eiwit) #voert per iteratie uit 
         ff = index #geeft var waarde 
         plaats.append(index) #schrijft var in list
         index += len(eiwit) #voeft per iteratie toe 
        
    return o,plaats #returned value 



def match():
    knipenzymen = enzymen()
    result = {}
    #seq = openbestand()
    #print(seq)
    for enzym in knipenzymen:
        #result[enzym]=[]
        if seq.find(knipenzymen[enzym]) != -1:
            o,plaats = zoek(seq, knipenzymen[enzym], enzym)
            print ("er is een match gevonden met " + str (enzym) + " op positie(s)" + str (plaats))
            print (seq)
            print(o)
            
            result[enzym].append(o) #schrijft var aan lijst 
    print(result) # print var 
#gijsbert keja
