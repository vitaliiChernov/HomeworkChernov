def is_same_language(lst):
    
    for i in lst:
        if i['language'] != lst[0]['language']:
            return False
        
    return True

'''
alternative
def is_same_language(lst):
    return len(set(i['language'] for i in lst))<2
    
'''