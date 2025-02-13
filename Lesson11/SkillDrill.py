class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_List:
    def __init__(self):
        self.head = None

    def pridaj(self,data):
        novy_bod = node(data)
        if self.head == None:
            self.head = novy_bod
            return
        dalsi_bod = self.head
        while dalsi_bod.next:
            dalsi_bod = dalsi_bod.next
        dalsi_bod.next =   novy_bod
    def vypis_list(self):
        aktualny_blok = self.head
        while aktualny_blok:
            print (aktualny_blok.data,end='->')
            aktualny_blok = aktualny_blok.next
        print('None')

testList = linked_List()
testList.pridaj(1)
testList.pridaj(2)
testList.pridaj(4)
testList.vypis_list()