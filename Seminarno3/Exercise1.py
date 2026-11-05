'''
Да се напише програма, която въвежда последователност от цели 
числа от клавиатурата, потребителя определя брой елементи и ги записва в 
списък. Програмата да извърши следните обработки: отпечатва утроения 
списък, извежда елементите на списъка един по един, проверява списъка за 
наличие на въведен от потребителя елемент в списъка, сортира списъка, 
намира максималния по стойност елемент, изтрива елемент от списъка с 
избран от потребителя индекс и променя стойността на избран елемент от 
списъка.
'''

n = int(input('List capacity: '))
nums = list()
for i in range(n):
    nums.append(int(input(f'{i+1} number: ')))

print(nums*3)
for i in nums:
    print(i)

if int(input('Check if selected number is in the list: ')) in nums:
    print('List does contain this number')
else:
    print('list doesnt contain this number')

nums.sort()

print(f'Biggest number in the list {max(nums)}')

indexDel = int(input('Pick a number to delete by its index: '))
nums.pop(indexDel - 1)

indexChange = int(input('Pick a number by its index to change: ')) - 1
newNum = int(input('Which number should it be changed to: '))
nums[indexChange] = newNum

print(nums)