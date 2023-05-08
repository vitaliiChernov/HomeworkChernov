# a - string, b - taple, c - list (c[i] = (a[i], b[i])
def myZip(x, y):
    c = []
    lenA = len(x)
    lenB = len(y)
    if lenA < lenB: n = lenA
    else: n = lenB
    
    for i in range(n):
        c.append((a[i], b[i]))
    
    return c

a = 'abc'
b = (10, 20, 30)
    
print(myZip(a, b))   