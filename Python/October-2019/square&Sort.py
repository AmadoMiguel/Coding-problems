# Given a sorted list of integers, square the elements and give the output in sorted order.


def squareAndSortArray(arr):
    return sorted([i * i for i in arr])


print(squareAndSortArray([-9, -2, 0, 2, 3]))
