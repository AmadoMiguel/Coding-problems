# Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum
# of vertex values equals s.


def hasPathWithGivenSum(t, s):
    if not t:
        return s == 0
    currSum = s - t.value
    # Check leaf node
    if not currSum and not t.left and not t.right:
        return True
    hasSum = False
    if t.left:
        hasSum = hasSum or hasPathWithGivenSum(t.left, currSum)
    if t.right:
        hasSum = hasSum or hasPathWithGivenSum(t.right, currSum)
    return hasSum

