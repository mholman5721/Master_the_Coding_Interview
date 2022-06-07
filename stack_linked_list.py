class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0
    def peek(self):
        value = self.top
        return value
    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = self.top
        else:
            newNode.next = self.top
            self.top = newNode
        self.length += 1
        return self
    def pop(self):
        value = self.top
        if self.length > 0:
            if self.top == self.bottom:
                self.bottom = None
            self.top = self.top.next
            value.next = None
            self.length -= 1
        return value
    def print(self):
        ptr = self.top
        print("Length:", str(self.length))
        while ptr != None:
            print(str(ptr.value))
            ptr = ptr.next
        print()

myStack = Stack()
myStack.push("1")
myStack.push("2")
myStack.push("3")

myStack.print()

print(myStack.peek().value)
myStack.pop()
print(myStack.peek().value)
myStack.pop()
print(myStack.peek().value)
myStack.pop()
print()

myStack.print()

print(myStack.bottom)
