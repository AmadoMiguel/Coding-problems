# Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the
# following methods:
#
# next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
# has_next(): returns whether or not the iterator still has elements left.
# For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.
#
# Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.


class NoMoreElementsException(Exception):
    pass


class Iterator2D(object):
    def __init__(self, parentArray):
        self.parentArray = parentArray
        self.outerPtr, self.innerPtr = 0, 0

    def next(self):
        if self.outerPtr <= len(self.parentArray):
            if self.innerPtr < len(self.parentArray[self.outerPtr]):
                value = self.parentArray[self.outerPtr][self.innerPtr]
                if self.innerPtr + 1 < len(self.parentArray[self.outerPtr]):
                    self.innerPtr += 1
                    return value
                elif self.outerPtr < len(self.parentArray):
                    self.innerPtr = 0
                    self.outerPtr += 1
                    return value
                else:
                    raise NoMoreElementsException("There are no more elements in the array")
            elif not len(self.parentArray[self.outerPtr]):
                self.innerPtr = 0
                self.outerPtr += 1
                return None
            else:
                value = self.parentArray[self.outerPtr][self.innerPtr]
                self.innerPtr = 0
                self.outerPtr += 1
                return value
        else:
            raise NoMoreElementsException("There are no more elements in the array")

    def has_next(self):
        if self.outerPtr < len(self.parentArray):
            return True
        return False


iter = Iterator2D([[], [1, 2], [3], [], [4]])
while iter.has_next():
    v = iter.next()
    if v is not None:
        print(v)
