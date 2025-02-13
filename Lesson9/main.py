nazovSuboru=input('Zadaj nazov suboru :' )
obsah=input('Zadaj obsah na zapisanie :')

with open(nazovSuboru,'w') as filehandler:
    filehandler.write(obsah)
    print('zmena')
    print('zmena2')
    print('Dalsia nova zmena na novom branchi')