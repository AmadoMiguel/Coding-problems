# Given a string of parentheses, write a function to compute the minimum number of parentheses
# to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

def numRemovedParenthesis(parStr):
    # Use two arrays; one for storing opening parenthesis, other for storing closing parenthesis
    opening = []
    closing = []
    for b in parStr:
        if b == '(':
            opening.append(b)
        else:
            closing.append(b)
    # Compare the length between them. The difference between the arrays is the result of
    # the number of parenthesis to be removed to balance the string
    toBeRemoved = abs(len(opening) - len(closing))
    return toBeRemoved

print( "Number of parenthesis to be removed:", numRemovedParenthesis("()(()))") )