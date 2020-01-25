# Implement a PrefixMapSum class with the following methods:
#
# insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
# sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
# For example, you should be able to run the following code:
#
# mapsum.insert("columnar", 3)
# assert mapsum.sum("col") == 3
#
# mapsum.insert("column", 2)
# assert mapsum.sum("col") == 5


class PrefixMapSum(object):
    def __init__(self):
        self.prefixMapSum = {}

    def insert(self, key: str, value: int):
        self.prefixMapSum[key] = value

    def sum(self, prefix: str):
        prefixTotal = 0
        for k in self.prefixMapSum.keys():
            if k.startswith(prefix):
                prefixTotal += self.prefixMapSum[k]
        return prefixTotal

    def pop(self, key: str = None):
        if key is not None:
            if key in self.prefixMapSum.keys():
                del self.prefixMapSum[key]
            else:
                raise KeyError("Key not found in the Map")
        else:
            raise KeyError("Key cannot be 'None'")

    def __str__(self):
        toString = "{\n\t"
        for k, v in self.prefixMapSum.items():
            toString += (k + " : " + str(v)) + ",\n"
            toString += "\t"
        toString = toString[:-1] + "}"
        return toString


mapSumObj = PrefixMapSum()
mapSumObj.insert("co", 2)
mapSumObj.insert("col", 3)
mapSumObj.insert("cal", 4)
mapSumObj.insert("color", 5)
mapSumObj.insert("calor", 1)
mapSumObj.insert("calories", 1)

print(mapSumObj)
assert mapSumObj.sum("co") == 10  # True

mapSumObj.pop("co")

assert mapSumObj.sum("co") == 8  # True
print(mapSumObj)

assert mapSumObj.sum("ca") == 6  # True
