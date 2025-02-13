# filehandler = open('text.txt','r')
# print(filehandler.read())
# print(filehandler.read(-1))
# print(repr(filehandler.read()))
# lines = filehandler.readlines()
#line2 = filehandler.readlines()
# for line in lines:
#     if line[-1 =='\n']:    # podmienka ak je posledny znak \n tak citame line bez toho znaku
#         line=line[0:-1]    # odstranime posledny znak .
#     print(line)
#     print(len(line)*'*')
from logging import exception

# for line in filehandler:  # take iste ako .readlines
#     print(line)
#file2handler =open('text2.txt','w') # write mod ktory pise na zaciatku suboru , ak subor neexistuje tak ho vytvori
# file2handler =open('text2.txt','a') # append mod ktory zapisuje na koniec suboru , ak subor neexistuje tak ho vytvori
# file2handler.write('Ako sa mas .\n')
# file2handler.close()
# file2handler=open('text2.txt','r')
# print(file2handler.read())
# print('Zapis cez print funkciu' , file = file2handler)
# print(file2handler.read())
# with open('text.txt','r') as filehandler:  # najbezpecnejsie riesenie lebo automaticky zatvara otvoreny subor
#     text = (filehandler.readline())
#
# def zobraz(txt):
#     print(txt)
#
# zobraz(text)
#nazovSuboru =input('Zadaj nazov suboru : ')

def vymen_slova (text,nove_slovo):
     nahradene_slova = [nove_slovo for slovo in text]
     nahradeny_text = ' '.join(nahradene_slova)
     return print(nahradeny_text)

try:
    with open('text2.txt','r') as filehandler:  # najbezpecnejsie riesenie lebo automaticky zatvara otvoreny subor
        text = (filehandler.readlines())

    dlzka = 0
    pocet_riadkov = 0
    for line in text:
        if len(line) > dlzka:
            dlzka=len(line)
        pocet_riadkov += 1

    #print('maxdlzka je :',dlzka)
    #print('Pocet riadkov je :',pocet_riadkov)
    # print(text.split())
    vymen='slovo'
    vymen_slova(text,vymen)
except:()