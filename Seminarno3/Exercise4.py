'''
Да се напише програма, която създава две множества от m цели 
числа, въведени от клавиатурата и извършва следните операции с тях: 
определя размера на двете създадени множества, обединение на двете 
множества, разлика на двете множества, пресичане на двете множества, 
премахване на избран елемент от първо множество и изчистване на двете 
множества. 

'''

m = int(input('Sets capacity: '))

nums1 = list()
print('Fill the First Set:')
for i in range(m):
    nums1.append(int(input()))

nums2 = list()
print('Fill the Second Set:')
for i in range(m):
    nums2.append(int(input()))

nums1 = set(nums1)
nums2 = set(nums2)

print(nums1 | nums2)
print(nums1 - nums2)

print(nums1 & nums2)

nums1.discard(int(input('Which element should be removed from the First Set: ')))
print(nums1)

nums1.clear()
nums2.clear()
