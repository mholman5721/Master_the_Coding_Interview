class Stack:
    def __init__(self) -> None:
        self.data = []
        self.length = 0
    def peek(self):
        value = None
        if self.length > 0:
            value = self.data[self.length - 1]
        return value
    def push(self, value):
        self.data.append(value)
        self.length += 1
        return self
    def pop(self):
        value = self.data.pop()
        self.length -= 1
        return value
    def print(self):
        print("Length:", str(self.length))
        for i in range(self.length-1, -1, -1):
            print(self.data[i])
        print()

myStack = Stack()
myStack.push("1")
myStack.push("2")
myStack.push("3")

myStack.print()

print(myStack.peek())
myStack.pop()
print(myStack.peek())
myStack.pop()
print(myStack.peek())
myStack.pop()
print()

myStack.print()