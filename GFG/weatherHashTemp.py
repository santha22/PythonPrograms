weather_dict = {}
with open("nyc_weather.csv") as f:
    for line in f:
        tokens = line.split(",")
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            print("Invalid temperature. Ignore the row")

print(weather_dict)

print(weather_dict["Jan 9"])  # temperature on Jan 9

print(weather_dict["Jan 4"])   # temperature on Jan 9
"""
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self,key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found  = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))

    def __delitem___(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", index)
                del self.arr[arr_index][index]


t = HashTable()
print(t.arr)"""