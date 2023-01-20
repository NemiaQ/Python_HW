# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc
text = input('Введите текст: ')
file = open('fileStart.txt', 'w')
file.write(text)
file.close()

file = open('fileStart.txt', 'r')
text = file.read()
file.close()

count = 1
new_text = ''
for i in range(0, len(text)):
    if text[0].isalpha():
        if i == len(text) - 1:
            new_text += str(count) + text[i]
        elif text[i] == text[i + 1]:
            count += 1
        else:
            new_text += str(count) + text[i]
            count = 1

    if text[0].isdigit():
        if text[i].isdigit():
            new_text += text[i + 1] * int(text[i])

# print(new_text)

file = open('fileEnd.txt', 'w')
file.write(new_text)
file.close()
