total = 0 #variabele om starks verder mee te rekeken

for dag in range(5): # itereert 5 keer
    bugs = int(input('hoeveel insecten heeft u vandaag gevangen?')) # deze statement wordt 5 keer geïtereerd
    total = bugs + total # de bugs worden per input bij elkaar opgeteld
print('u heeft deze week',total,'insecten gevangen') # print het aantal bugs
