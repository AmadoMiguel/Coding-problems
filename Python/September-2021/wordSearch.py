# You are given a 2D array of characters, and a target string. Return whether or not the word target word 
# exists in the matrix. Unlike a standard word search, the word must be either going left-to-right, 
# or top-to-bottom in the matrix.

# Example:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]

# Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down 
# in the first column.

# Here's the function signature:

def recur_word_search(curr_word:str,target_word:str,matrix,xIndx,yIndx):
    try:
        if (curr_word.__eq__(target_word)):
            return True
        next_letter = matrix[xIndx][yIndx]
        if target_word.startswith(curr_word+next_letter):
            curr_word += next_letter
        else:
            curr_word = next_letter
        if recur_word_search(curr_word,target_word,matrix,xIndx+1,yIndx) or\
            recur_word_search(curr_word,target_word,matrix,xIndx,yIndx+1):
            return True
        return False
    except IndexError:
        return False

def word_search(matrix, word):
    isWordPresent = recur_word_search("",word,matrix,0,0)
    if (isWordPresent):
        return True
    return False

  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'DMASS'))