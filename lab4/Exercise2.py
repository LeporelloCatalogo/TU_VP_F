'''
Напишете програма, която приема текст от потребителя и намира кой символ
се среща най-много пъти в него (без да броим интервалите, ако има такива).
Изведете самия символ и броя на срещанията му.
'''

text = input('Type your text: ').replace(" ", '')

uniqueChars = set(text)

n = 0
frequentChar = 'no chars found'
for i in uniqueChars:
    if n < text.count(i):
        frequentChar = i
        n = text.count(i)

print(f'{frequentChar} = {n}')
