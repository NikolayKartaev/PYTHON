file = open('INFO.txt', 'r', encoding='utf-8')

resultData = list()
for line in file.readlines():
    resultData.append(tuple(line.split('\n')[0].split(';')))

print(resultData)
file.close()

'''
a - режим добавления
w - режим на запись (очищает файл)
r - режим считывания
'''