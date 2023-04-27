#my code
def delete_nth(order,max_e):
    result = []
    
    for i in order:
        count = 0
        
        for j in result:
            if j == i: count += 1
        if count < max_e:
            result.append(i)
            
    return result

order = [1,2,3,1,2,1,2,3]
max_e = 2
print(delete_nth(order,max_e))

# Alternative
'''
def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans
'''

'''
def delete_nth(order,max_e):
    return [o for i,o in enumerate(order) if order[:i].count(o)<max_e ]
'''