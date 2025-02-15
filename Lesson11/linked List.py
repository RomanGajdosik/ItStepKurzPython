class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head =None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def printList(self):
        curent_Node = self.head
        while curent_Node:
            print(curent_Node.data , end='->')
            curent_Node = curent_Node.next
        print('None')

    def find_in_list(self,data_to_find):
        this_node = self.head
        najdene = False
        while this_node:
            if this_node.data == data_to_find:
                print('\nNajdene')
                return this_node
            this_node = this_node.next
        #print(f'Nachadza sa vami hladana hodnota {data_to_find} :{najdene}')
        print('Nenajdene')
    
    def delete(self,data_to_delete):
        temp = self.head

        if temp.data == data_to_delete:
            self.head = temp.next
            temp = None
            return
               
        prev =None
        while temp and temp.data != data_to_delete:
            prev = temp
            temp = temp.next
        
        if temp is None:
            print(f'Zadana hodnota {data_to_delete} sav v liste nenachadza')
            return 
        
        prev.next = temp.next
        temp =None
 
    def replace(self,data_to_replace,new_data):
        current_node = self.head
        while current_node:
            if current_node.data ==data_to_replace:
                current_node.data = new_data
                break
            current_node = current_node.next

class App():
    
    
    
    @staticmethod
    def run():
        lnkd_List = LinkedList()
        while True :
            print ('\nZvol si z menu :')
            print(20*'-')
            print('1.Pridaj do listu')
            print('2.Vymaz z listu')
            print('3.Vypis list')
            print('4.Zkontroluj ci list obsahuje hodnotu')
            print('5.Vymen hodnotu v liste')
            print('6. Exit')
            
            volba = int(input('Zadaj cislo pre vykonanie operacie: '))
            
            if volba == 1:
                hodnota = int(input('Zadaj hodnotu ktoru ches pridat do listu: '))
                lnkd_List.append(hodnota)
            
            elif volba == 2:
                hodnota = int(input('Zadaj hodnotu ktoru ches zmazat: '))
                lnkd_List.delete(hodnota)
            elif volba == 3:
                print('\n')
                print('Data v liste su nasledujuce : ')
                lnkd_List.printList()
            elif volba == 4:
                hodnota = int(input('Zadaj hodnotu ktoru ches najst: '))
                lnkd_List.find_in_list(hodnota)
            elif volba == 5:
                hodnota = int(input('Zadaj hodnotu ktoru ches zmenit: '))
                hodnota_New = int(input('Zadaj novu  hodnotu ktora ju nahradi: '))
                lnkd_List.replace(hodnota,hodnota_New)
            elif volba == 6:
                print('Dakujem za pouzitie mojho Linked Listu :)')
                return


App()   
App.run()

# lnkdList = LinkedList()
# lnkdList.append(1)
# lnkdList.append(2)
# lnkdList.append(3)
# lnkdList.append(4)
# lnkdList.append(5)
# lnkdList.replace(5,8)
# lnkdList.printList()
#lnkdList.replace(1,8)
#lnkdList.printList()
#data = lnkdList.find_in_list(1)
# lnkdList.delete(0)
# lnkdList.printList()












