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


def reverse_1(str):
    retVal = ""
    str_array = MyArray()
    for i in range(0, len(str)):
        str_array.push(str[i])
    for i in range(0, len(str)):
        char = str_array.pop()
        retVal += char
    return retVal

def reverse_2(str):
    length = len(str)
    for i in range(0, length//2):
        # swap str[i] <=> str[((length - 1) - i)]
        a = str[i]
        b = str[((length - 1) - i)]
        str = str[:i] + b + str[i+1:]
        str = str[:((length - 1) - i)] + a + str[((length - 1) - i)+1:]
    return str

str1 = "Hello My Name Is Matthew"
rstr1 = reverse_1(str1)
print(rstr1)

str2 = "Hello My Name Is Matthew"
rstr2 = reverse_2(str2)
print(rstr2)