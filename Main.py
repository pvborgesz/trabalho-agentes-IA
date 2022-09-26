import agents.AgenteSimples as AgenteSimples
import agents.AgenteGenerico as AgenteGenerico
import utils.Pontos as geradorPontos
from random import randint
# import numpy as np

def printSpace(positionPoints):
    for i in range(len(positionPoints)):
        print(positionPoints[i])


def createSpace(positionPoints):
    space = []
    for i in range(20):
        for j in range(20):
            space.append(0)

    return space

class Main:
    # def __init__(self,val):
    
    teste = (geradorPontos.geradorPontos())
    # for i in range(40):
    #     if(teste[0] != 'vazio' or teste[1] != 'vazio'):
    #         print(teste[i] , "na posicao",i)

    # print(len(geradorPontos.geradorPontos()))
    # print(printSpace(geradorPontos.geradorPontos()))
    acoes = ["andar", "coletar", "retornar"]
    percepcoes = ["ver"]
    localizacao = [0,0]
    agenteSimplesInstance = AgenteGenerico.AgenteGenerico(acoes=acoes, percepcoes=percepcoes, localizacao=localizacao)
    # print(teste)
