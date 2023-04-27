# my code
def invert(lst):
    result = []
    if lst == result:
        return lst
    len_lst = len(lst)
    for i in range(len_lst):
        result.append(-lst[i])
    return result

lst = [1, 2, 3, 0, -4, -5]
print(invert(lst))

# alternative

'''
def invert(lst):
    return [-x for x in lst]
'''

'''
def invert(lst):
    return list(map(lambda x: -x, lst))
'''

'''
def invert(lst):
    return list(map(int.__neg__, lst))
'''