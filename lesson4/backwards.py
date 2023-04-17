import sys
filename = sys.argv[0]
# далі відкриваємо файл для читання (опція 'r')
f = open(filename, 'r', encoding = 'utf-8') # в файлі тепер file descriptor
a =[]

for line in f: # для кожного рядка у файлі
    a.append(line)
    
b = a[::-1]
for i in b:
    print(i)

f.close() # закриття файлу