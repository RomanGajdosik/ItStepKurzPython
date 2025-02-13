numbers='-100 -100 -98 -50 1'
for symbol in numbers :
    cislo=list()
    zozCisiel=list()
    indx=0
    if symbol in '-1234567890':
        cislo.append(symbol)
        print(cislo)
    elif symbol == ' ':
        zozCisiel.insert(indx,cislo)
        print(zozCisiel)
        indx +=1
        cislo.clear
        #cislo.insert(0,100)
# cislo.insert(1,200)
# print(cislo)
#print(zozCisiel)
