# Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface,
# which also implements peek(). peek shows the next element that would be returned on next().


class PeekableIterator:
    list = []

    def __init__(self, list):
        self.list = list

    # Show the next element that would be returned from the next() method
    def peek(self):
        print("Showing next value from peek():", self.list[0])

    # Return next element and remove it from the list
    def next(self):
        currentElem = self.list[0]
        del self.list[0]
        return currentElem

    # Check if list has at least one element
    def hasNext(self):
        return len(self.list) > 0


# Instantiate the iterator
list = [1, 3, 5, 6, 2, -8, 9]
peekIter = PeekableIterator(list)
while peekIter.hasNext():
    peekIter.peek()
    nextVal = peekIter.next()
    print("Here is the next value:", nextVal)
print("List was succesfully iterated!")
