'''1 - 1
2 - 3 5
3 - 7 9 11 '''
a = []
count = 1
n = 3
for i in range(1, n + 1):
    for j in range(i, n + 1):
        a.append(count)
        count += 2
# print(a[-5: ])
s = 0
for i in a[-n:]:
    s += i
print(s)

'''
def row_sum_odd_numbers(n):
    # sum of numbers in each row equals number of the row to the power of 3
    return n**3
'''
