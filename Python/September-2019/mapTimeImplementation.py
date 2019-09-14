# Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.
#
# It should contain the following methods:
#
# set(key, value, time): sets key to value for t = time.
# get(key, time): gets the key at t = time.
# The map should work like this. If we set a key at a particular time, it will maintain that value forever
# or until it gets set at a later time. In other words, when we get a key at a time, it should return the
# value that was set for that key set at the most recent time.


class MapWithTime:
    def __init__(self):
        # Map that will contain inner maps. Each key-value pair is the key and a map assigned to it.
        # Inside that second map, the key value pairs are going to be the time and the value for that time.
        self.parentMap = {}
    def set(self, k, v, t):
        # If the key is already in the dictionary, assign/update the value for the corresponding time
        if k in self.parentMap.keys():
            self.parentMap[k][t] = v
        # If not, create a new map of time-value pairs for that key
        else:
            self.parentMap[k] = {}
            self.parentMap[k][t] = v
    def get(self, k, t):
        return self.parentMap[k][t]
    def showParentMap(self):
        print(self.parentMap)


# Create a new instance of the map with time class
mapWithTimeInstance = MapWithTime()
# Set different values to the same key at different times
mapWithTimeInstance.set('a', 1, 0)
mapWithTimeInstance.set('a', 2, 1)
mapWithTimeInstance.set('a', 4, 2)
# Retrieve each value
v1 = mapWithTimeInstance.get('a', 0)
v2 = mapWithTimeInstance.get('a', 1)
v3 = mapWithTimeInstance.get('a', 2)
# Verify
print(v1, v2, v3)
# Check parent map
mapWithTimeInstance.showParentMap()
