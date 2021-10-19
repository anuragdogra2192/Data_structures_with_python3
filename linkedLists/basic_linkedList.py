class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return None #return == return None
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode
    
    def InBetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def RemoveNode(self, Removekey):
        HeadVal = self.headval

        if(HeadVal is not None):
            if(HeadVal.dataval == Removekey):
                self.headval = HeadVal.nextval
                HeadVal = None
                return
        while(HeadVal is not None):
            if (HeadVal.data == Removekey):
                break
            prev = HeadVal
            HeadVal = HeadVal.next
            


    
list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

#Link first node to second node
list1.headval.nextval = e2

#Link second node to third node
e2.nextval = e3

#Traversing a Linked List
list1.listprint()

#Inserting at the End of the Linked List
list1.AtEnd("Thu")
list1.listprint()

#Inserting in between 2 data nodes
list1.InBetween(list1.headval.nextval, "Fri")
list1.listprint()

#Removing an item from the linked list

