# Array
#
# lookup O(1)
# push   O(1)
# insert O(n)
# delete O(n)

from unicodedata import name

from cv2 import detail_PairwiseSeamFinder


a = 1
b = 2

print(a, b)

a, b, = b, a

print(a, b)

string = "test"
string = string.replace("e", "X")
print(string)
print()

class MyClass:
    i = 12345
    def __init__(self, data) -> None:
        self.data = data
    
    def printData(self):
        self.i = 54321
        print(self.data, self.i)

c = MyClass(1)

c.printData()

c.counter = 12

print(c.counter)

del c.counter
MyClass.printData(c)

print("------------")

c2 = MyClass(2)
c2.inst = "INST"

print(c2.i)
c2.printData()
print(c2.i)
print(c2.inst)

print()

print(c.i)
c.printData()
print(c.i)

class MyClass2(MyClass):
    def __init__(self, data, data2) -> None:
        self.data = data
        self.data2 = data2
    
    def printData2(self):
        print(self.data, self.i)

c3 = MyClass2(3, 4)
c4 = MyClass2(4, 5)
c3.i = 111222
c3.printData()
c3.printData2()
c3.printData()

print(c.i)
print(c2.i)
del c2.i
print(c.i)
print(c2.i)

c4.printData()
c4.printData2()
c4.printData()

print("-------------")

class Employee:
    def __init__(self, name, dept, salary) -> None:
        self.name = name
        self.dept = dept
        self.salary = salary

e1 = Employee("Matthew", "Automation", 1000)

print(e1.name)

string = "Matthew"

for i in range(len(string)-1, 0-1, -1):
    print(string[i])

print("-------------")

if None:
    print("None is True")
else:
    print("None is False")