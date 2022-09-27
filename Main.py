from agents.AgenteSimples import AgenteSimples
from agents.AgenteGenerico import AgenteGenerico
import utils.Pontos as pontosService
from random import randint
# import numpy as np

#Função auxiliar para imprimir o space no terminal. 
def printSpace(space):
    for i in space:
        print(i, "\n")

#   ** Funcao de ação do agente para coletar e voltar para base
# * A ideia da função é pegar o valor onde está o ponto, verificar se ele é azul ou vermelho
# * e a partir disso, incrementar a quantidade de pontos coletados, transformar a posicao coletada em
# * 'vazio' e além disso, atualizar o space e retornar o Agente para base.
def collectPoint(positionPoint, space, collectedPoints, positionAgent): 
    positionX = positionPoint[0]
    positionY = positionPoint[1]

    if (space[positionX][positionY] == 'azul'): collectedPoints += 10
    elif (space[positionX][positionY] == 'vermelho'): collectedPoints += 20

    space[positionX][positionY] = 'vazio' #atualizando ponto coletado para vazio

    positionAgent = [0,0] #agente retornando para base 
    return space


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
def move(space, nextPosition):
    agentPosition = currentPosition(space)
    x = agentPosition[0]
    y = agentPosition[1]

    if (agentPosition[y] % 2 != 0): #se o valor de Y for impar, ele deve caminhar pra esquerda
        while (agentPosition[x][y] < 19): #enquanto não bater na borda da matriz
            agentPosition[x] = agentPosition[x-1]
        if (agentPosition[x] == 19): # se bater na borda, tem que descer 
            agentPosition[y] = agentPosition[y+1]

    else :     #se o valor de Y for par, ele deve caminhar pra direita
        while (agentPosition[x] < 19): #enquanto não bater na borda da matriz
            agentPosition[x] = agentPosition[x+1]
        if (agentPosition[x] == 19): # se bater na borda, tem que descer 
            agentPosition[y] = agentPosition[y+1]
    
    return space

class Main:
    # criando ambiente -> gerando a matrix 20x20 e distribuindo os pontos vermelhos e azuis
    space = (pontosService.geradorPontos())

    #Definindo acoes do agente
    acoesAgente = ['collectPoint', 'currentPosition', 'move', 'returnBase']
    percepcoesAgente = []
    localizacaoAgente = currentPosition(space)
    print(localizacaoAgente)
    # instanciando agente simples 
    # agenteSimples = AgenteSimples(acoes=acoesAgente, percepcoes=percepcoesAgente , localizacao=localizacaoAgente)
