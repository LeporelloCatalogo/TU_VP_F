

n = abs(int(input('Type the number to tell if its a Prime: ')))

Prime = True

if n > 2:
    for i in range(2, (n // 2 + 1)):
        if n % i == 0:
            Prime = False
            break

if Prime == True:
    print('It is a Prime')
else:
    print('Its not a Prime')