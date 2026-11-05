'''
Да се напише програма, която въвежда m низа за ключ и m цели 
числа за стойност от клавиатурата и ги записва в речник. Програмата да 
извърши следните обработки: търси избран ключ в речника, променя 
стойността на елемент от речника по неговия ключ, изтрива елемент от 
речника по ключ, извежда всички ключове от речника, извежда всички 
стойности от речника, сортира речника по ключове. Извеждането на 
съдържанието на речника да се прави с обхождане на елементите му по ключ
'''

m = int(input('Dictionary capacity: '))
rechnik = dict()
for i in range(m):
    print(i+1)
    rechnik[int(input('Key: '))] = input('Value: ')

keyPerValue = input('Key per Value: ')
for i in rechnik:
    if rechnik[i] == keyPerValue:
        print(f'Key: {i}')
        break

print(rechnik)
print('Change element: ')
rechnik[input('Key: ')] = input('New Value: ')

del rechnik[int(input('Delete element per key. Key: '))]

print(rechnik.keys())

print(rechnik.values())

sorted_keys = sorted(rechnik.keys())

for i in sorted_keys:
    print(f'{i} : {rechnik[i]}')