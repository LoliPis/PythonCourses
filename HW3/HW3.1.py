def count_letter(lists, letter):
    sumL = 0
    for word in lists:
        if  letter in word:
            sumL += 1
    print(sumL)

wordsList = []

words = int(input('Сколько будет слов? '))
for i in range(words):
    wordsList.append(input('Введите слово: '))
lett = input('Введите букву, наличие которой хотите проверить: ')

count_letter(wordsList, lett)
