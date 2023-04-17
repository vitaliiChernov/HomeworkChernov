f = open('input.txt', 'r')
for line in f:
    a = line.split()
    fizz = int(a[0])
    buzz = int(a[1])
    number = int(a[2])
        
    for i in range(1, number + 1):
        if not(i%fizz or i%buzz):
            print('FB', end = ' ')
        elif not (i%fizz) :
            print('F', end = ' ')
        elif not (i%buzz):
            print('B', end = ' ')
        else:
            print(i, end = ' ')
    print('\n')
    
f.close()