import random

k = int(input('Введите к: '))
res = ''

for i in range(k, -1, -1):
    if i >= 2:
        res += f'{random.randint(0, 100)}*x^{i} + '
    elif i == 1:
        res += f'{random.randint(0, 100)}*x + '
    else:
        res += f'{random.randint(0, 100)} = 0'
res = res.split()
for i in range(len(res)):
    if res[i].startswith('0'):
        res[i] = str(0)
    if res[i].startswith('1*x'):
        res[i] = res[i].replace('1*x', 'x')
res = ' '.join(res)
res = res.replace('0 + ', '').replace(' + 0', '')

file = open('file01.txt', 'w')
file.write(res)
file.close()
