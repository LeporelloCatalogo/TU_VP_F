'''
На функция се подават два аргумента: списък с числа и число. 
Променете всички елементи от списъка 
със стойност по-голяма от даденото число на 0(нула).
'''

def removeBiggerThanNum (nums, num):
    newNums = list(nums)
    for i in range(len(nums)):
        if nums[i] > num:
            newNums[i] = 0
    return newNums

nums = (1,14,15,16,20,3)
num = 15

print(removeBiggerThanNum(nums, num))


