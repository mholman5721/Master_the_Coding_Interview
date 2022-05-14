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

def reverse_3(str):
    str = list(str)
    length = len(str)
    for i in range(0, length//2):
        temp = str[i]
        str[i] = str[((length - 1) - i)]
        str[((length - 1) - i)] = temp
    return "".join(str)

def reverse_3(str):
    str = list(str)
    length = len(str)
    for i in range(0, length//2):
        temp = str[i]
        str[i] = str[((length - 1) - i)]
        str[((length - 1) - i)] = temp
    return "".join(str)

def reverse_4(str):
    str = list(str)
    length = len(str)
    for i in range(0, length//2):
        str[i] = ord(str[i]) ^ ord(str[((length - 1) - i)])
        str[((length - 1) - i)] = chr(ord(str[((length - 1) - i)]) ^ ord(str[i]))
        str[i] = chr(ord(str[i]) ^ ord(str[((length - 1) - i)]))
    return "".join(str)

def reverse_5(str):
    return list(str).reverse().join(str)

# a 10110111
# b 01110110
# ^ 11000001
# a = a ^ b = 10110111 ^ 01110110 = 11000001
# b = b ^ a = 01110110 ^ 11000001 = 10110111
# a = a ^ b = 11000001 ^ 10110111 = 01110110

str1 = "Hello My Name Is Matthew"
rstr1 = reverse_1(str1)
print(rstr1)

str2 = "Hello My Name Is Matthew"
rstr2 = reverse_2(str2)
print(rstr2)

str3 = "Hello My Name Is Matthew"
rstr3 = reverse_2(str3)
print(rstr3)

str4 = "Hello My Name Is Matthew"
rstr4 = reverse_2(str4)
print(rstr4)

str5 = "Hello My Name Is Matthew"
rstr5 = reverse_2(str5)
print(rstr5)

str6 = "Hello My Name Is Matthew"
rstr6 = (lambda a : "".join(reversed(a)))(str6)
print(rstr6)

str7 = "Hello My Name Is Matthew"
rstr7 = str7[::-1]
print(rstr7)