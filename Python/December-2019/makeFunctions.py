# def make_functions():
#     flist = []
#
#     for i in [1, 2, 3, 4, 4, 4, 4, 5]:
#         def print_i():
#             print(i)
#         flist.append(print_i)
#     return flist

# functions = make_functions()
# for f in functions:
#     f()


# Rewriting the same
l = [1, 2, 3, 4, 4, 4, 4, 5]
for _ in l:
    print(l[-1])
