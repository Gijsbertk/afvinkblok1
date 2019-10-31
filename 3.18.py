vega = input('Is er iemand vegatarisch? ') #vraag of er iemand vegatarisch is
vegan = input('Is er iemand veganistisch? ') #vraag of er iemand vegan is
glut = input('Heeft er iemand een gluten-allergie? ') #vraag of er is met gluten
if vega == 'nee': #vraag of er iemand vegan vega of gluten heeft en dan de uitkomende restaurants
    if vegan == 'nee':
        if glut == 'nee':
            print('je kan naar alle mogelijke restaurants')
if vega == 'ja':#vraag of er iemand vegan vega of gluten heeft en dan de uitkomende restaurants
    if vegan == 'nee':
        if glut == 'nee':
            print('je kan naar main, corner, chef en mama')
if vega == 'ja':#vraag of er iemand vegan vega of gluten heeft en dan de uitkomende restaurants
    if vegan == 'ja':
        if glut == 'nee':
            print('je kan naar corner en chef')
if vega == 'ja':#vraag of er iemand vegan vega of gluten heeft en dan de uitkomende restaurants
    if vegan == 'ja':
        if glut == 'ja':
            print('je kan naar corner en chef')
if vega == 'nee':#vraag of er iemand vegan vega of gluten heeft en dan de uitkomende restaurants
    if vegan == 'ja':
        if glut == 'nee':
            print('je kan naar main, corner en chef')
if vega == 'nee':#vraag of er iemand vegan vega of gluten heeft en dan de uitkomende restaurants
    if vegan == 'nee':
        if glut == 'ja':
            print('je kan naar main, corner en chef')
if vega == 'nee':#vraag of er iemand vegan vega of gluten heeft en dan de uitkomende restaurants
    if vegan == 'ja':
        if glut == 'ja':
            print('je kan naar chef en main')
if vega == 'ja':#vraag of er iemand vegan vega of gluten heeft en dan de uitkomende restaurants
    if vegan == 'nee':
        if glut == 'ja':
            print('je kan naar main corner en chef')
        
