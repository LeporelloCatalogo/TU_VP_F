#Exercise 7

n = float(input('Enter the first number: '))
m = float(input('Enter the second number: '))

operation = input('Enter the operation from this list: *, /, +, -   ')

if operation in ['*', '/', '+', '-']:
    match operation:
        case '*':
            print(f'{n} * {m} = {n*m}')
        case '/':
            if m != 0:
                print(f'{n} / {m} = {n/m}')
            else:
                print('Cant divide by 0')
        case '+':
            print(f'{n} + {m} = {n+m}')
        case '-':
            print(f'{n} - {m} = {n-m}')

