from random import randint
from random import sample
# import numpy as np

def geradorPontos():
    Pontos = []
    cont = 0
    space = [] 
    qtdAzul = 0
    qtdVermelho = 0

    for i in range(20):
        space.append(['vazio'] * 20)

  
    print(len(space))
    while cont < 20:
        random_c = randint(0, 19) 
        random_l = randint(0, 19) 

        if (random_c, random_l) not in Pontos:
            # Pontos.append([random_c, random_l])
            # Pegando um valor aleatorio pra fazer a proxima operacao, colocar 20 pontos, 10 azuis e 10 vermelhos
            # Ficou meio extenso o código, se der tempo a gente simplifica isso
            # Necessário testar 100%
            # Após testar, remover os prints

            # space[random_c][random_l] = 'azul'
            random_value = sample(set([1, 2]), 1)  

            if (random_value[0] == 1 and qtdAzul< 10): 
                random_value = space[random_c][random_l] = 'azul'
                qtdAzul += 1  
                print("Coloquei mais um azul na posicao {} {}, no total tem {} azul".format(random_c,random_l,qtdAzul))
            elif (random_value[0] == 2 and qtdVermelho < 10):  
                space[random_c][random_l] = 'vermelho' 
                qtdVermelho += 1
                print("Coloquei mais um vermelho na posicao {} {}, no total tem {} vermelho".format(random_c,random_l,qtdVermelho))
            elif (random_value[0] == 1 and qtdAzul == 10):
                space[random_c][random_l] = 'vermelho' 
                qtdVermelho += 1
                print("Coloquei mais um vermelho na posicao {} {}, no total tem {} vermelho".format(random_c,random_l,qtdVermelho))
            elif (random_value[0] == 1 and qtdVermelho == 10):   
                space[random_c][random_l] = 'vermelho' 
                qtdVermelho += 1
                print("Coloquei mais um vermelho na posicao {} {}, no total tem {} vermelho".format(random_c,random_l,qtdVermelho))
                
        cont += 1 

    # for i in range(len(space)):
    #     # for j in range (len(space)):
    #     for j in Pontos:
    #         firstItem = j[0]
    #         secondItem = j[1]
    #         if (firstItem == i):
    #             space[i][j] = [firstItem]
    #             print("Valor atual de J", j, firstItem, secondItem)
    #             print(space[i])
    #         elif (secondItem == i):
    #             space[i] = [secondItem]

    #         # space[firstItem][secondItem] = j[0][1]    
    print(space)      
    return space

# bem simples ainda, só um gerador de coordenada entre 0 e 20, vai precisar de alteração