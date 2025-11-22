import sys
def levdist(s: str, t:str):
    if s == '':
        return len(t)
    if t == '':
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
    dist = min([
        levdist(s[:-1] ,t) + 1,
        levdist(s, t[:-1]) + 1,
        levdist(s[:-1], t[:-1]) + cost])
    return dist
print(levdist(sys.argv[1], sys.argv[2]))

