circle = []
def circleOfWords(wordsList):
    global circle
    firstWord = wordsList[0]
    circle.append(firstWord)
    wordsList.remove(firstWord)
    def canFormCircle(wordsSubList,firstWord): 
        wordFound = False
        for w in wordsList:
            # Check if next word can be added to the circle
            if firstWord[-1] == w[0]:
                print(w)
                # If so, add it to the circle..
                wordFound = True
                circle.append(w)
                # Prepare next word to be compared to the rest of the words
                nextWord = w
                wordsSubList.remove(w)
                break    
        if wordFound:         
            canFormCircle(wordsSubList,nextWord) 
        else:  
            print(circle)
    # Start verifying if circle can be formed        
    canFormCircle(wordsList,firstWord)           

circleOfWords(["aaa", "bbb", "baa", "aab"])