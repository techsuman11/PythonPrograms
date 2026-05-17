#Collision handling in hashtable code basics code
#Video link: https://www.youtube.com/watch?v=54iv1si4YCM&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=6
#solution1: in every array index, we are storing list type, in each list, we are storing touple with key and value
#solution2: in every array index, we can store dictionary type with key and value.
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", index)
                del self.arr[arr_index][index]

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67

#march 6 and march 17 has same hashkey
print("hash key of march 6 is: "+str(t.get_hash("march 6")))
print("hash key of march 17 is: "+str(t.get_hash("march 17")))
t["march 17"] = 63457
print(t.arr)