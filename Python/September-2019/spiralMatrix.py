# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
# import numpy
# import numpy as np

# def getSpiralFromMatrix(m):
#     # Initialize the list that will contain the elements in spiral order
#     spiral = []
#     # Initialize border indexes
#     upIndx = 0 # Is going to increment
#     rightIndex = m[0].size - 1 # is going to decrement
#     bottomIndex = len([r for r in m]) - 1 # is going to decrement
#     leftIndex = 0 # is going to increment
#     # Start iterating the matrix from left to right until all elements are added
#     while len(spiral) < m.size:
#         # From left to right in the top border index
#         for n in m[upIndx]:
#             # Avoid repeated elements
#             if n not in spiral:
#                 spiral.append(n)
#         # Transpose the matrix
#         m = np.transpose(m)
#         # From top to bottom in the right border index
#         for n in m[rightIndex]:
#             if n not in spiral:
#                 spiral.append(n)
#         m = np.transpose(m)
#         # From right to left in the bottom border index
#         for n in np.flip(m[bottomIndex]):
#             if n not in spiral:
#                 spiral.append(n)
#         m = np.transpose(m)
#         # From bottom to top in the left border index
#         for n in np.flip(m[leftIndex]):
#             if n not in spiral:
#                 spiral.append(n)
#         # Transpose back the matrix to its original shape
#         m = np.transpose(m)
#         # Decrement/increment each index of traversal of the matrix
#         upIndx += 1
#         rightIndex -= 1
#         leftIndex += 1
#         bottomIndex -= 1
#     return spiral

class CustomList(list):
    def __getitem__(self, i):
        if i < 0:
            raise IndexError("Only positive indexes accepted")
        item = list.__getitem__(self, i)
        if item is None:
            raise ArithmeticError("Cannot access this value")
        return item


def get_next_dir(curr_dir):
    if curr_dir == 'R':
        return 'D'
    elif curr_dir == 'D':
        return 'L'
    elif curr_dir == 'L':
        return 'U'
    elif curr_dir == 'U':
        return 'R'


def update_indexes(move_dir, row_idx, col_idx):
    if move_dir == 'R':
        return row_idx, col_idx + 1
    elif move_dir == 'D':
        return row_idx + 1, col_idx
    elif move_dir == 'L':
        return row_idx, col_idx - 1
    elif move_dir == 'U':
        return row_idx - 1, col_idx


def get_back_in_track(move_dir, row_idx, col_idx):
    if move_dir == 'R':
        return row_idx, col_idx - 1
    elif move_dir == 'D':
        return row_idx - 1, col_idx
    elif move_dir == 'L':
        return row_idx, col_idx + 1
    elif move_dir == 'U':
        return row_idx + 1, col_idx


def print_in_spiral(m):
    end_control = 0
    # Start printing from the top left corner, towards right side
    moving_dir = 'R'
    col_idx, row_idx = 0, 0
    while True:
        if end_control > 2:
            print(m)
            break
        try:
            print(m[row_idx][col_idx])
            m[row_idx][col_idx] = None
            end_control = 0
            row_idx, col_idx = update_indexes(moving_dir, row_idx, col_idx)
        except (IndexError, ArithmeticError):
            # Go back one step in the same direction and then redirect
            end_control += 1
            row_idx, col_idx = get_back_in_track(moving_dir, row_idx, col_idx)
            moving_dir = get_next_dir(moving_dir)
            row_idx, col_idx = update_indexes(moving_dir, row_idx, col_idx)


mat = CustomList([
    CustomList([1,  2,  3,  4,  5]),
    CustomList([6,  7,  8,  9,  10]),
    CustomList([11, 12, 13, 14, 15]),
    CustomList([16, 17, 18, 19, 20]),
    CustomList([21, 22, 23, 24, 25])])

print_in_spiral(mat)
