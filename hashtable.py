class HashTable:
    def __init__(self, size) -> None:
        self.data = [[] for i in range(0, size)]
    def _hash(self, key):
        hash = 0
        for i in range(0, len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash
    def set(self, key, value):
        address = self._hash(key)
        for i, item in enumerate(self.data[address]):
            if item[0] == key:
                self.data[address][i] = (key, value)
                break
            else:
                self.data[address].append((key, value))
        if len(self.data[address]) == 0:
            self.data[address].append((key, value))
    def get(self, key):
        retVal = None
        bucket = []
        address = self._hash(key)
        for item in self.data[address]:
            if item[0] == key:
                bucket.append(item)
        if len(bucket) > 0:
            retVal = bucket[0][1]
        return retVal
    def keys(self):
        keysArray = []
        for i in range(0, len(self.data)):
            if self.data[i]:
                for j in range(0, len(self.data[i])):
                    keysArray.append(self.data[i][j][0])
        return keysArray
    def printContents(self):
        print(self.data)

ht = HashTable(10)

ht.printContents()

ht.set("grapes", 100)

ht.printContents()

ht.set("grapes", 200)

ht.printContents()

ht.set("apples", 10)

ht.printContents()

print(ht.get("grapes"))
print(ht.get("apples"))

print(ht.keys())