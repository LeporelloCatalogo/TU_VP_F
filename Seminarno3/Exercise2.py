'''
Напишете програма на Python, която създава списък от n въведени 
от потребителя низа и извършва следните обработки: определя кой от 
записаните в списъка низове е с най-голяма дължина, заменя търсен низ с друг 
въведен от потребителя, изтрива избран низ и вмъква нов низ в избрана 
позиция в списъка. 
'''

n = int(input('List capacity: '))
chars = list()
for i in range(n):
    chars.append(input(f'{i+1} text: '))

print(max(chars, key=len))

for i in range(len(chars)):
    print(f'{i+1}: {chars[i]}')

changeIndex = int(input('Which element to change: ')) - 1
changeValue = input('What will you change it with: ')

chars[changeIndex] = changeValue

chars.pop(int(input('Which element shoukd be deleted: ')) - 1)

chars.append(input('Which element should be added to the list: '))

print(chars)