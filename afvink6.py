#afvink6 git opdracht
seq = "ACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCC"

#opent het document.
from tkinter import filedialog
from tkinter import *


def openbestand():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))



    #leest het document in en slaat de eerste regel over omdat dat de benaming is.    
    bestand = open(root.filename).readlines()[1:]
    #zet het bestand weer leesbaar als een string en haalt daarna all enters(\n) eruit en verplaatst het met ("").
    seq = "".join(bestand).replace("\n","")
    return seq
        




def match2():
    o = ""
    index = 0

    B = []
    bestand = open ("enzymen.txt")
    for regel in bestand:
        enzym, seq = regel.split()
        seqenzym = seq.replace("^","")
        B.append(seqenzym)


        for eiwit in B:
            while index < len(seq):
                index = seq.find(seqenzym, index)
            if index == -1:
                break
            o = o+" " * (index - len(o)) + str(seqenzym)
            index += len(seqenzym)
        
            #print (seq)
            #print (o)





def enzymen():
    knipenzymen = {}
    bestand = open ("enzymen.txt")
    for regel in bestand:
        enzym_name, seq = regel.split()
        seqenzym = seq.replace("^","")
        knipenzymen[enzym_name] = seqenzym
    return knipenzymen
    

def zoek(seq, eiwit, enzym):
    o = ""
    index = 0
    plaats = []
    while index < len(seq):
        index = seq.find(eiwit, index)
        if index == -1:
              break
        o = o+" " * (index - len(o)) + str(eiwit)
        ff = index
        plaats.append(index)
        index += len(eiwit)
        
    return o,plaats



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
            
            #result[enzym].append(o)
    #print(result)
match()
