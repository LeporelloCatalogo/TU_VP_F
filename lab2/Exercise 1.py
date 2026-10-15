#Exercise 1

n = int(input('Pick the amount of numbers to compare: '))
previousNum = 0

for i in range(n):
    newNum = int(input())
    if newNum > previousNum:
        previousNum = newNum

print("Largest input num: ", previousNum)
