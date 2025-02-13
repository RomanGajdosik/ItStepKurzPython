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

#verzia 2

lnkdList = LinkedList()
lnkdList.append(1)
lnkdList.append(2)
lnkdList.append(3)

lnkdList.printList()

