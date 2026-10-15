#Exercise 8

n = int(input('Enter the lower boundary: '))
m = int(input('Enter the upper boundary: '))

if n > m:
    n, m = m, n

sum = 0

for i in range(10):
    newNum = int(input())
    if n <= newNum <= m:
        sum += 1

print('The amount of numbers set in the boundaries: ', sum)