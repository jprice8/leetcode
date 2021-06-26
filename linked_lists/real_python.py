

# Class to represent the Linked List
class LinkedList:
    def __init__(self):
        self.head = None 

    # method adds element to the left of the linked list
    def addToStart(self, data):
        # create a temp node
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode

    # method displays linked list
    def display(self):
        start = self.head 
        if start is None:
            print("empty list")
            return False

        while start:
            print(str(start.getData()), end=" ")
            start = start.link
            if start:
                print("-->", end=" ")
        print()

    # method returns and removes element at received position
    def removePosition(self, position):
        data = self.atIndex(position)
        self.remove(data)
        return data

    


# Class to represent each node of the Linked List
class Node:
    # default value of data and link is none if no data is passed
    def __init__(self, data=None, link=None):
        self.data = data 
        self.link = link

    # method to set link field of Node
    def setLink(self, node):
        self.link = node

    # method returns data field of the Node
    def getData(self):
        return self.data
    

# Main method

# create linkedlist
myList = LinkedList()

# add some elements to the start of linkedlist
myList.addToStart(5)
myList.addToStart(4)
myList.addToStart(3)
myList.addToStart(2)
myList.addToStart(1)

myList.display()