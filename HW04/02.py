file = open('file21.txt', 'w')
file.write('x^5 + 36*x^4 + x^3 + x + 79 = 0')
file.close()

file = open('file22.txt', 'w')
file.write('9*x^3 + 65*x^2 + 79 = 0')
file.close()

file = open('file21.txt', 'r')
equation1 = file.read()
file.close()

file = open('file22.txt', 'r')
equation2 = file.read()
file.close()


# print(f'уравнение 1 {equation1}')
# print(f'уравнение 2 {equation2}')


def equation_dict(equation):
    equation = equation.replace(' ', '').replace('=0', '')
    equation = equation.split('+')
    for i in range(len(equation)):
        if equation[i].startswith('x'):
            equation[i] = equation[i].replace('x', '1*x')
        if equation[i].endswith('x'):
            equation[i] = equation[i].replace('x', 'x^1')
        if 'x' not in equation[i]:
            equation[i] += '*x^0'

    my_dict = {}
    for i in equation:
        i = i.split('*')
        my_dict[i[1]] = i[0]

    return (my_dict)


# print(f'словарь 1 {equation_dict(equation1)}')
# print(f'словарь 2 {equation_dict(equation2)}')


def sum_dict(my_dict1, my_dict2):
    sum_dict = {}

    for k, v in my_dict1.items():
        sum_dict[k] = int(v) + int(my_dict2.get(k, 0))

    my_dict2.update(sum_dict)

    return my_dict2


my_sum_dict = (sum_dict(equation_dict(equation1), equation_dict(equation2)))


def dict_list(dict):
    my_list = []
    for k, v in dict.items():
        my_list.append(str(v) + '*' + k)

    for i in range(len(my_list) - 1, -1, -1):
        for j in range(len(my_list) - 1, -1, -1):
            if my_list[j].endswith(str(i)):
                temp = my_list[len(my_list) - 1 - i]
                my_list[len(my_list) - 1 - i] = my_list[j]
                my_list[j] = temp
    return my_list


sum_list = (dict_list(my_sum_dict))
# print(f'отформатированный лист с суммами {sum_list}')

for i in range(len(sum_list)):
    if '*x^0' in sum_list[i]:
        sum_list[i] = sum_list[i].replace('*x^0', '')
    if '*x^1' in sum_list[i]:
        sum_list[i] = sum_list[i].replace('*x^1', '*x')
    if sum_list[i].startswith('1*x'):
        sum_list[i] = sum_list[i].replace('1*x', 'x')

res = ' + '.join(sum_list) + " = 0"

file = open('file23.txt', 'w', encoding='UTF-8')
file.write('Сумма многочленов:\n')
file.write(res)
file.close()