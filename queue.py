class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    def peek(self):
        return self.first
    def enqueue(self, value):
        newNode = Node(value)
        if self.first == None and self.last == None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = self.last.next
        self.length += 1
        return self
    def dequeue(self):
        item = self.first
        if self.length > 0:
            if self.first == self.last:
                self.last = None
            self.first = self.first.next
            self.length -= 1
        return item
    def print(self):
        ptr = self.first
        print("Length:", str(self.length))
        while ptr != None:
            print(str(ptr.value))
            ptr = ptr.next
        print()

myQueue = Queue()

myQueue.enqueue(1)
# myQueue.enqueue(2)
# myQueue.enqueue(3)
# myQueue.enqueue(4)
# myQueue.enqueue(5)

myQueue.print()

val = myQueue.dequeue()
print(val.value)
print()

val = myQueue.dequeue()
print(val)
print()

val = myQueue.dequeue()
print(val)
print()

myQueue.print()
