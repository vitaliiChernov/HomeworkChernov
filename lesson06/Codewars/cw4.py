''' 1 version
def find_admin(lst, lang): 
    result = []
    for i in lst:
        if i['language'] == lang and i['githubAdmin'] == 'yes'
        result.append(i)
    return result
'''
def find_admin(lst, lang): 
    return [i for i in lst if i['language']==lang and i['githubAdmin']=='yes']
'''
alternative

find_admin = lambda L, l: [U for U in L if U['githubAdmin']=='yes' and U['language']==l]
'''