def showWords(req,options):
    # Determine how long is te prefix
    nLetReq = len(req)
    # Make a list of the possible words to return
    foundWords = []
    for w in options:
        # If the prefix not in the word, skip it
        if w[:nLetReq] != req:
            continue
        foundWords.append(w)    
    return foundWords    

wrdsSet = ["arroz","agua","arriba","buey","carro"]
usrQuery = raw_input("Type in a query to search for a word: ")

foundWords = showWords(usrQuery,wrdsSet)

print(foundWords)