from agents.AgenteSimples import AgenteSimples
from agents.AgenteGenerico import AgenteGenerico
from agents.AgenteCModelos import AgenteCModelos
import utils.Pontos as pontosService
from random import randint
import time
start_time = time.time()

# import numpy as np
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


def moveCModelo(space, agente):
    # try:
        lastPosition = agente.getLastPosition()
        print(lastPosition)
        x = lastPosition[0]
        y = lastPosition[1]

        for i in range (len(space)):
            for j in range (len(space)):
                while (j != y and y != 0): #chegar na ultima posicao
                    j += 1
                while (i != x and x != 0):
                    x += 1 
        agente.setPosition([i,j]) 
        print('coemcando move dnv', agente.getPosition())           
        move(space, [0,0], agente) 

    # except Exception as e:
    #     print(e, "-> moveCmodelo")

# Funcao para verificar se ainda existe algum ponto a ser coletado
def hasPoints(space):
    flagHasPoints = False
    for i in range(len(space)):
        for j in range(len(space)):

            if (space[i][j] == 'vermelho' or space[i][j] == 'azul'):
                flagHasPoints = True
                print(i,j, space[i][j])
                break
    return flagHasPoints
                
                
    # print(space)
 
    # if (not flagHasPoints):
        # print("não temos mais itens a ser coletados. parece que o trabalho foi concluido. ")
    return flagHasPoints

#Função auxiliar para imprimir o space no terminal. 
def printSpace(space):
    for i in range (0,19):
        for j in range (0,19):
            if (space[i][j] == 'vermelho'): 
                print( "\033[1;31m"  + f"[{space[i][j]}]" , end="" + bcolors.RESET)
            elif (space[i][j] == 'azul'): 
                print("\033[1;34m"+ f"[{space[i][j]}]" , end="" + bcolors.RESET)
            else:
                print(f"[{space[i][j]}] ",end="")
        if (j == 18): print("|\n")

    print('\n\n\n')
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
        # print("andei p esquerda voltando p base")    
    while(x != 0):
        x -= 1
    agente.setPosition([x,y])
    # print(f"estou na posicao {x} {y}")
    agente.setHasItem(False)

#   ** Funcao de ação do agente para coletar e voltar para base
# * A ideia da função é pegar o valor onde está o ponto, verificar se ele é azul ou vermelho
# * e a partir disso, incrementar a quantidade de pontos coletados, transformar a posicao coletada em
# * 'vazio' e além disso, atualizar o space e retornar o Agente para base.
def collectPoint(positionPoint, collectedPoints, pointColor, agente,space): 
    x = positionPoint[0]
    y = positionPoint[1]
    if (agente.getHasItem() == False) :
        if (pointColor == 'azul'): 
            space[x][y] = 'vazio'
            agente.setCollectedPoints(agente.getCollectedPoints() + 10)
            agente.setHasItem(True)
            printSpace(space)
            returnBase(agente)
            print("minha pontuacao atual é de: ", agente.getCollectedPoints())
            return True
        elif (pointColor == 'vermelho'): 
            space[x][y] = 'vazio'
            agente.setCollectedPoints(agente.getCollectedPoints() + 20)
            agente.setHasItem(True)
            printSpace(space)
            returnBase(agente)
            print("minha pontuacao atual é de: ", agente.getCollectedPoints())
            return True
    
    # printSpace(space)
    if (isinstance(agenteCModelos, AgenteCModelos)):
        agente.setLastPosition(x,y)
        print ("oi, sou o agente e coletei em ", agente.getLastPosition())
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

    if (agentPosition[0] == 19 and agentPosition[1] == 19): returnBase(agente)
    x = agentPosition[0]
    y = agentPosition[1]

    while (hasPoints(space)==True and agente.collectedPoints < 150):
        for i in range(len(space)):
            for j in range(len(space)):
                flag = hasPoints(space)
                if (space[x][y]== 'vermelho' and not agente.getHasItem()):
                    flagCollected = collectPoint([x,y], collectedPoints, 'vermelho', agente, space)
                    # print('acabei de coletar um vermelho')
                    if (flagCollected): 
                        space[x][y] = 'vazio'
                        print("coletei e deixei vazio")
                    printSpace(space)
                    returnBase(agente)
                    # space[x][y] = 'vazio'
                elif (space[x][y] == 'azul' and not agente.getHasItem()):
                    flagCollected = collectPoint([x,y], collectedPoints, 'azul', agente, space)
                    # print('acabei de coletar um azul')
                    returnBase(agente)
                    if (flagCollected): space[x][y] = 'vazio'
                if (y % 2 == 0 and x < 19) : 
                    # print(f"Estou na posicao {x} {y} que é da cor: {space[x][y]} e estou com item? {agente.getHasItem()}")
                    x += 1 
                    # print('andei p direita')
                    # print(f"Agora Estou na posicao {x} {y} \n")
                    if (flag):                    
                        returnBase(agente)
                        break
                elif (y % 2 != 0 and x > 0):     
                    # print(f"Estou na posicao {x} {y} que é da cor: {space[x][y]} e estou com item? {agente.getHasItem()}")
                    x -= 1
                    # print('andei p esquerda')
                    # print(f"Agora Estou na posicao {x} {y} \n")
                    if (flag):                    
                        returnBase(agente)
                        break
                if (x == 19 or x == 0 and y<19):
                    y += 1
                    # print("andei p baixo")
                    if (flag):                    
                        returnBase(agente)
                        break
                if (agente.getPosition()[0] == 0 and agente.getPosition()[1]==19 and not hasPoints(space)):
                    returnBase(agente)
                    break
                
                flag = hasPoints(space)
                if (flag):                    
                    returnBase(agente)
                    break
                agente.setPosition([x,y])
                # space[x][y] = 'agente'
        agente.setPosition([x,y])
    return space

class Main:
    #Variaveis globais)
    space = (pontosService.geradorPontos()) # criando ambiente -> gerando a matriz 20x20 e distribuindo os pontos vermelhos e azuis
    # printSpace(space)
    global collectedPoints
    collectedPoints = 0 #pontos que o agente já coletou, comeca de 0.

    #Definindo acoes do agente
    localizacaoAgente = currentPosition(space)
    acoesAgente = ['collectPoint', 'currentPosition', 'move', 'returnBase']
    percepcoesAgente = []

    # instanciando agente simples 
    agenteSimples = AgenteSimples(acoes=acoesAgente, percepcoes=percepcoesAgente , localizacao=localizacaoAgente, collectedPoints=collectedPoints)
    agenteCModelos = AgenteCModelos(acoes=acoesAgente, percepcoes=percepcoesAgente , localizacao=localizacaoAgente, collectedPoints=collectedPoints)

    agenteCModelos.setMapa(space)


    moveCModelo(space, agenteCModelos) 
    # move(space, [0,0], agenteSimples) # agente simples
    # print(agenteSimples.getCollectedPoints())
   
    # print((type(agenteCModelos)))
    # print(isinstance(agenteCModelos, AgenteCModelos))
    print("--- Tempo de execucao de: %s segundos ---" % (time.time() - start_time))
        # printSpace(space)

    # for i in range(19):
    #     for j in range(19):
    #         if (space[i][j] != 'vermelho' or space[i][j] != 'azul'):
    #             printSpace(space)
    