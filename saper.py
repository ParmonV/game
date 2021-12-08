import random

N, M = (5,10)# размер поля N*N и кол-во мин

def totalMins(PM,i,j):
    n=0
    for k in range(-1,2):
        for l in range(-1,2):
            x = i + k
            y = j + l
            if x<0 or x>=N or y<0 or y>=N:
                continue
            if PM[x*N+y] < 0:
                n +=1
    return n

def createGame(PM):
    '''Создает игровое поле:расположение мин и подсчет числа мин вокруг клеток без мин'''
    n = M
    rnd = random.Random()
    while n>0:
        i = rnd.randrange(N)
        j = rnd.randrange(N)
        if PM[i*N+j]!=0:
            continue
        PM[i*N+j] = -1
        n -= 1

    #вычисляем количество мин вокруг клетки
    for i in range(N):
        for j in range(N):
            if PM[i*N+j]== 0:
                PM[i*N+j] = totalMins(PM,i,j)
            
    

def show(pole):
    '''Функция отображения состояния текущего игорового поля'''
    for i in range(N):
        for j in range(N):
            print(str(pole[i*N+j]).rjust(3), end='')
        print()


def goPlayer():
    flag=True
    while flag:
        x,y = input("Enter координаты через пробел").split()
        if not x.isdigit() or not y.isdigit():
            print("Координаты введены не верно")
            continue

        x = int(x)-1
        y = int(y)-1

        if x<0 or x>=N or y<0 or y>=N:
            print("Cлишком большие значения координат")
            continue

        flag = False
    return (x,y)
                  
def isFinish(PM,P):

    for i in range(N*N):
        if P[i] != -2 and PM[i] < 0: return -1
    for i in range(N*N):
        if P[i] == -2 and PM[i] >= 0:return 1

    return -2       

def startGame():
    '''Запуск игры,отображение экрана игры'''
    PM = [0]*N*N
    P = [-2]*N*N

    createGame(PM)
    finishstate = isFinish(PM,P)
    while finishstate > 0 :
        show(P)
        x,y = goPlayer()
        P[x*N+y] = PM[x*N+y]
        finishstate = isFinish(PM,P)

    return finishstate

rec = startGame()
if rec == -1:
    print("Game over")
else:
    print("Win")


