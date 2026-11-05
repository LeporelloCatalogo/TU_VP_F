'''
Имаме списък с числа, в който някои числа се повтарят многократно (напр. [1,
2, 2, 3, 1, 4, 2]).Напишетепрограма, която премахва дубликатите, но
запасва първоначалния ред на числата в нов списък. (Подсказка: множествата
в Python разбъркват реда, затова помислете за проверка с if x not in
new_list в цикъл)'''

collection = list(input('The list of numbers: ').replace(' ',''))

newCollection = list()

for i in range(0, len(collection)):
    if collection[i] not in newCollection:
        newCollection.append(collection[i])

print(newCollection)