
prog = ""
maxx = 0
bestand = intput(open('Bestandsnaam'))
for n in bestand:
    prog += bestand.readline()
    maxx += 1
    if maxx == 5:
        break
print (prog)
