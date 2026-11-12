'''
Програма, която реализира калкулатор за цели числа. Действията които изпълнява са :    

    Събиране +  

   Изваждане  –  

 Умножение *  

   Деление /  

Потребителя въвежда вида на операцията.  

После въвежда две числа и резултата се извежда на екрана . Реализирайте отделни функции за отделните операции. 
'''

def calculator(operation):
    a = int(input())
    b = int(input())
    match operation:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            if b == 0:
                return 'Non defined'
            else:
                return a/b

operation = input('Choose the algebraic operation: ')

print(f'Result: {calculator(operation)}')