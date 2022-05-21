class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
    def append(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.length += 1
        return self
    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
    def insert(self, location, value):
        # a b c d
        # insert X at location 2
        # a b X c d
        newNode = Node(value)
        ptr = self.head
        if location > self.length:
            self.append(value)
        elif location <= 0:
            self.prepend(value)
        else:
            for i in range(0, location-1):
                ptr = ptr.next
            newNode.next = ptr.next
            ptr.next = newNode
            self.length += 1
        return self
    def printContents(self):
        output = ""
        ptr = self.head
        print("Length: " + str(self.length) + " ")
        while ptr != None:
            output += str(ptr.value) + " "
            ptr = ptr.next
        print(output)


myLinkedList = LinkedList(1)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(5)

myLinkedList.printContents()

myLinkedList.insert(4, 99)

myLinkedList.printContents()