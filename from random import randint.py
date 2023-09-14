from random import randint
a = randint(1,100)
pop = 1
while True:
    b = int(input())
    if a>b:
        print('Слишком мало')
        pop += 1
    if a<b:
        print('Слишком много')
        pop += 1
    if a==b:
        print('Вы угадали с ', pop, 'попыток')
        break
