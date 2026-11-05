'''
Напишете програма на Python, която създава речник от 7 въведени 
от потребителя низа и съответстващите им цели числа и извършва следните 
обработки: разпечатва съдържането на речника, определя на кой ключ 
съответства най-голямото въведено цяло число от записаните в речника, 
заменя стойността въведена за избран ключ с друга въведена от потребителя, 
изтрива стойност от речника по нейния ключ и добавя нова стойност в речника 
заедно с нейния ключ. 
'''
rechnik = dict()
for i in range(7):
    print(i+1)
    rechnik[input('Key: ')] = int(input('Value: '))

print(rechnik.values())

for key in rechnik:
    if rechnik[key] == max(rechnik.values()):
        print(f'Key per Max Value: {key}')

print('Which element to change:')
keyChange = input('Key: ')
valueChange = int(input('Value: '))
rechnik[keyChange] = valueChange

del rechnik[input('Delete element per key. Key: ')]

print('Add new element')
rechnik[input('Key: ')] = int(input('Value: '))