class Node:
    def __init__(self,data):
        self.data = data #initialize data
        self.next = None #initialize next as null

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("The given node must be in the LinkedList")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
 
        new_node = Node(new_data)
        
        #if the list is empty
        if self.head is None:
                self.head = new_node
                return
        
        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
        
        # 6. Change the next of last node
        last.next =  new_node

    def deleteNode(self, key):

        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head=temp.next
                temp = None
                return
        
        while temp is not None:

            if temp.data == key: #if we find the node then we break from the loop and do the unlinking outside
                break
            prev = temp
            temp = temp.next
        
        prev.next = temp.next
        temp = None


if __name__=='__main__':
    #start with empty list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.push(5)
    llist.printList()
    print("**********************")
    llist.insertAfter(llist.head.next.next,7)
    llist.printList()
    llist.append(9)
    llist.printList()

