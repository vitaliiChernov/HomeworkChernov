def get_average(lst): 
    s = 0
    n = 0
    for i in lst:
        s += i['age']
        n += 1
    return round(s / n)

'''
alternative

def get_average(lst): 
    return round(sum(x["age"] for x in lst) / len(lst))
    
get_average = lambda L: round(sum(d['age'] for d in L)/len(L))



'''