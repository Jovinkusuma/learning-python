kata = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

def number(x):
    if x < 11:
        return kata[x]
    elif x < 20:
        if x % 10 == 1:
            return 'eleven'
        elif x % 10 == 2:
            return 'twelve'
        elif x % 10 == 3:
            return 'thirteen'
        elif x % 10 == 5:
            return 'fifteen'
        else:
            return kata[x%10] + 'teen'
    elif x < 100:
        if x // 10 == 2: 
            return 'twenty ' + (number(x % 10) if x % 10 != 0 else ' ')
        if x // 10 == 3:
            return 'thirty ' + (number(x % 10) if x % 10 != 0 else ' ')
        if x // 10 == 5:
            return 'fifty ' + (number(x % 10) if x % 10 != 0 else ' ')
        else:
            return kata[x // 10] + 'ty ' + (number(x % 10) if x % 10 != 0 else '')
    elif x < 1000:
        return kata[x // 100] + ' hunderds and ' + (number(x % 100) if x % 100 != 0 else '')
    elif x < 1000000:
        return number(x // 1000) + ' thousands, ' + (number(x % 1000) if x % 1000 != 0 else '')
    elif x < 1000000000:
        return number(x // 1000000) + ' millions, ' + (number(x % 1000000) if x % 1000000 != 0 else '')
    elif x < 1000000000000:
        return number(x // 1000000000) + ' billions, ' + (number(x % 1000000000) if x % 1000000000 != 0 else '')

import os 
while True:
    os.system ('cls')
    try:
        h = int(input('number? '))
    except:
        print('Number please')
        os.system('pause')
    else:
        print(f'{h} = {number(h)}')
        os.system('pause')