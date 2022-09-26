from random import randint
# import numpy as np

def geradorPontos():
    Pontos = []
    cont = 0
    space = [] 

    for i in range(20):
        space.append(['vazio'] * 20)

    while cont < 20:
        random_c = randint(0, 20) #ponto azul
        random_l = randint(0, 20) #ponto vermelho

        if (random_c, random_l) not in Pontos:
            Pontos.append([random_c, random_l])
        cont += 1 

    for i in range(len(space)):
        # for j in range (len(space)):
        for j in Pontos:
            firstItem = j[0]
            secondItem = j[1]
            if (firstItem == i):
                space[i][j] = [firstItem]
                print("Valor atual de J", j, firstItem, secondItem)
                print(space[i])
            elif (secondItem == i):
                space[i] = [secondItem]

            # space[firstItem][secondItem] = j[0][1]          
    return space

# bem simples ainda, só um gerador de coordenada entre 0 e 20, vai precisar de alteração