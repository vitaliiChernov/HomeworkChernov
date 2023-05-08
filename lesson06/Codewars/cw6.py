'''
You will be given an array of objects (associative arrays in PHP, table in COBOL) representing data about developers who have signed up to attend the next coding meetup that you are organising.
Your task is to return an object (associative array in PHP, table in COBOL) which includes the count of each coding language represented at the meetup.
For example, given the following input array:
list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
    { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
    ]
    
{ 'C': 2, 'JavaScript': 1, 'Ruby': 1 }
'''

def count_languages(lst):
    lang = []
    for i in lst:
        lang.append(i['language'])
    norep = []
    norepCount = []
    
    for i in lang:
        if i not in norep:
            norep.append(i)
            norepCount.append(lang.count(i))
    
    return dict(zip(norep, norepCount))

list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
    { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
    ]
print(count_languages(list1))

'''
alternative

from collections import Counter
def count_languages(lst): 
    return Counter([d['language'] for d in lst])
    
def count_languages(lst): 
    language = [el['language'] for el in lst]
    return {i: language.count(i) for i in language}
    
count_languages = lambda devs: __import__("collections").Counter(d["language"] for d in devs)
    
'''