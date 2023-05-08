'''
The rest of your team will make sure that the argument is
sanitized before being passed to your function although you
will need to account for adding trailing zeros if they are
missing (though you won't have to worry about a dangling period).

Examples:
3 needs to become $3.00
'''
def format_money(amount):
    amount = str((float(amount)))
    a = list(amount.split('.'))
    if len(a[1]) < 2: return '$' + amount + '0'
    return '$' + amount

amount = 3.87
print(format_money(amount))

''' alternative
def format_money(amount):
    return '$%0.2f' % amount
    
    
def format_money(amount):
    # your formatting code here
    return f'${amount:.2f}'
    
format_money = lambda x: '${:.2f}'.format(x)
'''