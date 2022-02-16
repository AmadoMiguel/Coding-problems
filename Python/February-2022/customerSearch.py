

def searchInRepo(query, lQuery, repo):
    numSug = 0
    suggestions = []
    for w in repo:
        if numSug == 3:
            break
        if query == w[:lQuery]:
            suggestions.append(w)
            numSug += 1
    return suggestions


# Overall time complexity -> O(N * M)
def searchSuggestions(repo, custQuery):
    # Optimize repository so that it only contains relevant words based on the first 2 chars of the custQuery
    optimalRepo = []
    custQuery = custQuery.lower()
    # O(N)
    for w in repo:
        if w[:2].lower() == custQuery[:2]:
            optimalRepo.append(w.lower())
    # O(Nlog(N))
    optimalRepo = sorted(optimalRepo)
    suggestions = []
    lQuery = len(custQuery)
    # O(M)
    for i in range(lQuery+1):
        if i > 1:
            # O(N)
            sugRes = searchInRepo(custQuery[:i], i, optimalRepo)
            suggestions.append(sugRes)
    return suggestions


print(searchSuggestions(["Mobile", "mouse", "mOneypot", "moNitor", "mousepad", "fIsH", "potatoes"], "mon"))
