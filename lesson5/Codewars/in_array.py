#my code
def in_array(array1, array2):
    result = []
    for i in array1:
        for j in array2:
            if i in j and i not in result:
                result.append(i)
                break
    result.sort()     
    return result

array1 = ['live', 'arp', 'strong']
array2 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(array1, array2))

# Alternative
'''
def in_array(array1, array2):
    a = set(x for x in array1 for j in array2 if x in j)
    return sorted(a)
'''

