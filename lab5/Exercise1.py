'''
Напишете програма, която намира  лицето на геометрична фигура като първо се въвежда вида на фигурата:  

    1- квадрат   

    2-правоъгълник   

    3- прав.триъгълник  

За пресмятане на лицето на отделните фигури да се напишат подходящи функции.
'''

def square(side):
    return side*side

def rectangle(a,b):
    return a*b

def rightTriangle(a,b):
    return a*b/2


which = input('Which figure:\n1. Square\n2. Rectangle\n3. Right Triangle\n')
match which:
    case '1':
        side = int(input('Side: '))
        print(square(side))
    case '2':
        a = int(input('Side a: '))
        b = int(input('Side b: '))
        print(rectangle(a,b))
    case '3':
        a = int(input('Side a: '))
        b = int(input('Side b: '))
        print(rightTriangle(a,b))

    