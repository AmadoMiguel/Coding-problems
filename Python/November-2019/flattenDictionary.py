# Write a function to flatten a nested dictionary. Namespace the keys with a period.
#
# For example, given the following dictionary:
#
# {
#     "key": 3,
#     "foo": {
#         "a": 5,
#         "bar": {
#             "baz": 8
#         }
#     }
# }
# it should become:
#
# {
#     "key": 3,
#     "foo.a": 5,
#     "foo.bar.baz": 8
# }
# You can assume keys do not contain dots in them, i.e. no clobbering will occur.


def flattenDict(dicti, currentKey, flatDicti):
    # Iterate over the keys of the current dictionary
    for k in dicti.keys():
        currentKey.append(k)
        if issubclass(type(dicti[k]), dict):
            flatDicti = flattenDict(dicti[k], currentKey, flatDicti)
        else:
            flatDicti[".".join(currentKey)] = dicti[k]
            currentKey.remove(k)
        if k in currentKey:
            currentKey.remove(k)
    return flatDicti


print(flattenDict({
                    "key": 3,
                    "foo": {
                        "a": 5,
                        "bar": {
                            "baz": 8,
                            "blim": 9
                        },
                        "celt": {
                            "kau": {
                                "klim": 4
                            },
                            "dor": 4,
                            "li": [56]
                        },
                        "jau": {
                            "leu": 34
                        },
                        "ket": 4,
                        "ko": 5
                    }
                }, [], {}))
