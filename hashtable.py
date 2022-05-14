class HashTable:
    def __init__(self, size) -> None:
        self.data = [[] for i in range(0, size)]
    def _hash(self, key):
        hash = 0
        for i in range(0, len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash
    def set(self, key, value):
        hash = self._hash(key)
        self.data[hash].append((key, value))
    def get(self, key):
        retVal = []
        hash = self._hash(key)
        for item in self.data[hash]:
            if item[0] == key:
                retVal.append(item)
        return retVal
    def printContents(self):
        print(self.data)

ht = HashTable(10)

ht.printContents()

ht.set("grapes", 100)
ht.set("grapes", 200)

ht.printContents()

print(ht.get("grapes"))