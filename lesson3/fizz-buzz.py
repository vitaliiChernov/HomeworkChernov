fizz = int(input('fizz = '))
buzz = int(input('buzz = '))
number = int(input('number = '))

for i in range(1, number + 1):
    if not(i%fizz or i%buzz):
        print('FB', end = ' ')
    elif not (i%fizz) :
        print('F', end = ' ')
    elif not (i%buzz):
        print('B', end = ' ')
    else:
        print(i, end = ' ')    