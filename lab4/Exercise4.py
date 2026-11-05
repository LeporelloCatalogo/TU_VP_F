'''
Създайте програма– мини телефонен указател. Потребителят въвежда 3
контакта (име като ключ и телефонен номер като стойност). След като
въвеждането приключи, програмата пита за име за търсене:
'''
telephone = dict()
for i in range(3):
    name = input('Dials name: ')
    number = input('Dials number: ')
    telephone[name] = number

getName = input('Which dial are you searching: ')
if getName in telephone:
    print(telephone[getName])