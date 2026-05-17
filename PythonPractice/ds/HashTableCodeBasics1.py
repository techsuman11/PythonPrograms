class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
print(t.arr)
#march 6 and march 17 has same hashkey
print("hash key of march 6 is: "+str(t.get_hash("march 6")))
print("hash key of march 17 is: "+str(t.get_hash("march 17")))
#Collision with march 6 because it has same hash of march 17, so value will override
t["march 17"] = 459
#printing elements
print(t.arr)





