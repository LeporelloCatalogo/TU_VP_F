import math
# 1

a = float(input('\nType the first trapezoid side: '))
b = float(input('Type the second trapezoid side: '))
h = float(input('Type the trapezoid height: '))

sTr = (a + b)*h/2
print('Trapezoid square: ', round(sTr, 2))

# 2

r = float(input('\nType the radius of the circle: '))
sCir = math.pi*r**2
pCir = math.pi*r*2

print('Area of the circle: ', sCir)
print('Perimeter of the circle: ', pCir)

#3

hours = float(input('\nEnter hours: '))
rate = float(input('Enter rate: '))
pay = hours*rate
print('Pay: ', pay)