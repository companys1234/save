import random
a=[1,2,3,4,5,6,7,8,9,10]
sad=0
user=random.choices(a)
usera=random.choices(a)
e=random.choices(a)
f=random.choices(a)
g=random.choices(a)
sas=random.choices(a)
print(user)
print("хотите продолжить?")
d=str(input())
t=0
if d == "нет":
    if user > f:
        print("вы победили!")
    if user < f:
        print("вы проиграли!")
    if user == f:
        print("ничья!")

if d == "да":
    print(user,usera)
    print("хотите продолжить?")
    r =str(input())
if r == "да":
        print(user,usera,e)
# если чо замени в else условие чтобы была одна конструкция и попробуй добавит ещё else с этой конструкцией



        if user > f :
            sad += 1
        else:
            user < f
            sad += 0
            user == f
            sad += 0
            if usera > g:
                sad += 1
            else:
                usera < g
                sad += 0
                usera == g
                sad += 0
                if e > sas:
                    sad += 1
                else:
                    e < sas
                    sad += 0
                    e == sas
                    sad += 0
            print("враг")
            print(f)
            print(g)
            print(sas)
        if sad == 3:
            print('вы победили!')
            print("враг")
            print(f)
            print(g)
            print(sas)
        if sad == 2:
            print('вы победили!')
            print("враг")
            print(f)
            print(g)
            print(sas)
        if sad == 1:
            print('проигрыш')
            print("враг")
            print(f)
            print(g)
            print(sas)
        if sad == 0:
            print('проигрыш')

if r == "нет":
    if user > usera:
        print("вы победили!")
    if user < usera:
        print("вы проиграли!")
    if user == usera:
        print("ничья!")
