# Візьміть файл, в якому є багато англійських слів у рядках.
# Порахуйте частоту зустрічі кожного слова та видрукуйте
# відсортовано.

f = open('input.txt', 'r')
listWords = [] #загальний список усіх слів із файлу
for line in f:
    a = line.split() # рядок перетворюємо на список зі слів
    listWords += a #додаємо список до загального списку слів

listWord = [] # список слів без повторень
countWord = [] # список із частоти зустрічі кожного слова

for word in listWords:
    if word not in listWord:
        listWord.append(word)
        countWord.append(listWords.count(word))
        
result = [] # впорядкований масив з частотою зустрічі слів
k = len(listWord)
for i in range(k):
    indexE = countWord.index(max(countWord))
    result.append(listWord[indexE] + ' ' + str(countWord[indexE]))
    countWord[indexE] = 0

print(result)
   
f.close()

''' Result
['the 9', 'as 4', 'Python 3', 'in 3', 'a 3', 'to 3', 'his 3', 'was 2',
'by 2', 'Rossum 2', 'for 2', 'lead 2', 'conceived 1', 'late 1', '1980 1',
'Guido 1', 'van 1', 'at 1', 'Centrum 1', 'Wiskunde 1', '& 1', 'Informatica 1',
'CWI 1', 'Netherlands 1', 'successor 1', 'ABC 1', 'programming 1', 'language, 1',
'which 1', 'inspired 1', 'SETL, 1', 'capable 1', 'of 1', 'exception 1', 'handling 1',
'and 1', 'interfacing 1', 'with 1', 'Amoeba 1', 'operating 1', 'system. 1', 'Its 1',
'implementation 1', 'began 1', 'December 1', '1989. 1', 'Van 1', 'shouldered 1',
'sole 1', 'responsibility 1', 'project, 1', 'developer, 1', 'until 1', '12 1', 'July 1',
'2018, 1', 'when 1', 'he 1', 'announced 1', 'permanent 1', 'vacation 1', 'from 1',
'responsibilities 1', "Python's 1", 'benevolent 1', 'dictator 1', 'life, 1', 'title 1',
'community 1', 'bestowed 1', 'upon 1', 'him 1', 'reflect 1', 'long-term 1', 'commitment 1',
"project's 1", 'chief 1', 'decision-maker. 1', 'In 1', 'January 1', '2019, 1', 'active 1',
'core 1', 'developers 1', 'elected 1', 'five-member 1', 'Steering 1',
'Council 1', 'project. 1']
'''