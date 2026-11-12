'''
Напишете потребителска функция , проверяваща дали число е палиндром. 
Функцията получава като аргумент число, връща като резултат 1, 
ако числото е палиндром и 0 ако числото не е палиндром. 
'''

def isPalindrome(text):
    text = str(text)
    if text == text[::-1]:
        return 1
    else:
        return 0

num = int(input('Type your number: '))
print(isPalindrome(num))