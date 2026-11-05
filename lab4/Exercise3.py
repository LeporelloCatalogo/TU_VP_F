'''
Потребителят въвежда списък от думи (разделени с интервал) и цяло число k.
Напишете програма, която филтрира думите и запазва в кортеж само тези думи,
чиято дължина е по-голяма или равна на k

'''

dumiOld = set(input('Type your list of words: ').split())
k = int(input("Minimal chars: "))

dumi = set()
for i in dumiOld:
    if k <= len(i):
        dumi.add(i)

dumiTuple = tuple(dumi)
print(dumiTuple)
