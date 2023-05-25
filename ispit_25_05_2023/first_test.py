```
def spam(number):
    '''Эта функция принимает числовой параметр. Должна вернуть строку, которая
    повторяется столько раз, сколько параметров передано. Она уже написана,
    но не работает. Любым способом заставьте ее работать.
    '''
    return 'bulochka' * number


def my_sum(list_of_numbers):

    """
    Функция получает на вход массив чисел, должна вернуть сумму этих чисел.
    Не использовать встроенные функции суммирования.
    """
    sum = 0
    for i in list_of_numbers:
        sum += i
        
    return sum


def shortener(string):
    """
    Function receives a long string with many words.
    It should return the same string, but words,
    larger then 6 symbols should be changed, symbols
    after the sixth one should be replaced by symbol *
    :param string
    :returns string

     Функция получает на вход длинную строку с множеством слов.
     Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
     функция должна вместо всех символов после шестого поставить одну звездочку.
     Пример: Из слова 'verwijdering' должно получиться 'verwij*'

    """
    my_list = string.split()
    result = []
    for i in my_list:
        if len(i) > 6:
            i = i[:6] + '*'
        result.append(i)
    
    new_string = ''
    for i in result:
        new_string += i + ' '
    return new_string[:-1]
    #  ...wite your code here


def compare_ends(words):
    """
    Function receives an array of strings.
    Please return number of strings, which
    length is at least 2 symbols and first character
    is equal to the last character

    Функция получает на вход массив строк. Вернуть надо количество строк,
    которые не короче двух символов и у которых первый и последний
    символ совпадают.

    """
    count = 0
    for i in words:
        if (len(i) >= 2) and (i[0] == i[-1]):
            count += 1
    return count
    #  ...wite your code here
```
