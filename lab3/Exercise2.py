'''
Напишете програма, в която се създава числов списък. 
Той  се запълва със случайни числа.
След това между всяка двойка елементи от този списък се вмъква нов , 
равен на сумата от стойностите на съседните елементи. 
'''
import random

n = int(input('Define how many numbers should the initial list have: '))
numbers = []
numbersNew = []

for i in range(n):
    numbers.append(random.randint(1,100))

for i in range(0, n, 2):
    numbersNew.append(numbers[i])
    numbersNew.append(numbers[i] + numbers[i+1])
    numbersNew.append(numbers[i+1])

print(numbers)
print(numbersNew)