'''
2 + 2 => 4
1 + 2 * 3 => 7
1 - 2 * 3 => 5
'''
from string import punctuation

data_1 = "-2*2+2+(10/5-3)"
data_2 = "1+2/2*4"
data_3 = "1-2*3"
data_4 = '-2-(8+4-3-15)*(4/4-2)'

calc = {
    '*': lambda x, y: int(x) * int(y),
    '/': lambda x, y: int(x) / int(y),
    '+': lambda x, y: int(x) + int(y),
    '-': lambda x, y: int(x) - int(y)
}
value = '*/'

def convert(data: list):
    for i in punctuation:
        data = data.replace(i, ' ' + i + ' ')
    return data.split()


def check_first_symb(data: list):
    if data[0] == '-':
        data[1] = str(-int(data[1]))
        data.pop(0)
    return data


def switch_value():
    global value
    if value == '*/':
        value = '+-'
    else:
        value = '*/'
    return value


def check_symb(data: list):
    global value
    for i in range(len(data)):
        if data[i] in '(':
            while data.index(')') - data.index('(') > 2:
                range_symb = [data.index('(') + 1, data.index(')')]
                return range_symb
            data.pop(data.index(')'))
            data.pop(data.index('('))
            value = '*/'
            check_symb(data)
        if i == len(data) - 1:
            return [0, len(data)]


def oper(data: list):
    global value
    range_symb = check_symb(data)
    while range_symb[0] < range_symb[1]:

        if data[range_symb[0]] in value:
            data[range_symb[0] - 1] = str(
                int((calc[data[range_symb[0]]](data[range_symb[0] - 1], data[range_symb[0] + 1]))))
            data.pop(range_symb[0] + 1)
            data.pop(range_symb[0])
            range_symb = check_symb(data)
        else:
            range_symb[0] += 1


def calculator(data: list):
    global value
    while '(' in data:
        oper(data)
        value = switch_value()

    i = 0
    value = '*/'
    while len(data) > 1:
        if data[i] in value:
            data[i - 1] = str(calc[data[i]](data[i - 1], data[i + 1]))
            data.pop(i + 1)
            data.pop(i)
            i -= 1
        i += 1

        if i == len(data):
            value = switch_value()
            i = 0
    return data

data = convert(data_4)
new_data = calculator(check_first_symb(data))
print(*new_data)
