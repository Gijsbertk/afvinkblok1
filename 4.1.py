total = 0

for dag in range(5):
    bugs = int(input('hoeveel insecten heeft u vandaag gevangen?'))
    total = bugs + total
print('u heeft deze week',total,'insecten gevangen')
