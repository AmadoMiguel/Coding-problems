# A function that returns a pair of elements
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
# Returns the first value of the function
def car(f):
    def first(a,b):
        return a
    return f(first)
# Returns the second value of the function
def cdr(f):
    def second(a,b):
        return b
    return f(second)

print(car(cons(1,2)),cdr(cons(1,2)))