from agents.AgenteSimples import AgenteSimples
from agents.AgenteGenerico import AgenteGenerico
import utils.Pontos as pontosService
from random import randint
# import numpy as np

#Função auxiliar para imprimir o space no terminal. 
def printSpace(space):
    for i in range (0,19):
        for j in range (0,19):
            print(f"[{space[i][j]}] ",end="")
        if (j == 18): print("|\n")

#Função para verificar elemento da position atual
def verifySpace(pos, space):
    if (space[pos[0]][pos[1]] == '_'):
        return 'vazio'
    elif (space[pos[0]][pos[1]] == 'vermelho'):
        return 'vermelho'
    elif (space[pos[0]][pos[1]] == 'azul'):
        return 'azul'

#Retonar agente para [0,0]
def returnBase(agente):
    pos = agente.getPosition()
    x = pos[0]
    y = pos[1]
    while(y != 0):
        y -= 1 
        print("andei p esquerda voltando p base")    
    while(x != 0):
        x -= 1
    agente.setPosition([x,y])
    print(f"estou na posicao {x} {y}")
    agente.setHasItem(False)

#   ** Funcao de ação do agente para coletar e voltar para base
# * A ideia da função é pegar o valor onde está o ponto, verificar se ele é azul ou vermelho
# * e a partir disso, incrementar a quantidade de pontos coletados, transformar a posicao coletada em
# * 'vazio' e além disso, atualizar o space e retornar o Agente para base.
def collectPoint(positionPoint, collectedPoints, pointColor, agente): 
    positionX = positionPoint[0]
    positionY = positionPoint[1]
    if (agente.getHasItem() == False) :
        if (pointColor == 'azul'): 
            agente.setCollectedPoints(agente.getCollectedPoints() + 10)
            agente.setHasItem(True)
            returnBase(agente)
        elif (pointColor == 'vermelho'): 
            agente.setCollectedPoints(agente.getCollectedPoints() + 20)
            agente.setHasItem(True)
            returnBase(agente)
    else:
        returnBase(agente)
    
    print("minha pontuacao atual é de: ", agente.getCollectedPoints())
    # positionAgent = [0,0] #agente retornando para base 


#Função que retorna a posição atual do agente no space e imprime no terminal o valor. 
def currentPosition(space):
    # printSpace(space)
    x = 0
    y = 0
    for i in range (len(space)):
        for j in range (len(space)):
            if space[i][j] == 'agente':
                print(f"Oi, sou o Agente e estou na posição X={i} Y={j}.")
                x = i
                j = y
    return [x,y] #retorna vetor com par da posicao do agente -> agente inicia na origem(0,0)

#Função para movimentar o agente na matriz. 
def move(space, nextPosition, agente):
    # agentPosition = currentPosition(space)
    agentPosition = agente.getPosition()
    # print("current ", agentPosition)
    x = agentPosition[0]
    y = agentPosition[1]
    
    print(agente.getHasItem(), "ta como item?")
    while (agente.getHasItem() == False and agente.getCollectedPoints() < 300):
        for i in range(len(space)):
            for j in range(len(space)):
                if (space[x][y]== 'vermelho'):
                    collectPoint([x,y], collectedPoints, 'vermelho', agente)
                    print('acabei de coletar um vermelho')
                    agente.setPosition([x,y])
                    returnBase(agente)
                    space[x][y] = 'vazio'
                    move(space,[0,0], agente)
                elif (space[x][y] == 'azul'):
                    collectPoint([x,y], collectedPoints, 'azul', agente)
                    print('acabei de coletar um azul')
                    returnBase(agente)
                    space[x][y] = 'vazio'
                    move(space,[0,0], agente)
                if (y % 2 == 0 and x < 19) : 
                    print(f"Estou na posicao {x} {y} que é da cor: {space[x][y]} e estou com item? {agente.getHasItem()}")
                    x += 1
                    print('andei p direita')
                    print(f"Agora Estou na posicao {x} {y} \n")
                elif (y % 2 != 0 and x > 0):     
                    print(f"Estou na posicao {x} {y} que é da cor: {space[x][y]} e estou com item? {agente.getHasItem()}")
                    x -= 1
                    print('andei p esquerda')
                    print(f"Agora Estou na posicao {x} {y} \n")
                if (x == 19 or x == 0 and 0<=y<19):
                    y += 1
                    print("andei p baixo")

                # printSpace(space)
                agente.setPosition([x,y])
                # space[x][y] = 'agente'
        agente.setPosition([x,y])
                
    # if (agentPosition[y] % 2 != 0): #se o valor de Y for impar, ele deve caminhar pra esquerda
    #     while (agentPosition[x][y] < 19): #enquanto não bater na borda da matriz
    #         agentPosition[x] = agentPosition[x-1]
    #         print("o agente se moveu para a posicao")
    #         if (agentPosition[x][y] == 'azul' or agentPosition[x][y] == 'vermelho'):
    #             collectPoint(agentPosition[x][y], space, collectedPoints, space[x][y]) #se encontrar ponto, deve coletar
    #             space[x][y] = 'vazio'
    #     if (agentPosition[x] == 19): # se bater na borda, tem que descer 
    #         agentPosition[y] = agentPosition[y+1]
    #         space[x][y] = 'vazio'
    #         space[agentPosition[x]][agentPosition[y]] = 'agente'

    # else :     #se o valor de Y for par, ele deve caminhar pra direita
    #     while (x < 19): #enquanto não bater na borda da matriz
    #         # agentPosition[x] = agentPosition[x+1]
    #         x =+ 1
    #         if (space[x][y] == 'azul' or space[x][y] == 'vermelho'): #se encontrar ponto, deve coletar
    #             collectPoint(agentPosition[x][y], space, collectedPoints, space[x][y])
            
    #     if (agentPosition[x] == 19): # se bater na borda, tem que descer 
    #         agentPosition[y] = agentPosition[y+1]
    # print(space[agentPosition[x]][agentPosition[y]])
    return space

class Main:
    #Variaveis globais
    space = (pontosService.geradorPontos()) # criando ambiente -> gerando a matriz 20x20 e distribuindo os pontos vermelhos e azuis
    printSpace(space)
    global collectedPoints
    collectedPoints = 0 #pontos que o agente já coletou, comeca de 0.

    #Definindo acoes do agente
    localizacaoAgente = currentPosition(space)
    acoesAgente = ['collectPoint', 'currentPosition', 'move', 'returnBase']
    percepcoesAgente = []

    # instanciando agente simples 
    agenteSimples = AgenteSimples(acoes=acoesAgente, percepcoes=percepcoesAgente , localizacao=localizacaoAgente, collectedPoints=collectedPoints)

    while (agenteSimples.getCollectedPoints() < 300):
        move(space, [0,0], agenteSimples)
        # printSpace(space)

    for i in range(19):
        for j in range(19):
            if (space[i][j] != 'vermelho' or space[i][j] != 'azul'):
                printSpace(space)
    