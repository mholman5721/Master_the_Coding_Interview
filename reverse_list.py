class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data) -> None:
        self.head = Node(data)
        self.tail = self.head
        self.length = 1
    def append(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = self.tail.next
        self.length += 1
        return self
    def reverse(self):
        ref1 = self.head
        ref2 = self.head
        if self.length == 1:
            return self
        elif self.length == 2:
            ref2 = ref2.next
            ref2.next = ref1
            ref1.next = None
            self.head = ref2
            self.tail = ref1
            return self
        else:
            #   e
            #   t     h
            # N-*-*-*-* N
            #       1 2 3
            #         
            # change h.next = None
            # while 3 != None
            #   change 2.next = 1
            #   set 1 = 2
            #   set 2 = 3
            #   set 3 = 3.next
            # change 2.next = 1
            # swap h and t:
            #   set e = h
            #   set h = t
            #   set t = e
            p1 = self.head
            p2 = p1.next
            p3 = p2.next

            # change h.next = None
            self.head.next = None
            # while 3 != None
            while p3 != None:
                p2.next = p1
                p1 = p2
                p2 = p3
                p3 = p3.next
            # change 2.next = 1
            p2.next = p1
            # swap h and t:
            temp = self.head
            self.head = self.tail
            self.tail = temp
        pass
    def print(self):
        ptr = self.head
        printString = ""
        while ptr != None:
            printString += str(ptr.data) + " "
            ptr = ptr.next
        print("Length:" + str(self.length))
        print(printString)
        return printString

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.print()
ll.reverse()
ll.print()