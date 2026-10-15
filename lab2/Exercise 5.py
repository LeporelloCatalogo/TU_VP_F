#Exercise 5

n = int(input('Enter the day of your choosing: '))
if 0 < n <= 7:
    match n:
        case 1:
            print('Monday')
        case 2:
            print('Tuesday')
        case 3:
            print('Wednesday')
        case 4:
            print('Thursday')
        case 5:
            print('Friday')
        case 6:
            print('Saturday')
        case 7:
            print('Sunday')
else:
    print('No such day')