from random import randint
from random import sample
# import numpy as np

# print(bcolors.FAIL + "Unable to delete record." + bcolors.RESET)

def geradorPontos():
    Pontos = []
    cont = 0
    space = [] 
    qtdAzul = 0
    qtdVermelho = 0

    for i in range(20):
        space.append(['_'] * 20)

  
    # print(len(space))
    space[0][0] = 'agente'
    while cont < 10:
        random_c = randint(0, 19) 
        random_l = randint(0, 19) 

        if (random_c, random_l) not in Pontos:
            # Pontos.append([random_c, random_l])

            # --------- IMPORTANTE ------------------
            # Pegando um valor aleatorio pra fazer a proxima operacao, colocar 20 pontos, 10 azuis e 10 vermelhos
            # Ficou meio extenso o código, se der tempo a gente simplifica isso
            # Necessário testar 100%
            # Após testar, remover os prints
            # ---------------------------------------

            random_value = sample(set([1, 2]), 1)  

            if (random_value[0] == 1 and qtdAzul< 5): 
                random_value = space[random_c][random_l] = 'azul'
                qtdAzul += 1  
                # print("Coloquei mais um azul na posicao {} {}, no total tem {} azul".format(random_c,random_l,qtdAzul))
            elif (random_value[0] == 2 and qtdVermelho <= 5):  
                space[random_c][random_l] = 'vermelho' 
                qtdVermelho += 1
                # print("Coloquei mais um vermelho na posicao {} {}, no total tem {} vermelho".format(random_c,random_l,qtdVermelho))
            elif (random_value[0] == 1 and qtdAzul < 5):
                space[random_c][random_l] = 'vermelho' 
                qtdVermelho += 1
                # print("Coloquei mais um vermelho na posicao {} {}, no total tem {} vermelho".format(random_c,random_l,qtdVermelho))
            elif (random_value[0] == 1 and qtdVermelho <= 5):   
                space[random_c][random_l] = 'vermelho' 
                qtdVermelho += 1
                # print("Coloquei mais um vermelho na posicao {} {}, no total tem {} vermelho".format(random_c,random_l,qtdVermelho))
                
        cont += 1    
    return space

# bem simples ainda, só um gerador de coordenada entre 0 e 20, vai precisar de alteração