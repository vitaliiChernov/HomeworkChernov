# Банкомат видає суму максимально можливими купюрами
# Існують купюри номіналом 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1 грн.
balans = int(input('balans = '))
nominal = [1000, 500, 200, 100, 50, 20, 10]
for i in nominal:
    numberBill = balans // i
    if numberBill:
        print(i, '-', numberBill)
    balans = balans % i
