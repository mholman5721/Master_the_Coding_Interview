# CITATION: https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/learn/lecture/12301306#questions

class MyArray:
    def __init__(self) -> None:
        self.length = 0
        self.data = {}
    def get(self, index):
        return self.data[index]
    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length
    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem
    def delete(self, index):
        item = self.data[index]
        self._shiftItems(index)
        return item
    def _shiftItems(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1
        

newArray = MyArray()

newArray.push("Hello")
newArray.push("World")
newArray.push("!")

print(newArray.data)

newArray.delete(1)

print(newArray.data)