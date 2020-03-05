
def findFirstRecuring(s):
	if len(s):
		hist = {}
		for c in s:
			hist[c] = hist.setdefault(c, 0) + 1
			if hist[c] == 2:
				return c
	return None

st = "qwertysjflkad;jkdjf;talsdf;ljas;ldjf;"
print(findFirstRecuring(st))
