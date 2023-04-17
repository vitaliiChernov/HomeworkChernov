f = open('input.txt', 'r')
o = open('output.txt', 'w')
for line in f:
    a = line.split()
    fizz = int(a[0])
    buzz = int(a[1])
    number = int(a[2])
    lineAp = ''    
    for i in range(1, number + 1):
        if not(i%fizz or i%buzz):
            lineAp = lineAp + 'FB' + ' '
        elif not (i%fizz) :
            lineAp = lineAp + 'F' + ' '
        elif not (i%buzz):
            lineAp = lineAp + 'B' + ' '
        else:
            lineAp = lineAp + str(i) + ' '
    print(lineAp)
    
    o.write(lineAp + '\n')
    
f.close()
o.close()