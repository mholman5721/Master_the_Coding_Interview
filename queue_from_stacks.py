# https://leetcode.com/problems/implement-queue-using-stacks/description/

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

class MyQueue(object):

    def __init__(self):
        self.stackA = Stack()
        self.stackB = Stack()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stackA.push(x)
        

    def pop(self):
        """
        :rtype: int
        """
        # 'Slinky' everything into stackB
        for i in range(0, self.stackA.length):
            val = self.stackA.pop()
            self.stackB.push(val.value)
        # 'Pop' the last value from stackB to return
        retVal = self.stackB.pop()
        # 'Slinky' everything back into stackA
        for i in range(0, self.stackB.length):
            val = self.stackB.pop()
            self.stackA.push(val.value)

        return retVal
        

    def peek(self):
        """
        :rtype: int
        """
        # 'Slinky' everything into stackB
        for i in range(0, self.stackA.length):
            val = self.stackA.pop()
            self.stackB.push(val.value)
        # 'Pop' the last value from stackB to return
        retVal = self.stackB.peek()
        # 'Slinky' everything back into stackA
        for i in range(0, self.stackB.length):
            val = self.stackB.pop()
            self.stackA.push(val.value)

        return retVal
        

    def empty(self):
        """
        :rtype: bool
        """
        retVal = True
        if self.stackA.length > 0:
            retVal = False
        return retVal
    

    def print(self):
        self.stackA.print()

obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)

obj.print()

print(obj.peek())
print(obj.pop())
print()

obj.print()