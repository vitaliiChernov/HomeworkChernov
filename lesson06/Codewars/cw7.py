'''
You will be given an array of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.
Given the following input array:
list1 = [
  { firstName: 'Aba', lastName: 'N.', country: 'Ghana', continent: 'Africa', age: 21, language: 'Python' },
  { firstName: 'Abb', lastName: 'O.', country: 'Israel', continent: 'Asia', age: 39, language: 'Java' }
];

[
  { firstName: 'Abb', lastName: 'O.', country: 'Israel', continent: 'Asia', age: 39, language: 'Java' }
]
'''
def find_odd_names(lst):
    result = []
    
    for i in lst:
        f = i['firstName']
        s = 0
        for j in f:  
            s += ord(j)
        if s % 2:
            result.append(i)
            
    return result

list1 = [
  { 'firstName': 'Aba', 'lastName': 'N.', 'country': 'Ghana', 'continent': 'Africa', 'age': 21, 'language': 'Python' },
  { 'firstName': 'Abb', 'lastName': 'O.', 'country': 'Israel', 'continent': 'Asia', 'age': 39, 'language': 'Java' }
]

print(find_odd_names(list1))

'''
alternative

def find_odd_names(lst): 
    return [x for x in lst if sum(map(ord, x["firstName"])) % 2]
    
def find_odd_names(lst): 
    return [*filter(lambda d: sum(map(ord, d['firstName']))&1, lst)]
    '''