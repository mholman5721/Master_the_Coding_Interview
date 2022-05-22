class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, value) -> None:
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = self.tail.next
        self.length += 1
        return self
    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = self.head.prev
        self.length += 1
        return self
    def insert(self, location, value):
        # a b c d
        # insert X at location 2
        # a b X c d
        newNode = Node(value)
        ptr = self.head
        if location >= self.length:
            self.append(value)
        elif location <= 0:
            self.prepend(value)
        else:
            ptr = self._findLocation(location, ptr)
            newNode.next = ptr.next
            newNode.prev = ptr
            ptr.next.prev = newNode
            ptr.next = newNode
            self.length += 1
        return self
    def remove(self, location):
        # a b X c d
        # remove X at location 2
        # a b c d
        ptr = self.head
        if location >= self.length:
            return -1
        elif location <= 0:
            return -2
        else:
            ptr = self._findLocation(location, ptr)
            delNode = ptr.next
            ptr.next = delNode.next
            delNode.next.prev = ptr
            del delNode
            self.length -= 1
        return self 
    def _findLocation(self, location, ptr):
        for i in range(0, location - 1):
            ptr = ptr.next
        return ptr
    def printContentsForward(self):
        output = ""
        ptr = self.head
        print("Length: " + str(self.length) + " ")
        while ptr != None:
            output += str(ptr.value) + " "
            ptr = ptr.next
        print(output)
    def printContentsReverse(self):
        output = ""
        ptr = self.tail
        print("Length: " + str(self.length) + " ")
        while ptr != None:
            output += str(ptr.value) + " "
            ptr = ptr.prev
        print(output)


myLinkedList = LinkedList(1)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(5)

myLinkedList.printContentsForward()

myLinkedList.insert(2, 99)

myLinkedList.printContentsForward()

print(myLinkedList.remove(2))

myLinkedList.printContentsForward()
myLinkedList.printContentsReverse()