class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        #self.data = Node(data)
        self.head = None

    def getLength(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def insertAtFirst(self,data):
        new_node = Node(data)
        if self.getLength() == 0:
            self.head = new_node
        else:
            itr=self.head
            new_node.next = itr
            self.head = new_node

    def insertAtLast(self,data):
        new_node = Node(data)
        lenOfLinkedList = self.getLength()
        if lenOfLinkedList == 0:
            self.insertAtFirst(data)
        else:
            itr=self.head
            count=0
            while itr:
                if count == lenOfLinkedList-1:
                    itr.next = new_node
                count+=1
                itr=itr.next

    def insertAt(self,index,data):
        if index == 0:
            self.insertAtFirst(data)
            return
        else:
            lenOfLinkedList = self.getLength()
            if lenOfLinkedList == index:
                self.insertAtLast(data)
            else:
                new_node = Node(data)
                itr=self.head
                count=0
                while itr:
                    if count == index-1:
                        new_node.next = itr.next
                        itr.next = new_node
                        break
                    count+=1
                    itr=itr.next

    #Converting list object to linked list
    def toLinkedList(self,list):
        for item in list:
            self.insertAtLast(item)

    #Inserting element after a particular data value
    #Search for first occurence of data_after value and insert
    #Now insert data_value node after data_after node
    #If data not found, then inserting at end
    def insert_after_value(self,data_after,data_value):
        indexToInsert=0
        count=0
        dataNodeFound=False
        itr = self.head
        while itr:
            if itr.data == data_after:
                dataNodeFound=True
                indexToInsert=count+1
                break
            itr=itr.next
            count+=1
        if(dataNodeFound):
            self.insertAt(indexToInsert,data_value)
        else:
            self.insertAtLast(data_value)

    def removeAt(self,index):
        lenOfLinkedList = self.getLength()
        if index < 0 or index >= lenOfLinkedList:
            raise IndexError("invalid index")
        elif index == 0:
            itr=self.head
            itr=itr.next
            self.head=itr
        else:
            itr = self.head
            count=0
            while itr:
                if count == index-1:
                    itr.next=itr.next.next
                    break
                itr = itr.next
                count+=1

    #delete first occurrence of a node if data_value matches
    def remove_by_value(self,data_value):
        indexToRemove=0
        count=0
        itr = self.head
        while itr:
            if itr.data == data_value:
                indexToRemove=count
                self.removeAt(indexToRemove)
                break
            itr=itr.next
            count+=1

    #To print the elements in linked list
    def print(self):
        """print()
        itr = self.head
        while itr:
            #print("itr: ",id(itr))
            print(itr.data,' -> ',end=' ')
            itr = itr.next"""
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

linked_list = LinkedList()
linked_list.insertAtFirst(6)
linked_list.insertAtFirst(7)
linked_list.insertAtLast(8)
linked_list.insertAtLast(90)
linked_list.insertAt(2,40)
print(linked_list.getLength())
linked_list.print()

Fruits=["Apple","Orange","Kiwi","Papaya"]
fruitsLinkedList=LinkedList()
fruitsLinkedList.toLinkedList(Fruits)
fruitsLinkedList.print()

fruitsLinkedList.insert_after_value("Orange","Grapes")
fruitsLinkedList.print()

fruitsLinkedList.insert_after_value("Watermelon","Plums")
fruitsLinkedList.print()

fruitsLinkedList.removeAt(1)
fruitsLinkedList.print()

fruitsLinkedList.remove_by_value("Papaya")
fruitsLinkedList.print()

